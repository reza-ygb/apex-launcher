# 🚀 APEX LAUNCHER - The Ultimate Linux Application Launcher

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Linux-orange.svg)](https://github.com/reza-ygb/apex-launcher)
[![PyQt5](https://img.shields.io/badge/GUI-PyQt5-red.svg)](https://pypi.org/project/PyQt5/)
[![Stars](https://img.shields.io/github/stars/reza-ygb/apex-launcher?style=social)](https://github.com/reza-ygb/apex-launcher/stargazers)

> **The most powerful, beautiful, and intelligent application launcher for Linux systems. One-line installation, 6000+ app detection, automatic icon generation, and universal compatibility.**

## ⚡ **Quick Start**

**Install with one command:**
```bash
curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/apex_install.sh | bash
```

**Launch:**
```bash
apex-launcher
```

**Done!** 🎉 Start organizing your 6000+ applications instantly.

## ✨ Why APEX LAUNCHER?

APEX LAUNCHER is the **ultimate evolution** of Linux application launchers, designed to handle **6000+ applications** with automatic categorization, beautiful modern GUI, and bulletproof crash protection.

### 🔥 **KEY FEATURES**

- **🎯 UNIVERSAL COMPATIBILITY**: Works on ALL Linux distributions
- **⚡ ONE-LINE INSTALLATION**: No complex setup required
- **🎨 AUTOMATIC ICON GENERATION**: Beautiful icons for every application
- **🧠 SMART CATEGORIZATION**: AI-powered app organization
- **🛡️ BULLETPROOF STABILITY**: Never crashes, always works
- **🚀 ULTRA-FAST PERFORMANCE**: SQLite caching, optimized scanning
- **💎 MODERN GLASSMORPHISM UI**: Beautiful, responsive interface
- **🔍 ADVANCED SEARCH**: Find any app instantly
- **📦 MULTI-FORMAT SUPPORT**: Desktop apps, CLI tools, Snap, Flatpak, AppImage
- 🌟 **Never see blank icons again!**

### 🚀 **Ultra-Fast Organization**
- 📊 **Handles 6000+ applications** without breaking a sweat
- ⚡ **Lightning-fast search** across all your apps
- 🧠 **Intelligent categorization** using advanced algorithms
- 📱 **Multi-source detection**: Desktop, CLI, Snap, Flatpak, AppImage

### 🎯 **Perfect for Arch & Ubuntu**
- 🏗️ **One-click installation** with automatic dependency resolution
- 🔧 **Optimized for both distributions** 
- 📦 **Supports all package managers**: pacman, apt, snap, flatpak
- ⚙️ **Auto-configures desktop integration**

---

## 🌟 Features

### 🎨 **Visual Excellence**
- **Modern Material Design UI** with glassmorphism effects
- **Real-time icon generation** with category-based color schemes
- **Smooth animations** and hover effects
- **Dark/Light theme adaptation**

### 🔍 **Smart Search & Organization**
- **Fuzzy search** finds apps even with typos
- **Category-based filtering** with 11 intelligent categories
- **Usage statistics** and frequently used apps
- **Keyboard shortcuts** for power users

### 📦 **Universal Compatibility**
- **Desktop Applications** (.desktop files)
- **Command Line Tools** (PATH executables)  
- **Snap Packages** (snap list integration)
- **Flatpak Applications** (flatpak list integration)
- **AppImage Files** (automatic detection)

### ⚡ **Performance Optimized**
- **SQLite caching** for instant startup
- **Multi-threaded scanning** for speed
- **Memory efficient** icon generation
- **Background updates** without UI blocking

---

## 🚀 **ONE-LINE INSTALLATION**

Install APEX LAUNCHER on any Linux distribution with a single command:

```bash
curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/apex_install.sh | bash
```

That's it! The installer will:
- ✅ **Auto-detect** your Linux distribution  
- ✅ **Install dependencies** (Python, PyQt5, Pillow)
- ✅ **Set up desktop integration** 
- ✅ **Create launcher commands**
- ✅ **Ready to use immediately**

### 📦 **What Gets Installed:**
- **Main launcher**: `/usr/local/share/apex-launcher/apex_launcher.py`
- **Command alias**: `apex-launcher` (works from anywhere)
- **Desktop entry**: Available in applications menu
- **Icon cache**: `~/.cache/apex-launcher/`
- **Configuration**: `~/.config/apex-launcher/`

### 🔄 **Supported Distributions:**
The installer works on **ALL** major Linux distributions:
- **Ubuntu/Debian** → `apt install`
- **Arch/Manjaro** → `pacman -S`
- **Fedora/RHEL** → `dnf install`
- **openSUSE** → `zypper install`
- **Alpine** → `apk add`
- **Others** → Falls back to `pip3 install`

### Alternative: Manual Installation
```bash
git clone https://github.com/reza-ygb/apex-launcher.git
cd apex-launcher
chmod +x apex_install.sh
./apex_install.sh
```

---

## 🎯 **HOW TO USE**

After installation, launch APEX LAUNCHER in multiple ways:

### 🖥️ **From Applications Menu**
- Look for **"APEX Launcher"** in your system menu
- Usually found under **"Utilities"** or **"System Tools"**

### ⌨️ **From Terminal** 
```bash
# Simple command
apex-launcher

# Or run directly
python3 apex_launcher.py
```

### � **Quick Launch Tips**
- **Search**: Press `Ctrl+F` or just start typing
- **Categories**: Click categories on the left sidebar  
- **Refresh**: Press `F5` to rescan applications
- **Keyboard Navigation**: Use arrow keys and Enter

### ⌨️ **Keyboard Shortcuts**
- `Ctrl+F` or `/` - Focus search box
- `F5` or `Ctrl+R` - Refresh application list
- `Ctrl+1-9` - Quick category switching
- `Esc` - Clear search / Go back

### 🔍 **Search Tips**
- **Fuzzy search**: Type "fire" to find "Firefox"
- **Category search**: Use "game:" to see only games
- **Type search**: Use "snap:" to see only snap packages
- **Command search**: Search by executable name

---

## 📊 **Application Categories**

The launcher intelligently categorizes applications into:

| Category | Icon | Description | Examples |
|----------|------|-------------|----------|
| **Programming** | 💻 | Development tools & IDEs | VS Code, Python, Git |
| **Security** | � | Security & hacking tools | Wireshark, Nmap, Burp |
| **System** | ⚙️ | System utilities | htop, systemctl, mount |
| **Internet** | 🌐 | Browsers & network apps | Firefox, Chrome, wget |
| **Media** | 🎬 | Audio/video applications | VLC, Spotify, GIMP |
| **Office** | 📄 | Office & productivity | LibreOffice, PDF readers |
| **Graphics** | 🎨 | Design & photo editing | GIMP, Inkscape, Blender |
| **Games** | 🎮 | Gaming applications | Steam, Lutris, emulators |
| **Development** | � | Terminal & dev tools | Terminal, SSH, Docker |
| **Education** | 📚 | Learning applications | Educational software |
| **Other** | 📁 | Uncategorized apps | Everything else |

---

## 🎨 **Icon Generation System**

### 🌈 **Smart Color Coding**
Each category has its own color scheme:
- **Programming**: Green gradient (Nature/Growth)
- **Security**: Red gradient (Alert/Protection) 
- **System**: Orange gradient (Power/Energy)
- **Internet**: Blue gradient (Trust/Communication)
- **Media**: Purple gradient (Creativity/Entertainment)
- **Office**: Gray gradient (Professional/Business)
- **Graphics**: Pink gradient (Artistic/Creative)
- **Games**: Indigo gradient (Fun/Entertainment)

### 🎯 **Application-Specific Icons**
The system recognizes popular applications and assigns custom symbols:
- Firefox → 🔥, Chrome → 🌎, VS Code → 💻
- Terminal → ⚡, File Manager → 📁, GIMP → 🎨
- VLC → ▶️, Spotify → 🎵, Steam → 🎮
- And many more...

---

## ⚙️ **Configuration**

### 📁 **File Locations**
- **Icons Cache**: `~/.cache/apex-launcher/icons/`
- **Database**: `~/.cache/apex-launcher/apps.db`
- **Desktop Entry**: `~/.local/share/applications/apex-launcher.desktop`
- **Launcher Script**: `~/.local/bin/apex-launcher`

### 🔧 **Customization**
You can customize the launcher by editing the configuration in the source code:
- **Categories**: Modify `AdvancedApplicationDetector.categories`
- **Icon Colors**: Edit `IconGenerator.category_icons`
- **App-Specific Icons**: Update `IconGenerator.app_specific_icons`

---

## 🛠️ **Advanced Features**

### 📊 **Statistics & Analytics** 
- **Usage tracking** for most-used applications
- **Category distribution** analysis
- **Launch frequency** statistics
- **Performance metrics**

### 🚀 **Performance Optimizations**
- **SQLite caching** for instant subsequent launches
- **Icon caching** to avoid regeneration  
- **Multi-threaded scanning** for large application lists
- **Memory-efficient** image processing

### 🔄 **Auto-Update System**
- **Background scanning** for new applications
- **Smart cache invalidation** 
- **Incremental updates** instead of full rescans
- **Change detection** for modified applications

---

## 🐛 **Troubleshooting**

### ❌ **Common Issues**

#### **"No applications found"**
```bash
# Force refresh the application database
python3 apex_launcher.py --force-refresh

# Or clear cache and rescan
rm -rf ~/.cache/apex-launcher/
python3 apex_launcher.py
```

#### **"Icons not generating"** 
```bash
# Check Pillow installation
python3 -c "from PIL import Image; print('Pillow OK')"

# Install missing fonts
sudo apt install fonts-dejavu fonts-liberation  # Ubuntu
sudo pacman -S ttf-dejavu ttf-liberation        # Arch
```

#### **"PyQt5 import error"**
```bash
# Ubuntu/Debian
sudo apt install python3-pyqt5

# Arch Linux  
sudo pacman -S python-pyqt5

# Or via pip
pip3 install PyQt5
```

### 🔍 **Debug Mode**
```bash
# Run with verbose output
python3 apex_launcher.py --debug

# Check application detection
python3 -c "
from apex_launcher import AdvancedApplicationDetector
detector = AdvancedApplicationDetector()
apps = detector.detect_applications(force_refresh=True)
print(f'Found {sum(len(v) for v in apps.values())} total applications')
"
```

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

### 🐛 **Bug Reports**
- Use the [GitHub Issues](https://github.com/reza-ygb/apex-launcher/issues) page
- Include your distribution, Python version, and error messages
- Provide steps to reproduce the issue

### 💡 **Feature Requests**  
- Suggest new features via GitHub Issues
- Explain the use case and benefit
- Consider contributing code if possible

### 🔧 **Code Contributions**
1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

### 📝 **Documentation**
- Improve this README
- Add code comments
- Create tutorials or guides

---

## 📋 **System Requirements**

### **Minimum Requirements**
- **Python**: 3.7+
- **RAM**: 512MB available
- **Storage**: 100MB for cache and icons
- **Desktop Environment**: Any Linux DE with .desktop support

### **Recommended Setup**
- **Python**: 3.9+
- **RAM**: 2GB available  
- **Storage**: 500MB for extensive icon cache
- **Desktop Environment**: GNOME, KDE, XFCE, or similar

### **Supported Distributions**
- ✅ **Arch Linux** (+ derivatives like Manjaro, EndeavourOS)
- ✅ **Ubuntu** (+ derivatives like Linux Mint, Pop!_OS) 
- ✅ **Fedora** (+ derivatives like Nobara)
- ✅ **openSUSE** (Leap & Tumbleweed)
- ✅ **Debian** (Stable, Testing, Unstable)
- ✅ Most other Linux distributions with minor modifications

---

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **PyQt5** team for the excellent GUI framework
- **Pillow** team for image processing capabilities  
- **Linux Desktop** community for .desktop file standards
- **Material Design** for UI/UX inspiration
- **All contributors** who helped improve this project

---

## 🌟 **Star the Project**

If you find this launcher useful, please ⭐ star the repository on GitHub!
It helps other users discover this tool and motivates further development.

---

**💪 Experience the Ultimate in Application Management with APEX LAUNCHER! 🚀**

Made with ❤️ for the Linux community