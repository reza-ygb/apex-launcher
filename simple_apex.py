#!/usr/bin/env python3
"""
🚀 APEX LAUNCHER - Simple Version
One-file launcher for Linux applications

Just run: python3 simple_apex.py
"""

import sys
import os
import subprocess
import json
from pathlib import Path

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False

class SimpleApexLauncher:
    def __init__(self):
        self.apps = self.find_applications()
    
    def find_applications(self):
        """Find installed applications"""
        apps = []
        
        # Desktop files locations
        desktop_dirs = [
            "/usr/share/applications",
            "/usr/local/share/applications", 
            f"{Path.home()}/.local/share/applications"
        ]
        
        for directory in desktop_dirs:
            if os.path.exists(directory):
                for file in os.listdir(directory):
                    if file.endswith('.desktop'):
                        app_info = self.parse_desktop_file(os.path.join(directory, file))
                        if app_info:
                            apps.append(app_info)
        
        return sorted(apps, key=lambda x: x['name'].lower())
    
    def parse_desktop_file(self, filepath):
        """Parse .desktop file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            name = ""
            exec_cmd = ""
            icon = ""
            
            for line in content.split('\n'):
                if line.startswith('Name='):
                    name = line.split('=', 1)[1]
                elif line.startswith('Exec='):
                    exec_cmd = line.split('=', 1)[1]
                elif line.startswith('Icon='):
                    icon = line.split('=', 1)[1]
            
            if name and exec_cmd:
                return {
                    'name': name,
                    'exec': exec_cmd,
                    'icon': icon,
                    'path': filepath
                }
        except:
            pass
        return None
    
    def launch_app(self, exec_cmd):
        """Launch application"""
        try:
            # Clean up exec command
            cmd = exec_cmd.split()[0] if exec_cmd else ""
            if cmd:
                subprocess.Popen([cmd], shell=False)
                return True
        except:
            pass
        return False

class SimpleGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.launcher = SimpleApexLauncher()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("🚀 APEX LAUNCHER")
        self.setGeometry(300, 300, 600, 400)
        
        # Main widget
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Search box
        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("🔍 Search applications...")
        self.search_box.textChanged.connect(self.filter_apps)
        layout.addWidget(self.search_box)
        
        # Apps list
        self.apps_list = QListWidget()
        self.apps_list.itemDoubleClicked.connect(self.launch_selected_app)
        layout.addWidget(self.apps_list)
        
        # Load apps
        self.load_apps()
        
        # Style
        self.setStyleSheet("""
            QMainWindow {
                background: #1a1a1a;
                color: white;
            }
            QLineEdit {
                padding: 10px;
                border: 2px solid #333;
                border-radius: 5px;
                background: #2a2a2a;
                color: white;
                font-size: 14px;
            }
            QListWidget {
                background: #2a2a2a;
                border: none;
                border-radius: 5px;
            }
            QListWidgetItem {
                padding: 10px;
                border-bottom: 1px solid #333;
            }
            QListWidgetItem:hover {
                background: #0078d4;
            }
        """)
    
    def load_apps(self):
        """Load applications into list"""
        self.apps_list.clear()
        for app in self.launcher.apps:
            item = QListWidgetItem(f"🚀 {app['name']}")
            item.setData(Qt.UserRole, app)
            self.apps_list.addItem(item)
    
    def filter_apps(self):
        """Filter applications based on search"""
        search_text = self.search_box.text().lower()
        for i in range(self.apps_list.count()):
            item = self.apps_list.item(i)
            app = item.data(Qt.UserRole)
            visible = search_text in app['name'].lower()
            item.setHidden(not visible)
    
    def launch_selected_app(self, item):
        """Launch selected application"""
        app = item.data(Qt.UserRole)
        if self.launcher.launch_app(app['exec']):
            self.close()

def run_terminal_version():
    """Terminal version when PyQt5 is not available"""
    launcher = SimpleApexLauncher()
    
    print("🚀 APEX LAUNCHER - Terminal Mode")
    print("=" * 40)
    
    while True:
        print(f"\nFound {len(launcher.apps)} applications:")
        
        # Show apps with numbers
        for i, app in enumerate(launcher.apps[:20], 1):  # Show first 20
            print(f"{i:2d}. {app['name']}")
        
        if len(launcher.apps) > 20:
            print(f"... and {len(launcher.apps) - 20} more")
        
        print("\nOptions:")
        print("- Enter number to launch app")
        print("- Type 's' to search")
        print("- Type 'q' to quit")
        
        choice = input("\n🚀 Your choice: ").strip()
        
        if choice.lower() == 'q':
            break
        elif choice.lower() == 's':
            search = input("🔍 Search: ").lower()
            filtered = [app for app in launcher.apps if search in app['name'].lower()]
            
            if filtered:
                print(f"\nSearch results for '{search}':")
                for i, app in enumerate(filtered[:10], 1):
                    print(f"{i:2d}. {app['name']}")
                
                try:
                    num = int(input("\nLaunch number: ")) - 1
                    if 0 <= num < len(filtered):
                        if launcher.launch_app(filtered[num]['exec']):
                            print(f"✅ Launched: {filtered[num]['name']}")
                        else:
                            print("❌ Failed to launch")
                    else:
                        print("❌ Invalid number")
                except ValueError:
                    print("❌ Invalid input")
            else:
                print("❌ No apps found")
        else:
            try:
                num = int(choice) - 1
                if 0 <= num < len(launcher.apps):
                    if launcher.launch_app(launcher.apps[num]['exec']):
                        print(f"✅ Launched: {launcher.apps[num]['name']}")
                        break
                    else:
                        print("❌ Failed to launch")
                else:
                    print("❌ Invalid number")
            except ValueError:
                print("❌ Invalid input")

def main():
    """Main function"""
    if PYQT_AVAILABLE:
        app = QApplication(sys.argv)
        window = SimpleGUI()
        window.show()
        sys.exit(app.exec_())
    else:
        print("⚠️  PyQt5 not found, running in terminal mode")
        print("💡 Install PyQt5 for GUI: sudo apt install python3-pyqt5")
        run_terminal_version()

if __name__ == "__main__":
    main()
