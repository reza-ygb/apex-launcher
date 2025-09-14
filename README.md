# 🚀 APEX Launcher - Ultimate Linux Application Launcher

<div align="center">

![APEX Launcher](apex-launcher.png)

**⚡ The Fastest, Lightest, Most Reliable Application Launcher for Linux ⚡**

[![Release](https://img.shields.io/github/v/release/reza-ygb/apex-launcher)](https://github.com/reza-ygb/apex-launcher/releases)
[![License](https://img.shields.io/github/license/reza-ygb/apex-launcher)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)

</div>

<div align="center" style="margin: 16px 0;">

<h3>📦 Quick Downloads</h3>

<a href="https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.deb">
  <img alt="Download .deb" src="https://img.shields.io/badge/Download-.deb-blue?logo=debian&logoColor=white&style=for-the-badge" />
 </a>
<a href="https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.rpm">
  <img alt="Download .rpm" src="https://img.shields.io/badge/Download-.rpm-294172?logo=fedora&logoColor=white&style=for-the-badge" />
 </a>
<a href="https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.AppImage">
  <img alt="Download AppImage" src="https://img.shields.io/badge/Download-AppImage-000000?logo=appimage&logoColor=white&style=for-the-badge" />
 </a>
<a href="https://aur.archlinux.org/packages/apex-launcher-bin">
  <img alt="AUR" src="https://img.shields.io/badge/AUR-apex--launcher--bin-1793D1?logo=archlinux&logoColor=white&style=for-the-badge" />
 </a>
<a href="https://github.com/reza-ygb/apex-launcher/pkgs/container/apex-launcher">
  <img alt="Docker" src="https://img.shields.io/badge/Docker-ghcr.io%2Freza--ygb%2Fapex--launcher-2496ED?logo=docker&logoColor=white&style=for-the-badge" />
 </a>

<p>

```bash
# Arch (AUR)
yay -S apex-launcher-bin

# Ubuntu/Debian (.deb)
wget -q https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.deb \
  && sudo dpkg -i apex-launcher.deb || sudo apt -f install

# Fedora/RHEL (.rpm)
sudo dnf install -y https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.rpm

# AppImage (any distro)
wget -q https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.AppImage \
  && chmod +x apex-launcher.AppImage && ./apex-launcher.AppImage

# Docker
docker pull ghcr.io/reza-ygb/apex-launcher:latest
```

</p>

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

## 🚀 Features

- **Lightweight**: Minimal memory footprint (<50MB RAM usage)
- **Fast Search**: Real-time application filtering as you type
- **Multi-Mode**: Both GUI and CLI interfaces
- **Universal**: Works on all major Linux distributions
- **Container Ready**: Docker support for CLI and GUI modes
- **No Dependencies**: Falls back gracefully when GUI libraries unavailable
- **Professional**: Production-ready with automated testing and packaging

## 💾 Installation

### One-Line Install (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/install.sh | bash
```

### Download Packages
| Package | Best For | Download |
|---------|----------|----------|
| **.deb** | Ubuntu, Debian, Mint | [📥 Download](https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.deb) |
| **.rpm** | Fedora, CentOS, RHEL | [📥 Download](https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.rpm) |
| **.AppImage** | Any Linux distro | [📥 Download](https://github.com/reza-ygb/apex-launcher/releases/latest/download/apex-launcher.AppImage) |
| **AUR** | Arch Linux | `yay -S apex-launcher-bin` |
| **Docker** | Containers | `docker pull ghcr.io/reza-ygb/apex-launcher:latest` |

### Manual Install
```bash
git clone https://github.com/reza-ygb/apex-launcher.git
cd apex-launcher
pip install -r requirements.txt
python3 apex_launcher.py
```

### Testing
```bash
# Run tests
./test.sh

# Test in Docker
docker-compose up test

# Test AUR package
cd aur && ./test-aur.sh
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for the Linux community
- Optimized for minimal resource usage
- Professional packaging and CI/CD

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

### Docker
```bash
# CLI mode (recommended for containers)
docker run --rm -it ghcr.io/reza-ygb/apex-launcher:latest --cli

# GUI mode (Linux with X11 forwarding)
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /usr/share/applications:/usr/share/applications:ro \
  ghcr.io/reza-ygb/apex-launcher:latest
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

## � Usage

### GUI Mode
Simply run `apex-launcher` or click the desktop icon. The GUI will:
- Automatically scan for installed applications
- Provide real-time search as you type
- Launch applications with a single click
- Display applications organized by categories

### CLI Mode
Run `apex-launcher --cli` or `smart_cli_launcher.py` for terminal interface:
```bash
apex-launcher --cli
# or
python3 smart_cli_launcher.py
```

The CLI provides a numbered menu system for easy navigation.

### Docker Usage
```bash
# Quick CLI launch
docker run --rm -it ghcr.io/reza-ygb/apex-launcher:latest --cli

# GUI mode (Linux desktop)
docker run --rm -it \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v /usr/share/applications:/usr/share/applications:ro \
  ghcr.io/reza-ygb/apex-launcher:latest
```

## 🔧 Development

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