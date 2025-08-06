#!/bin/bash
"""
🚀 ENHANCED BULLETPROOF LAUNCHER - AUTO INSTALLER
💪 Ultimate Installation Script for Arch/Ubuntu
🎯 Automatic Setup for 6000+ Applications

This script will:
✨ Auto-detect your distribution (Arch/Ubuntu) 
🔧 Install all required dependencies
📦 Set up the enhanced launcher
🎨 Configure desktop integration
🚀 Launch the ultimate experience
"""

set -e  # Exit on any error

# Color codes for beautiful output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Emojis for enhanced output
ROCKET="🚀"
GEAR="⚙️"
CHECK="✅"
CROSS="❌"
STAR="⭐"
FIRE="🔥"
DIAMOND="💎"

print_header() {
    echo -e "${BLUE}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${BLUE}║${WHITE}                🚀 ENHANCED BULLETPROOF LAUNCHER INSTALLER         ${BLUE}║${NC}"
    echo -e "${BLUE}║${WHITE}                      💪 Ultimate 10X Power Edition                ${BLUE}║${NC}"
    echo -e "${BLUE}║${WHITE}                    🎯 Auto-Setup for 6000+ Apps                  ${BLUE}║${NC}"
    echo -e "${BLUE}╚══════════════════════════════════════════════════════════════════╝${NC}"
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

detect_distribution() {
    print_step "Detecting your Linux distribution..."
    
    if command -v pacman &> /dev/null; then
        DISTRO="arch"
        print_success "Detected: Arch Linux / Manjaro"
    elif command -v apt &> /dev/null; then
        DISTRO="ubuntu"
        print_success "Detected: Ubuntu / Debian"
    elif command -v dnf &> /dev/null; then
        DISTRO="fedora"
        print_success "Detected: Fedora / Red Hat"
    elif command -v zypper &> /dev/null; then
        DISTRO="opensuse"
        print_success "Detected: openSUSE"
    else
        print_error "Unsupported distribution detected!"
        echo -e "${YELLOW}This script supports: Arch, Ubuntu, Fedora, openSUSE${NC}"
        exit 1
    fi
}

install_dependencies() {
    print_step "Installing required dependencies..."
    
    case $DISTRO in
        "arch")
            print_info "Installing packages via pacman..."
            sudo pacman -Syu --noconfirm
            sudo pacman -S --noconfirm python python-pip python-pyqt5 python-pillow python-requests \
                                     git flatpak snapd python-virtualenv python-setuptools \
                                     ttf-dejavu ttf-liberation noto-fonts-emoji \
                                     desktop-file-utils xdg-utils
            ;;
        "ubuntu")
            print_info "Installing packages via apt..."
            sudo apt update
            sudo apt install -y python3 python3-pip python3-pyqt5 python3-pil python3-requests \
                               git flatpak snapd python3-venv python3-setuptools \
                               fonts-dejavu fonts-liberation fonts-noto-color-emoji \
                               desktop-file-utils xdg-utils
            ;;
        "fedora")
            print_info "Installing packages via dnf..."
            sudo dnf update -y
            sudo dnf install -y python3 python3-pip python3-qt5 python3-pillow python3-requests \
                               git flatpak snapd python3-virtualenv python3-setuptools \
                               dejavu-fonts liberation-fonts google-noto-emoji-color-fonts \
                               desktop-file-utils xdg-utils
            ;;
        "opensuse")
            print_info "Installing packages via zypper..."
            sudo zypper refresh
            sudo zypper install -y python3 python3-pip python3-qt5 python3-Pillow python3-requests \
                                  git flatpak snapd python3-virtualenv python3-setuptools \
                                  dejavu-fonts liberation-fonts noto-coloremoji-fonts \
                                  desktop-file-utils xdg-utils
            ;;
    esac
    
    print_success "System dependencies installed successfully!"
}

install_python_packages() {
    print_step "Installing Python packages..."
    
    # Create virtual environment for better isolation
    if [ ! -d "venv" ]; then
        python3 -m venv venv
        print_success "Created virtual environment"
    fi
    
    source venv/bin/activate
    
    # Upgrade pip first
    pip install --upgrade pip
    
    # Install required packages
    pip install PyQt5 Pillow requests pyyaml sqlite3 hashlib pathlib
    
    print_success "Python packages installed successfully!"
}

setup_directory_structure() {
    print_step "Setting up directory structure..."
    
    # Create necessary directories
    mkdir -p ~/.cache/bulletproof-launcher/icons
    mkdir -p ~/.local/share/applications
    mkdir -p ~/.local/share/icons/hicolor/64x64/apps
    mkdir -p ~/.local/bin
    
    print_success "Directory structure created!"
}

