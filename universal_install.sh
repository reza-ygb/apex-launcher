#!/bin/bash
"""
🚀 ENHANCED BULLETPROOF LAUNCHER - ONE-LINE INSTALLER
💪 Works on ALL Linux distributions with ONE command!
🎯 Universal installer for maximum compatibility

Just run: curl -sL https://raw.githubusercontent.com/yourusername/enhanced-bulletproof-launcher/main/install.sh | bash
"""

set -e  # Exit on any error

# Colors for beautiful output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Emojis
ROCKET="🚀"
GEAR="⚙️"
CHECK="✅"
CROSS="❌"
STAR="⭐"
FIRE="🔥"
DIAMOND="💎"

print_header() {
    clear
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${WHITE}                🚀 ENHANCED BULLETPROOF LAUNCHER                   ${BLUE}║${NC}"
    echo -e "${BLUE}║${WHITE}                      💪 ONE-LINE INSTALLER                        ${BLUE}║${NC}"
    echo -e "${BLUE}║${WHITE}                    Works on ALL Linux Systems!                   ${BLUE}║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${CYAN}${GEAR} Installing Enhanced Bulletproof Launcher...${NC}"
    echo ""
}

print_step() {
    echo -e "${CYAN}${GEAR} $1${NC}"
}

print_success() {
    echo -e "${GREEN}${CHECK} $1${NC}"
}

print_error() {
    echo -e "${RED}${CROSS} $1${NC}"
}

print_info() {
    echo -e "${YELLOW}${STAR} $1${NC}"
}

# Detect distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
        VERSION=$VERSION_ID
    elif command -v lsb_release &> /dev/null; then
        DISTRO=$(lsb_release -si | tr '[:upper:]' '[:lower:]')
    else
        DISTRO="unknown"
    fi
    
    print_info "Detected: $DISTRO"
}

# Install Python and dependencies based on distro
install_dependencies() {
    print_step "Installing dependencies for $DISTRO..."
    
    case $DISTRO in
        "arch"|"manjaro"|"endeavouros")
            sudo pacman -Syu --noconfirm
            sudo pacman -S --noconfirm python python-pip python-pyqt5 python-pillow git wget curl
            ;;
        "ubuntu"|"debian"|"linuxmint"|"pop"|"elementary"|"zorin")
            sudo apt update
            sudo apt install -y python3 python3-pip python3-pyqt5 python3-pil git wget curl
            # Install pip packages if system packages don't work
            pip3 install --user PyQt5 Pillow requests 2>/dev/null || true
            ;;
        "fedora"|"centos"|"rhel"|"rocky"|"almalinux")
            sudo dnf update -y
            sudo dnf install -y python3 python3-pip python3-qt5 python3-pillow git wget curl
            pip3 install --user PyQt5 Pillow requests 2>/dev/null || true
            ;;
        "opensuse"|"suse")
            sudo zypper refresh
            sudo zypper install -y python3 python3-pip python3-qt5 python3-Pillow git wget curl
            pip3 install --user PyQt5 Pillow requests 2>/dev/null || true
            ;;
        "alpine")
            sudo apk update
            sudo apk add python3 py3-pip py3-qt5 py3-pillow git wget curl
            pip3 install --user PyQt5 Pillow requests 2>/dev/null || true
            ;;
        *)
            # Universal fallback
            print_info "Unknown distro, trying universal method..."
            # Try to install python3 and pip
            if command -v apt &> /dev/null; then
                sudo apt update && sudo apt install -y python3 python3-pip git wget curl
            elif command -v yum &> /dev/null; then
                sudo yum install -y python3 python3-pip git wget curl
            elif command -v dnf &> /dev/null; then
                sudo dnf install -y python3 python3-pip git wget curl
            elif command -v pacman &> /dev/null; then
                sudo pacman -S --noconfirm python python-pip git wget curl
            elif command -v zypper &> /dev/null; then
                sudo zypper install -y python3 python3-pip git wget curl
            elif command -v apk &> /dev/null; then
                sudo apk add python3 py3-pip git wget curl
            fi
            
            # Install Python packages via pip
            pip3 install --user PyQt5 Pillow requests
            ;;
    esac
    
    print_success "Dependencies installed!"
}

