# 📝 Changelog

All notable changes to APEX Launcher will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Docker support with GUI and CLI modes
- GitHub Actions CI/CD pipeline
- Multi-format package releases (.deb, .rpm, .AppImage)
- Comprehensive documentation (README, CONTRIBUTING)

## [1.0.0] - 2024-01-XX

### 🎉 Initial Release

#### ✨ Features Added
- **Dual Interface**: Beautiful PyQt5 GUI with CLI fallback
- **Universal Compatibility**: Works on all major Linux distributions
- **Smart Categorization**: Automatic app organization into 11 categories
- **Ultra-Fast Scanning**: Finds applications in seconds
- **Multi-Source Support**: .desktop files, Snap, Flatpak, AppImage, CLI tools
- **Lightweight Design**: Minimal RAM usage (~50MB)
- **Crash-Proof Architecture**: Bulletproof error handling
- **Simple Text Icons**: Fast, universal icon system
- **Keyboard Shortcuts**: Ctrl+F for search focus
- **One-Line Installation**: Simple curl-based installer

#### 🏗️ Architecture
- **Main GUI**: `apex_launcher.py` - PyQt5-based interface
- **CLI Mode**: `smart_cli_launcher.py` - Terminal fallback
- **Wrapper Script**: `bin/apex-launcher` - Unified entry point
- **Auto-Detection**: Automatic GUI/CLI mode selection

#### 📦 Application Sources
- Desktop entries (`/usr/share/applications/`, `~/.local/share/applications/`)
- Snap packages (`/snap/bin/`)  
- Flatpak applications (`/var/lib/flatpak/exports/bin/`)
- AppImage files (common locations)
- CLI tools (selected PATH directories)

#### 🎯 Categories
- 💻 **Programming** - Development tools, IDEs, compilers
- 🔒 **Security** - Penetration testing, forensics tools
- ⚙️ **System** - Administration, monitoring utilities
- 🌐 **Internet** - Browsers, network applications
- 🎬 **Media** - Audio, video, graphics software
- 📄 **Office** - Productivity, document tools
- 🎨 **Graphics** - Design, photo editing
- 🎮 **Games** - Gaming applications
- 🔧 **Development** - Terminal, SSH, containers
- 📚 **Education** - Learning applications
- 📁 **Other** - Uncategorized applications

#### 🔧 Installation Methods
- **One-line script**: `curl | bash` installer
- **Manual**: Git clone and `./install.sh`
- **Package managers**: .deb, .rpm, .AppImage, AUR
- **Docker**: Container support

#### 📦 Package Availability
- **Debian/Ubuntu**: `.deb` package
- **Fedora/RHEL**: `.rpm` package  
- **Arch Linux**: AUR package (`apex-launcher-bin`)
- **Universal**: `.AppImage` for any distro
- **Docker**: `ghcr.io/reza-ygb/apex-launcher`

#### ⚡ Performance Features
- **Fast Startup**: ~2 second launch time
- **Efficient Scanning**: Parallel processing
- **Memory Optimized**: Minimal resource usage
- **Simple Icons**: Text-based, no complex generation
- **Direct Launch**: No external dependencies

#### 🛡️ Reliability Features
- **Exception Handling**: Comprehensive error catching
- **Graceful Degradation**: GUI→CLI fallback
- **Safe Parsing**: Robust .desktop file handling
- **No Crashes**: Defensive programming throughout

#### 🎨 User Interface
- **Clean Design**: Minimal, focused interface
- **Category Sidebar**: Easy navigation
- **Search Box**: Instant filtering
- **Simple Icons**: Fast, colorful text-based icons
- **Responsive**: Smooth user experience

### 🔄 Migration from Complex Version
- **Removed**: Heavy features causing instability
- **Removed**: RapidFuzz dependency (fuzzy search)
- **Removed**: Complex icon generation system
- **Removed**: Usage tracking and favorites
- **Removed**: Multiple stylesheets and animations
- **Simplified**: Core functionality for speed and reliability

### 🐛 Bug Fixes
- Fixed GUI crashes on category selection
- Resolved memory leaks in scanning process  
- Improved error handling for missing dependencies
- Fixed permission issues with launcher script

### 📋 Technical Details
- **Python**: 3.6+ compatibility
- **GUI Framework**: PyQt5 with fallback detection  
- **Dependencies**: Minimal (PyQt5 + Pillow, both optional)
- **Platform**: All Linux distributions
- **Size**: ~10MB installed, ~50MB RAM usage

### 🙏 Acknowledgments
- Python and PyQt5 communities
- Linux desktop standards (freedesktop.org)
- All contributors and testers

---

## Release Notes Format

### Added
- New features

### Changed  
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Features removed in this version

### Fixed
- Bug fixes

### Security
- Security improvements

---

**For detailed commit history, see [GitHub Commits](https://github.com/reza-ygb/apex-launcher/commits/main)**