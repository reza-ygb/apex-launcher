# 🚀 APEX Launcher - Ultimate Linux Application Launcher

<div align="center">

![APEX Launcher](apex-launcher.png)

**⚡ The Fastest, Lightest, Most Reliable Application Launcher for Linux ⚡**

[![Release](https://img.shields.io/github/v/release/reza-ygb/apex-launcher)](https://github.com/reza-ygb/apex-launcher/releases)
[![License](https://img.shields.io/github/license/reza-ygb/apex-launcher)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)

</div>

---

## ✨ Features

🔥 **Ultra-Fast Scanning** - Finds all your apps in seconds  
🎯 **Smart Categories** - Auto-organizes by type (Programming, Security, Games, etc.)  
💻 **GUI + CLI** - Beautiful desktop interface with terminal fallback  
🛡️ **Crash-Proof** - Never breaks, even with 10,000+ applications  
⚡ **Lightning Speed** - Optimized for minimal RAM usage (50MB)  
� **Docker Ready** - Works in containers and minimal environments  
� **Universal** - Supports .desktop, Snap, Flatpak, AppImage, CLI tools  

---

## 🚀 Quick Install

### One-Line Install (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/install.sh | bash
```

### Manual Install
```bash
git clone https://github.com/reza-ygb/apex-launcher.git
cd apex-launcher
chmod +x install.sh
./install.sh
```

### Docker
```bash
# GUI in Docker (with X11 forwarding)
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /usr/share/applications:/usr/share/applications:ro \
  ghcr.io/reza-ygb/apex-launcher:latest

# CLI-only in Docker  
docker run --rm -it ghcr.io/reza-ygb/apex-launcher:latest --cli
```

---

## � Package Installation

### Ubuntu/Debian (.deb)
```bash
wget https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.deb
sudo dpkg -i apex-launcher.deb
sudo apt-get install -f  # Fix dependencies if needed
```

### Arch Linux (AUR)
```bash
yay -S apex-launcher-bin
# OR
paru -S apex-launcher-bin
# OR manual:
git clone https://aur.archlinux.org/apex-launcher-bin.git
cd apex-launcher-bin && makepkg -si
```

### Fedora/CentOS/RHEL (.rpm)
```bash
wget https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.rpm
sudo rpm -i apex-launcher.rpm
# OR with dnf
sudo dnf install https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.rpm
```

### Universal AppImage
```bash
wget https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.AppImage
chmod +x apex-launcher.AppImage
./apex-launcher.AppImage
```

---

## 🎯 Usage

### GUI Mode (Default)
```bash
apex-launcher
```

### CLI Mode
```bash
apex-launcher --cli
```

### Keyboard Shortcuts
- `Ctrl+F` - Focus search box
- `Enter` - Launch selected app  
- `Escape` - Clear search / Go back

---

## ⚙️ Requirements

### Minimal Requirements
- **OS:** Any Linux distribution
- **Python:** 3.6+ (usually pre-installed)
- **RAM:** 50MB minimum
- **Storage:** 10MB

### For GUI Mode
- **PyQt5** (auto-installed with package managers)
- **X11 or Wayland** display server

### For CLI Mode
- **Terminal only** - works everywhere!

---

## 🔧 Advanced Usage

### System-wide Installation
```bash
sudo ./install.sh --system
```

### Custom Installation Path  
```bash
./install.sh --prefix=/opt/apex-launcher
```

### Development Mode
```bash
git clone https://github.com/reza-ygb/apex-launcher.git
cd apex-launcher
python3 apex_launcher.py  # GUI
python3 smart_cli_launcher.py  # CLI
```

---

## � Troubleshooting

### GUI Won't Start
```bash
# Install PyQt5
sudo apt install python3-pyqt5        # Ubuntu/Debian  
sudo pacman -S python-pyqt5          # Arch
sudo dnf install python3-qt5         # Fedora
pip3 install --user PyQt5            # Universal

# Or use CLI mode
apex-launcher --cli
```

### No Applications Found
```bash
# Refresh application database
apex-launcher --refresh
```

### Permission Issues
```bash
# Fix permissions
chmod +x ~/.local/bin/apex-launcher
# Or reinstall
./install.sh --force
```

---

## 🏗️ Architecture

### Supported Application Types
- 🖥️ **Desktop Apps** (.desktop files)
- 📦 **Snap Packages** 
- � **Flatpak Apps**
- 📦 **AppImages**
- ⚡ **CLI Tools** (PATH binaries)

### Smart Categories
- 💻 **Programming** - IDEs, editors, compilers
- � **Security** - Penetration testing, forensics  
- ⚙️ **System** - Admin tools, monitors
- 🌐 **Internet** - Browsers, email, download
- 🎬 **Media** - Video, audio, graphics
- 📄 **Office** - Documents, productivity
- 🎨 **Graphics** - Design, photo editing
- 🎮 **Games** - Entertainment
- 🔧 **Development** - Terminal, SSH, FTP
- 📚 **Education** - Learning tools

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start for Developers
```bash
git clone https://github.com/reza-ygb/apex-launcher.git
cd apex-launcher
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 apex_launcher.py
```