create_desktop_entry() {
    print_step "Creating desktop integration..."
    
    DESKTOP_FILE="$HOME/.local/share/applications/enhanced-bulletproof-launcher.desktop"
    CURRENT_DIR=$(pwd)
    
    cat > "$DESKTOP_FILE" << EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Enhanced Bulletproof Launcher
GenericName=Application Launcher
Comment=Ultimate application launcher with 10X power - Auto-organize 6000+ apps
Exec=python3 "$CURRENT_DIR/enhanced_bulletproof_launcher.py"
Icon=$CURRENT_DIR/bulletproof_launcher_icon_64.png
Terminal=false
Categories=System;Utility;Launcher;
Keywords=launcher;applications;apps;search;organize;
StartupNotify=true
StartupWMClass=UltimateBulletproofLauncher
MimeType=application/x-desktop;
EOF

    chmod +x "$DESKTOP_FILE"
    
    # Copy icon to system location
    if [ -f "bulletproof_launcher_icon_64.png" ]; then
        cp bulletproof_launcher_icon_64.png ~/.local/share/icons/hicolor/64x64/apps/enhanced-bulletproof-launcher.png
    fi
    
    # Update desktop database
    update-desktop-database ~/.local/share/applications 2>/dev/null || true
    
    print_success "Desktop integration configured!"
}

create_launcher_script() {
    print_step "Creating launcher script..."
    
    LAUNCHER_SCRIPT="$HOME/.local/bin/bulletproof-launcher"
    CURRENT_DIR=$(pwd)
    
    cat > "$LAUNCHER_SCRIPT" << EOF
#!/bin/bash
# Enhanced Bulletproof Launcher - Quick Launch Script
cd "$CURRENT_DIR"
if [ -d "venv" ]; then
    source venv/bin/activate
fi
python3 enhanced_bulletproof_launcher.py "\$@"
EOF

    chmod +x "$LAUNCHER_SCRIPT"
    
    print_success "Launcher script created at ~/.local/bin/bulletproof-launcher"
}

configure_autostart() {
    print_step "Setting up autostart (optional)..."
    
    read -p "$(echo -e ${YELLOW}Do you want the launcher to start automatically at login? [y/N]: ${NC})" -r
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        mkdir -p ~/.config/autostart
        AUTOSTART_FILE="$HOME/.config/autostart/enhanced-bulletproof-launcher.desktop"
        CURRENT_DIR=$(pwd)
        
        cat > "$AUTOSTART_FILE" << EOF
[Desktop Entry]
Type=Application
Name=Enhanced Bulletproof Launcher
Exec=python3 "$CURRENT_DIR/enhanced_bulletproof_launcher.py" --minimized
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Comment=Ultimate application launcher with auto-organization
EOF
        
        print_success "Autostart configured!"
    else
        print_info "Autostart skipped"
    fi
}

setup_shell_integration() {
    print_step "Setting up shell integration..."
    
    # Add to PATH if not already there
    if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc 2>/dev/null || true
        print_success "Added ~/.local/bin to PATH"
    else
        print_info "PATH already configured"
    fi
    
    # Create shell aliases
    if ! grep -q "alias bpl=" ~/.bashrc 2>/dev/null; then
        echo "alias bpl='bulletproof-launcher'" >> ~/.bashrc
        echo "alias launcher='bulletproof-launcher'" >> ~/.bashrc
    fi
    
    if [ -f ~/.zshrc ]; then
        if ! grep -q "alias bpl=" ~/.zshrc 2>/dev/null; then
            echo "alias bpl='bulletproof-launcher'" >> ~/.zshrc
            echo "alias launcher='bulletproof-launcher'" >> ~/.zshrc
        fi
    fi
    
    print_success "Shell integration configured!"
}

perform_system_optimization() {
    print_step "Performing system optimizations..."
    
    # Enable additional package sources
    case $DISTRO in
        "arch")
            # Enable multilib if not already enabled
            if ! grep -q "^\[multilib\]" /etc/pacman.conf; then
                print_info "Enabling multilib repository..."
                echo -e "\n[multilib]\nInclude = /etc/pacman.d/mirrorlist" | sudo tee -a /etc/pacman.conf
                sudo pacman -Sy
            fi
            ;;
        "ubuntu")
            # Enable universe repository
            sudo add-apt-repository universe -y 2>/dev/null || true
            # Enable flatpak
            sudo apt install -y flatpak gnome-software-plugin-flatpak 2>/dev/null || true
            flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 2>/dev/null || true
            ;;
    esac
    
    # Configure snapd
    if command -v snap &> /dev/null; then
        sudo systemctl enable --now snapd.socket 2>/dev/null || true
        print_info "Snapd service enabled"
    fi
    
    print_success "System optimizations completed!"
}