# Create installation directory
setup_directory() {
    print_step "Setting up installation directory..."
    
    INSTALL_DIR="$HOME/.local/share/enhanced-bulletproof-launcher"
    mkdir -p "$INSTALL_DIR"
    cd "$INSTALL_DIR"
    
    print_success "Directory created: $INSTALL_DIR"
}

# Download the launcher
download_launcher() {
    print_step "Downloading Enhanced Bulletproof Launcher..."
    
    # Download main launcher file
    wget -q "https://raw.githubusercontent.com/yourusername/enhanced-bulletproof-launcher/main/enhanced_bulletproof_launcher.py" -O enhanced_bulletproof_launcher.py
    
    # Download icon
    wget -q "https://raw.githubusercontent.com/yourusername/enhanced-bulletproof-launcher/main/bulletproof_launcher_icon_64.png" -O bulletproof_launcher_icon_64.png 2>/dev/null || {
        # Create a simple icon if download fails
        python3 -c "
from PIL import Image, ImageDraw
img = Image.new('RGBA', (64, 64), (52, 152, 219, 255))
draw = ImageDraw.Draw(img)
draw.text((20, 20), '🚀', fill=(255, 255, 255, 255))
img.save('bulletproof_launcher_icon_64.png')
" 2>/dev/null || echo "🚀" > icon.txt
    }
    
    chmod +x "$launcher_path/simple_bulletproof_launcher.py"
    
    print_success "Launcher downloaded!"
}

# Create desktop integration
create_desktop_integration() {
    print_step "Setting up desktop integration..."
    
    # Create desktop entry
    mkdir -p "$HOME/.local/share/applications"
    cat > "$HOME/.local/share/applications/enhanced-bulletproof-launcher.desktop" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Enhanced Bulletproof Launcher
GenericName=Application Launcher
Comment=Ultimate application launcher - Organize 6000+ apps with auto-generated icons
Exec=python3 "$launcher_path/simple_bulletproof_launcher.py"
Icon=$INSTALL_DIR/bulletproof_launcher_icon_64.png
Terminal=false
Categories=System;Utility;Launcher;
Keywords=launcher;applications;apps;search;organize;bulletproof;
StartupNotify=true
StartupWMClass=UltimateBulletproofLauncher
EOF
    
    # Create launcher script
    mkdir -p "$HOME/.local/bin"
    cat > "$HOME/.local/bin/bulletproof-launcher" << EOF
#!/bin/bash
cd "$INSTALL_DIR"
python3 enhanced_bulletproof_launcher.py "\$@"
EOF
    chmod +x "$HOME/.local/bin/bulletproof-launcher"
    
    # Update desktop database
    update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || true
    
    print_success "Desktop integration created!"
}

# Setup shell integration
setup_shell() {
    print_step "Setting up shell integration..."
    
    # Add to PATH if needed
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc" 2>/dev/null || true
    fi
    
    # Add aliases
    if ! grep -q "alias bpl=" "$HOME/.bashrc" 2>/dev/null; then
        echo "alias bpl='bulletproof-launcher'" >> "$HOME/.bashrc"
        echo "alias launcher='bulletproof-launcher'" >> "$HOME/.bashrc"
    fi
    
    if [ -f "$HOME/.zshrc" ]; then
        if ! grep -q "alias bpl=" "$HOME/.zshrc" 2>/dev/null; then
            echo "alias bpl='bulletproof-launcher'" >> "$HOME/.zshrc"
            echo "alias launcher='bulletproof-launcher'" >> "$HOME/.zshrc"
        fi
    fi
    
    print_success "Shell integration configured!"
}

