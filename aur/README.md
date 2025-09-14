# 📦 APEX Launcher - AUR Package

This directory contains the AUR (Arch User Repository) package files for APEX Launcher.

## Files

- **PKGBUILD** - Main package build script
- **.SRCINFO** - Package metadata (auto-generated)
- **apex-launcher.install** - Post-install/remove scripts
- **test-aur.sh** - Testing script for package validation

## Installation on Arch Linux

### Using AUR Helper (Recommended)
```bash
yay -S apex-launcher-bin
# or
paru -S apex-launcher-bin
```

### Manual Installation
```bash
git clone https://aur.archlinux.org/apex-launcher-bin.git
cd apex-launcher-bin
makepkg -si
```

## Building from Source

If you want to build the package yourself:

1. **Clone this repository**:
   ```bash
   git clone https://github.com/reza-ygb/apex-launcher.git
   cd apex-launcher/aur
   ```

2. **Test the package** (optional):
   ```bash
   ./test-aur.sh
   ```

3. **Build the package**:
   ```bash
   makepkg -si
   ```

## Package Information

- **Package Name**: `apex-launcher-bin`
- **Version**: 1.0.0
- **Architecture**: `any`
- **License**: MIT

### Dependencies
- `python` - Python runtime
- `python-pyqt5` - GUI framework
- `python-pillow` - Image processing

### Optional Dependencies
- `python-pyqt5` - GUI mode support (falls back to CLI if missing)
- `python-pillow` - Enhanced icon support (uses text icons if missing)

## Package Details

This package installs:

- `/usr/bin/apex-launcher` - Main launcher script
- `/usr/share/apex-launcher/` - Application files
- `/usr/share/applications/apex-launcher.desktop` - Desktop entry
- `/usr/share/pixmaps/apex-launcher.png` - Application icon
- `/usr/share/licenses/apex-launcher-bin/LICENSE` - License file

## Usage After Installation

```bash
# GUI mode (default)
apex-launcher

# CLI mode (terminal)
apex-launcher --cli
```

## Updating

To update to a newer version:

```bash
yay -S apex-launcher-bin  # Will update if new version available
```

## Uninstalling

```bash
sudo pacman -R apex-launcher-bin
```

Note: Configuration files in `~/.cache/apex-launcher/` are preserved and can be manually removed if desired.

## Troubleshooting

### GUI Mode Not Working
```bash
# Install PyQt5 if missing
sudo pacman -S python-pyqt5

# Use CLI mode as fallback
apex-launcher --cli
```

### Permission Issues
```bash
# Check if launcher is executable
ls -la /usr/bin/apex-launcher

# Reinstall if needed
yay -S apex-launcher-bin --overwrite '*'
```

## Contributing

If you find issues with the AUR package:

1. Check the [main repository](https://github.com/reza-ygb/apex-launcher) first
2. Report AUR-specific issues on the AUR package page
3. Submit improvements via pull requests

## Maintainer

- **reza-ygb** <reza-ygb@users.noreply.github.com>

---

**Made with ❤️ for the Arch Linux community**