run_initial_scan() {
    print_step "Running initial application scan..."
    
    if [ -d "venv" ]; then
        source venv/bin/activate
    fi
    
    # Create a simple script to run the initial scan
    cat > initial_scan.py << 'EOF'
#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from enhanced_bulletproof_launcher import AdvancedApplicationDetector, IconGenerator

print("🔍 Running initial application scan...")
detector = AdvancedApplicationDetector()
apps = detector.detect_applications(force_refresh=True)

total_apps = sum(len(app_list) for app_list in apps.values())
print(f"✅ Initial scan completed! Found {total_apps} applications")

# Generate some icons for testing
icon_gen = IconGenerator()
test_apps = ['firefox', 'code', 'terminal', 'file-manager']
for app in test_apps:
    icon_path = icon_gen.generate_icon(app, 'Internet', 'desktop')
    if icon_path:
        print(f"🎨 Generated icon for {app}")

print("🚀 Enhanced Bulletproof Launcher is ready to use!")
EOF

    python3 initial_scan.py
    rm initial_scan.py
    
    print_success "Initial scan completed!"
}

show_completion_message() {
    echo ""
    echo -e "${GREEN}╔══════════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║${WHITE}                    🎉 INSTALLATION COMPLETED! 🎉                   ${GREEN}║${NC}"
    echo -e "${GREEN}║${WHITE}            Enhanced Bulletproof Launcher is Ready to Rock!        ${GREEN}║${NC}"
    echo -e "${GREEN}╚══════════════════════════════════════════════════════════════════╝${NC}"
    echo ""
    echo -e "${FIRE} ${WHITE}How to use your new launcher:${NC}"
    echo -e "${STAR} ${CYAN}From GUI:${NC} Search for 'Enhanced Bulletproof Launcher' in your applications menu"
    echo -e "${STAR} ${CYAN}From Terminal:${NC} Run ${YELLOW}bulletproof-launcher${NC} or ${YELLOW}bpl${NC}"
    echo -e "${STAR} ${CYAN}Direct Python:${NC} Run ${YELLOW}python3 enhanced_bulletproof_launcher.py${NC}"
    echo ""
    echo -e "${DIAMOND} ${WHITE}Features you'll love:${NC}"
    echo -e "${CHECK} ${GREEN}Automatic icon generation for ALL applications${NC}"
    echo -e "${CHECK} ${GREEN}Smart categorization of 6000+ applications${NC}"
    echo -e "${CHECK} ${GREEN}Lightning-fast search and organization${NC}"
    echo -e "${CHECK} ${GREEN}Support for Desktop, Snap, Flatpak, AppImage apps${NC}"
    echo -e "${CHECK} ${GREEN}Beautiful modern interface with 10X power${NC}"
    echo ""
    echo -e "${PURPLE}Want to launch it now? [Y/n]: ${NC}"
    read -r launch_now
    if [[ ! $launch_now =~ ^[Nn]$ ]]; then
        print_step "Launching Enhanced Bulletproof Launcher..."
        if [ -d "venv" ]; then
            source venv/bin/activate
        fi
        python3 enhanced_bulletproof_launcher.py &
        print_success "Launcher started! Enjoy your enhanced experience!"
    fi
}

# Main installation flow
main() {
    print_header
    
    # Check if running as root
    if [ "$EUID" -eq 0 ]; then
        print_error "Please don't run this script as root!"
        echo -e "${YELLOW}Run it as a normal user. It will ask for sudo when needed.${NC}"
        exit 1
    fi
    
    # Check internet connection
    if ! ping -c 1 google.com &> /dev/null; then
        print_error "No internet connection detected!"
        echo -e "${YELLOW}Please check your internet connection and try again.${NC}"
        exit 1
    fi
    
    print_step "Starting Enhanced Bulletproof Launcher installation..."
    echo ""
    
    detect_distribution
    install_dependencies
    install_python_packages
    setup_directory_structure
    create_desktop_entry
    create_launcher_script
    configure_autostart
    setup_shell_integration
    perform_system_optimization
    run_initial_scan
    
    show_completion_message
}

# Run the installer
main "$@"
