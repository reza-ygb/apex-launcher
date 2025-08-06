#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Smart CLI Launcher - Terminal-based intelligent launcher
Works without GUI, perfect for headless systems
"""

import sys
import os
import subprocess
import json
from pathlib import Path

# Import the detector from smart_launcher
sys.path.insert(0, '/home/reza/code')
from smart_launcher import ApplicationDetector

class SmartCLILauncher:
    """Terminal-based smart launcher"""
    
    def __init__(self):
        self.detector = ApplicationDetector()
        self.applications = {}
        self.current_category = ""
        
    def load_applications(self):
        """Load and categorize applications"""
        print("🔍 Scanning for applications...")
        detected_apps = self.detector.detect_applications()
        
        total_apps = 0
        for category, apps in detected_apps.items():
            if apps:  # Only include categories with apps
                self.applications[category] = apps
                total_apps += len(apps)
                
        print(f"✅ Found {total_apps} applications in {len(self.applications)} categories")
        
    def show_main_menu(self):
        """Show main categories menu"""
        while True:
            print("\n" + "=" * 60)
            print("🚀 SMART ECHO LAUNCHER")
            print("=" * 60)
            
            categories = list(self.applications.keys())
            
            # Show categories
            for i, category in enumerate(categories, 1):
                count = len(self.applications[category])
                print(f"{i:2d}. 📁 {category:<20} ({count} apps)")
                
            print(f"\n{len(categories)+1:2d}. 🔍 Search applications")
            print(f"{len(categories)+2:2d}. 🔄 Refresh/Rescan")
            print(f"{len(categories)+3:2d}. ❌ Exit")
            
            try:
                choice = input("\n➤ Select option: ").strip()
                
                if not choice:
                    continue
                    
                choice_num = int(choice)
                
                if 1 <= choice_num <= len(categories):
                    selected_category = categories[choice_num - 1]
                    self.show_category_apps(selected_category)
                elif choice_num == len(categories) + 1:
                    self.search_applications()
                elif choice_num == len(categories) + 2:
                    self.load_applications()
                elif choice_num == len(categories) + 3:
                    print("\n👋 Goodbye!")
                    break
                else:
                    print("❌ Invalid option!")
                    
            except (ValueError, KeyboardInterrupt):
                print("\n👋 Goodbye!")
                break
                
    def show_category_apps(self, category: str):
        """Show applications in a category"""
        while True:
            apps = self.applications[category]
            
            print(f"\n📁 {category} ({len(apps)} applications)")
            print("-" * 60)
            
            # Show apps (paginated if too many)
            page_size = 20
            page = 0
            
            while True:
                start_idx = page * page_size
                end_idx = start_idx + page_size
                page_apps = apps[start_idx:end_idx]
                
                if not page_apps:
                    break
                    
                for i, app in enumerate(page_apps, start_idx + 1):
                    name = app['name'][:40] + "..." if len(app['name']) > 40 else app['name']
                    desc = app['description'][:30] + "..." if len(app['description']) > 30 else app['description']
                    source = f"[{app['source']}]"
                    print(f"{i:3d}. ⚡ {name:<43} {source:<8} {desc}")
                
                # Navigation options
                print()
                if end_idx < len(apps):
                    print(f"n. ➡️  Next page ({end_idx + 1}-{min(end_idx + page_size, len(apps))})")
                if page > 0:
                    print(f"p. ⬅️  Previous page")
                print("s. 🔍 Search in this category")
                print("b. ⬅️  Back to main menu")
                print("q. ❌ Quit")
                
                try:
                    choice = input(f"\n➤ Select app (1-{len(page_apps)}) or option: ").strip().lower()
                    
                    if choice == 'q':
                        return
                    elif choice == 'b':
                        return
                    elif choice == 's':
                        self.search_in_category(category)
                        break
                    elif choice == 'n' and end_idx < len(apps):
                        page += 1
                        continue
                    elif choice == 'p' and page > 0:
                        page -= 1
                        continue
                    else:
                        # Try to launch app
                        try:
                            app_num = int(choice)
                            if 1 <= app_num <= len(page_apps):
                                app = apps[start_idx + app_num - 1]
                                self.launch_application(app)
                            else:
                                print("❌ Invalid application number!")
                        except ValueError:
                            print("❌ Invalid input!")
                            
                except KeyboardInterrupt:
                    return
                    
                input("\nPress Enter to continue...")
                break
                
    def search_applications(self):
        """Search all applications"""
        query = input("\n🔍 Enter search term: ").strip()
        if not query:
            return
            
        found_apps = []
        for category, apps in self.applications.items():
            for app in apps:
                if self.matches_search(app, query):
                    found_apps.append((category, app))
                    
        if not found_apps:
            print(f"❌ No applications found for '{query}'")
            input("Press Enter to continue...")
            return
            
        print(f"\n🔍 Search results for '{query}' ({len(found_apps)} found)")
        print("-" * 70)
        
        for i, (category, app) in enumerate(found_apps, 1):
            name = app['name'][:30] + "..." if len(app['name']) > 30 else app['name']
            desc = app['description'][:25] + "..." if len(app['description']) > 25 else app['description']
            print(f"{i:3d}. ⚡ {name:<33} 📁{category:<12} {desc}")
            
        try:
            choice = input(f"\n➤ Select app (1-{len(found_apps)}) or Enter to go back: ").strip()
            if choice:
                app_num = int(choice)
                if 1 <= app_num <= len(found_apps):
                    _, app = found_apps[app_num - 1]
                    self.launch_application(app)
        except (ValueError, KeyboardInterrupt):
            pass
            
    def search_in_category(self, category: str):
        """Search within a specific category"""
        query = input(f"\n🔍 Search in {category}: ").strip()
        if not query:
            return
            
        apps = self.applications[category]
        found_apps = [app for app in apps if self.matches_search(app, query)]
        
        if not found_apps:
            print(f"❌ No applications found in {category} for '{query}'")
            input("Press Enter to continue...")
            return
            
        print(f"\n🔍 Found {len(found_apps)} apps in {category} for '{query}'")
        print("-" * 60)
        
        for i, app in enumerate(found_apps, 1):
            name = app['name'][:40] + "..." if len(app['name']) > 40 else app['name']
            desc = app['description'][:30] + "..." if len(app['description']) > 30 else app['description']
            print(f"{i:3d}. ⚡ {name:<43} {desc}")
            
        try:
            choice = input(f"\n➤ Select app (1-{len(found_apps)}) or Enter to go back: ").strip()
            if choice:
                app_num = int(choice)
                if 1 <= app_num <= len(found_apps):
                    app = found_apps[app_num - 1]
                    self.launch_application(app)
        except (ValueError, KeyboardInterrupt):
            pass
            
    def matches_search(self, app: dict, query: str) -> bool:
        """Check if app matches search query"""
        query = query.lower()
        search_fields = [
            app.get('name', '').lower(),
            app.get('command', '').lower(),
            app.get('description', '').lower()
        ]
        return any(query in field for field in search_fields)
        
    def launch_application(self, app: dict):
        """Launch an application"""
        print(f"\n🚀 Launching: {app['name']}")
        print(f"📝 Command: {app['command']}")
        if app['description']:
            print(f"💬 Description: {app['description']}")
            
        confirm = input(f"\n❓ Launch this application? (y/N): ").strip().lower()
        
        if confirm in ['y', 'yes']:
            try:
                print("⚡ Starting application...")
                subprocess.Popen(app['command'], shell=True, 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
                print("✅ Application launched successfully!")
            except Exception as e:
                print(f"❌ Failed to launch: {e}")
        else:
            print("❌ Launch cancelled")
            
        input("Press Enter to continue...")
        
    def run(self):
        """Run the launcher"""
        print("🚀 Smart Echo Launcher - CLI Edition")
        print("Loading applications...")
        
        try:
            self.load_applications()
            if not self.applications:
                print("❌ No applications found!")
                return
                
            self.show_main_menu()
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    """Main entry point"""
    launcher = SmartCLILauncher()
    launcher.run()

if __name__ == "__main__":
    main()
