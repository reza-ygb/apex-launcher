#!/usr/bin/env python3
"""
🚀 BULLETPROOF LAUNCHER - UNIVERSAL ENTRY POINT
🎯 Smart launcher that automatically chooses the best interface

This script will:
✅ Auto-detect available dependencies
🚀 Launch the enhanced version if possible
⚡ Fallback to basic version if needed
💪 Always provide a working launcher experience
"""

import sys
import os
import subprocess
from pathlib import Path

def check_dependencies():
    """Check what dependencies are available"""
    deps = {
        'pyqt5': False,
        'pillow': False,
        'requests': False
    }
    
    try:
        from PyQt5.QtWidgets import QApplication
        deps['pyqt5'] = True
    except ImportError:
        pass
    
    try:
        from PIL import Image
        deps['pillow'] = True
    except ImportError:
        pass
    
    try:
        import requests
        deps['requests'] = True
    except ImportError:
        pass
    
    return deps

def install_missing_deps():
    """Attempt to install missing dependencies"""
    print("🔧 Installing missing dependencies...")
    
    packages = ['PyQt5', 'Pillow', 'requests']
    
    for package in packages:
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', package
            ], stdout=subprocess.DEVNULL)
            print(f"✅ Installed {package}")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}")
    
    return check_dependencies()

def launch_enhanced():
    """Launch the enhanced bulletproof launcher"""
    try:
        enhanced_path = Path(__file__).parent / 'enhanced_bulletproof_launcher.py'
        if enhanced_path.exists():
            print("🚀 Launching Enhanced Bulletproof Launcher...")
            from enhanced_bulletproof_launcher import main
            main()
            return True
    except Exception as e:
        print(f"Enhanced launcher failed: {e}")
    return False

def launch_basic():
    """Launch the basic bulletproof launcher"""
    try:
        basic_path = Path(__file__).parent / 'bulletproof_launcher.py'
        if basic_path.exists():
            print("⚡ Launching Basic Bulletproof Launcher...")
            subprocess.run([sys.executable, str(basic_path)])
            return True
    except Exception as e:
        print(f"Basic launcher failed: {e}")
    return False

def launch_cli():
    """Launch the CLI launcher as fallback"""
    try:
        cli_path = Path(__file__).parent / 'smart_cli_launcher.py'
        if cli_path.exists():
            print("📟 Launching CLI Launcher...")
            subprocess.run([sys.executable, str(cli_path)])
            return True
    except Exception as e:
        print(f"CLI launcher failed: {e}")
    return False

def main():
    """Main launcher logic"""
    print("🚀 BULLETPROOF LAUNCHER - Starting Up...")
    print("="*50)
    
    # Check what we have
    deps = check_dependencies()
    
    # Try enhanced launcher if we have all dependencies
    if all(deps.values()):
        print("✅ All dependencies available - Using Enhanced Mode")
        if launch_enhanced():
            return
    
    # Try to install missing dependencies
    elif '--install' in sys.argv or input("Install missing dependencies? [Y/n]: ").lower() not in ['n', 'no']:
        deps = install_missing_deps()
        if all(deps.values()):
            if launch_enhanced():
                return
    
    # Fallback to basic launcher
    if deps['pyqt5']:
        print("⚡ Using Basic GUI Mode")
        if launch_basic():
            return
    
    # Final fallback to CLI
    print("📟 Falling back to CLI Mode")
    if launch_cli():
        return
    
    # If everything fails
    print("❌ Could not launch any interface!")
    print("Try running: python3 enhanced_bulletproof_launcher.py")

if __name__ == "__main__":
    main()