# Test installation
test_installation() {
    print_step "Testing installation..."
    
    cd "$INSTALL_DIR"
    
    # Test Python imports
    python3 -c "
import sys
import os
try:
    from PyQt5.QtWidgets import QApplication
    print('✅ PyQt5 OK')
except ImportError:
    print('❌ PyQt5 failed, installing via pip...')
    os.system('pip3 install --user PyQt5')

try:
    from PIL import Image
    print('✅ Pillow OK')
except ImportError:
    print('❌ Pillow failed, installing via pip...')
    os.system('pip3 install --user Pillow')
    
print('✅ Python test completed!')
"
    
    print_success "Installation test completed!"
}

# Create uninstaller
create_uninstaller() {
    print_step "Creating uninstaller..."
    
    cat > "$INSTALL_DIR/uninstall.sh" << 'EOF'
#!/bin/bash
echo "🗑️ Uninstalling Enhanced Bulletproof Launcher..."
rm -rf "$HOME/.local/share/enhanced-bulletproof-launcher"
rm -f "$HOME/.local/share/applications/enhanced-bulletproof-launcher.desktop"
rm -f "$HOME/.local/bin/bulletproof-launcher"
sed -i '/bulletproof-launcher/d' "$HOME/.bashrc" 2>/dev/null || true
sed -i '/bulletproof-launcher/d' "$HOME/.zshrc" 2>/dev/null || true
echo "✅ Uninstallation completed!"
EOF
    chmod +x "$INSTALL_DIR/uninstall.sh"
    
    print_success "Uninstaller created!"
}

# Show completion message
show_completion() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║${WHITE}                    🎉 INSTALLATION COMPLETED! 🎉                   ${GREEN}║${NC}"
    echo -e "${GREEN}║${WHITE}            Enhanced Bulletproof Launcher is Ready!                ${GREEN}║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${FIRE} ${WHITE}How to launch:${NC}"
    echo -e "${STAR} ${CYAN}From menu:${NC} Search for 'Enhanced Bulletproof Launcher'"
    echo -e "${STAR} ${CYAN}From terminal:${NC} Run ${YELLOW}bulletproof-launcher${NC} or ${YELLOW}bpl${NC}"
    echo -e "${STAR} ${CYAN}Direct:${NC} Run ${YELLOW}python3 ~/.local/share/enhanced-bulletproof-launcher/enhanced_bulletproof_launcher.py${NC}"
    echo ""
    echo -e "${DIAMOND} ${WHITE}Features:${NC}"
    echo -e "${CHECK} ${GREEN}Automatic icon generation for ALL apps${NC}"
    echo -e "${CHECK} ${GREEN}Smart organization of 6000+ applications${NC}"
    echo -e "${CHECK} ${GREEN}Lightning-fast search and categorization${NC}"
    echo -e "${CHECK} ${GREEN}Support for Desktop, Snap, Flatpak apps${NC}"
    echo -e "${CHECK} ${GREEN}Beautiful modern interface${NC}"
    echo ""
    echo -e "${PURPLE}To uninstall: ${YELLOW}~/.local/share/enhanced-bulletproof-launcher/uninstall.sh${NC}"
    echo ""
    echo -e "${PURPLE}Launch now? [Y/n]: ${NC}"
    read -r launch_now
    if [[ ! $launch_now =~ ^[Nn]$ ]]; then
        echo -e "${ROCKET} Launching Enhanced Bulletproof Launcher..."
        cd "$INSTALL_DIR"
        python3 enhanced_bulletproof_launcher.py &
        echo -e "${CHECK} ${GREEN}Launcher started! Enjoy!${NC}"
    fi
}

# Main installation function
main() {
    # Check if we're root
    if [ "$EUID" -eq 0 ]; then
        print_error "Please don't run as root! Run as normal user."
        exit 1
    fi
    
    # Check for internet
    if ! ping -c 1 google.com &> /dev/null && ! ping -c 1 8.8.8.8 &> /dev/null; then
        print_error "No internet connection!"
        exit 1
    fi
    
    print_header
    detect_distro
    install_dependencies
    setup_directory
    download_launcher
    create_desktop_integration
    setup_shell
    test_installation
    create_uninstaller
    show_completion
}

# Run the installer
main "$@"
