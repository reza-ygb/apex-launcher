#!/usr/bin/env python3
"""
🚀 Enhanced Bulletproof Launcher - Quick Setup & Test Script
💪 Quickly set up and test the enhanced launcher functionality

This script will:
✅ Install required Python packages
🎨 Generate test icons
🔍 Scan for applications  
🚀 Launch the enhanced interface
"""

import sys
import subprocess
import os
from pathlib import Path

def print_header():
    print("🚀" + "="*60 + "🚀")
    print("   ENHANCED BULLETPROOF LAUNCHER - QUICK SETUP")
    print("      💪 Testing the Ultimate Power Edition")
    print("🚀" + "="*60 + "🚀")
    print()

def install_packages():
    """Install required Python packages"""
    print("📦 Installing required Python packages...")
    
    packages = [
        'PyQt5>=5.15.0',
        'Pillow>=9.0.0', 
        'requests>=2.28.0'
    ]
    
    for package in packages:
        try:
            print(f"   Installing {package}...")
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', package
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"   ✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"   ❌ Failed to install {package}")
            return False
    
    print("✅ All packages installed successfully!\n")
    return True

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        from PyQt5.QtWidgets import QApplication
        print("   ✅ PyQt5 import successful")
    except ImportError as e:
        print(f"   ❌ PyQt5 import failed: {e}")
        return False
    
    try:
        from PIL import Image
        print("   ✅ Pillow import successful")
    except ImportError as e:
        print(f"   ❌ Pillow import failed: {e}")
        return False
    
    try:
        import requests
        print("   ✅ Requests import successful")
    except ImportError as e:
        print(f"   ❌ Requests import failed: {e}")
        return False
    
    print("✅ All imports successful!\n")
    return True

def create_test_directories():
    """Create necessary directories for testing"""
    print("📁 Creating test directories...")
    
    cache_dir = Path.home() / '.cache' / 'bulletproof-launcher' / 'icons'
    cache_dir.mkdir(parents=True, exist_ok=True)
    print(f"   ✅ Created: {cache_dir}")
    
    print("✅ Directories created successfully!\n")

def test_icon_generation():
    """Test the icon generation system"""
    print("🎨 Testing icon generation...")
    
    try:
        # Import the icon generator
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from enhanced_bulletproof_launcher import IconGenerator
        
        # Create icon generator
        icon_gen = IconGenerator()
        
        # Test icon generation for different categories
        test_apps = [
            ('Firefox', 'Internet'),
            ('VS Code', 'Programming'), 
            ('Terminal', 'System'),
            ('VLC Player', 'Media'),
            ('GIMP', 'Graphics')
        ]
        
        for app_name, category in test_apps:
            icon_path = icon_gen.generate_icon(app_name, category, 'desktop', size=64)
            if icon_path and os.path.exists(icon_path):
                print(f"   ✅ Generated icon for {app_name}")
            else:
                print(f"   ❌ Failed to generate icon for {app_name}")
        
        print("✅ Icon generation test completed!\n")
        return True
        
    except Exception as e:
        print(f"   ❌ Icon generation test failed: {e}\n")
        return False

def test_app_detection():
    """Test the application detection system"""
    print("🔍 Testing application detection...")
    
    try:
        from enhanced_bulletproof_launcher import AdvancedApplicationDetector
        
        # Create detector
        detector = AdvancedApplicationDetector()
        
        # Run detection
        print("   Scanning for applications...")
        apps = detector.detect_applications(force_refresh=True)
        
        # Show results
        total_apps = sum(len(app_list) for app_list in apps.values())
        print(f"   ✅ Found {total_apps} applications")
        
        # Show category breakdown
        for category, app_list in apps.items():
            if app_list:
                print(f"   📂 {category}: {len(app_list)} apps")
        
        print("✅ Application detection test completed!\n")
        return True
        
    except Exception as e:
        print(f"   ❌ Application detection test failed: {e}\n")
        return False

def launch_enhanced_launcher():
    """Launch the enhanced launcher"""
    print("🚀 Launching Enhanced Bulletproof Launcher...")
    
    try:
        launcher_path = Path(__file__).parent / 'enhanced_bulletproof_launcher.py'
        if launcher_path.exists():
            print("   Starting the ultimate launcher experience...")
            subprocess.Popen([sys.executable, str(launcher_path)])
            print("✅ Enhanced launcher started successfully!")
            return True
        else:
            print(f"   ❌ Launcher file not found: {launcher_path}")
            return False
    except Exception as e:
        print(f"   ❌ Failed to launch: {e}")
        return False

def main():
    """Main setup and test function"""
    print_header()
    
    # Check Python version
    if sys.version_info < (3, 7):
        print("❌ Python 3.7+ required. Current version:", sys.version)
        return False
    
    print(f"✅ Python {sys.version.split()[0]} detected\n")
    
    # Run all tests
    steps = [
        ("Installing packages", install_packages),
        ("Testing imports", test_imports), 
        ("Creating directories", create_test_directories),
        ("Testing icon generation", test_icon_generation),
        ("Testing app detection", test_app_detection)
    ]
    
    for step_name, step_func in steps:
        if not step_func():
            print(f"❌ Setup failed at: {step_name}")
            return False
    
    # Ask if user wants to launch
    print("🎯 Setup completed successfully!")
    launch_choice = input("Do you want to launch the Enhanced Bulletproof Launcher now? [Y/n]: ")
    
    if launch_choice.lower() not in ['n', 'no']:
        launch_enhanced_launcher()
    
    print("\n🌟 Setup complete! You can now run:")
    print("   python3 enhanced_bulletproof_launcher.py")
    print("\n💪 Enjoy the Ultimate Launcher Experience!")

if __name__ == "__main__":
    main()
