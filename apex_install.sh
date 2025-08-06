#!/bin/bash

# 🚀 APEX LAUNCHER - Universal One-Line Installer
# Compatible with ALL Linux distributions

set -e

echo "🚀 APEX LAUNCHER - Universal Installer"
echo "========================================"
echo "🎯 Installing the Ultimate Linux Application Launcher"
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

# Detect distribution
detect_distro() {
    if [ -f /etc/os-release ]; then
        . /etc/os-release
        DISTRO=$ID
        DISTRO_LIKE=$ID_LIKE
    elif [ -f /etc/redhat-release ]; then
        DISTRO="rhel"
    elif [ -f /etc/debian_version ]; then
        DISTRO="debian"
    else
        DISTRO="unknown"
    fi
    
    print_status "Detected distribution: $DISTRO"
}

# Install dependencies based on distribution
install_dependencies() {
    print_status "Installing dependencies for $DISTRO..."
    
    case $DISTRO in
        ubuntu|debian|linuxmint|pop|elementary)
            print_status "Using apt package manager..."
            sudo apt update
            sudo apt install -y python3 python3-pip python3-pyqt5 python3-pil curl wget git
            ;;
        arch|manjaro|endeavouros|garuda)
            print_status "Using pacman package manager..."
            sudo pacman -Sy --noconfirm python python-pip python-pyqt5 python-pillow curl wget git
            ;;
        fedora|centos|rhel|rocky|almalinux)
            print_status "Using dnf/yum package manager..."
            if command -v dnf &> /dev/null; then
                sudo dnf install -y python3 python3-pip python3-qt5 python3-pillow curl wget git
            else
                sudo yum install -y python3 python3-pip python3-qt5 python3-pillow curl wget git
            fi
            ;;
        opensuse|opensuse-leap|opensuse-tumbleweed)
            print_status "Using zypper package manager..."
            sudo zypper install -y python3 python3-pip python3-qt5 python3-Pillow curl wget git
            ;;
        alpine)
            print_status "Using apk package manager..."
            sudo apk add python3 py3-pip py3-qt5 py3-pillow curl wget git
            ;;
        gentoo)
            print_status "Using emerge package manager..."
            sudo emerge dev-lang/python dev-python/pip dev-python/PyQt5 dev-python/pillow net-misc/curl net-misc/wget dev-vcs/git
            ;;
        *)
            print_warning "Unknown distribution. Trying pip installation..."
            if command -v python3 &> /dev/null; then
                python3 -m pip install --user PyQt5 Pillow
            else
                print_error "Python3 not found. Please install Python3 manually."
                exit 1
            fi
            ;;
    esac
}

# Download and install APEX Launcher
install_apex_launcher() {
    print_status "Installing APEX Launcher..."
    
    # Create installation directory
    INSTALL_DIR="/usr/local/share/apex-launcher"
    BIN_DIR="/usr/local/bin"
    
    # Download files
    print_status "Downloading APEX Launcher files..."
    
    # Create temporary directory
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    
    # Download main launcher
    curl -fsSL "https://raw.githubusercontent.com/yourusername/apex-launcher/main/apex_launcher.py" -o apex_launcher.py
    
    # Download simple launcher (fallback)
    curl -fsSL "https://raw.githubusercontent.com/yourusername/apex-launcher/main/simple_bulletproof_launcher.py" -o simple_launcher.py
    
    # Download icon
    curl -fsSL "https://raw.githubusercontent.com/yourusername/apex-launcher/main/bulletproof_launcher_icon_64.png" -o apex_launcher_icon.png
    
    # Download desktop file
    curl -fsSL "https://raw.githubusercontent.com/yourusername/apex-launcher/main/apex-launcher.desktop" -o apex-launcher.desktop
    
    # Create installation directories
    sudo mkdir -p "$INSTALL_DIR"
    sudo mkdir -p "/usr/share/pixmaps"
    sudo mkdir -p "/usr/share/applications"
    
    # Install files
    sudo cp apex_launcher.py "$INSTALL_DIR/"
    sudo cp simple_launcher.py "$INSTALL_DIR/"
    sudo cp apex_launcher_icon.png "/usr/share/pixmaps/apex-launcher.png"
    sudo cp apex-launcher.desktop "/usr/share/applications/"
    
    # Create executable launcher script
    sudo tee "$BIN_DIR/apex-launcher" > /dev/null << 'EOF'
#!/bin/bash
# APEX Launcher startup script

LAUNCHER_DIR="/usr/local/share/apex-launcher"

# Try main launcher first
if python3 -c "import PyQt5" 2>/dev/null; then
    python3 "$LAUNCHER_DIR/apex_launcher.py" "$@"
else
    echo "⚠️ PyQt5 not available, using simple launcher..."
    python3 "$LAUNCHER_DIR/simple_launcher.py" "$@"
fi
EOF
    
    # Make launcher executable
    sudo chmod +x "$BIN_DIR/apex-launcher"
    
    # Update desktop database
    if command -v update-desktop-database &> /dev/null; then
        sudo update-desktop-database /usr/share/applications
    fi
    
    # Clean up
    cd /
    rm -rf "$TEMP_DIR"
}

# Create user configuration
setup_user_config() {
    print_status "Setting up user configuration..."
    
    CONFIG_DIR="$HOME/.config/apex-launcher"
    CACHE_DIR="$HOME/.cache/apex-launcher"
    
    mkdir -p "$CONFIG_DIR"
    mkdir -p "$CACHE_DIR"
    
    # Create default configuration
    cat > "$CONFIG_DIR/config.json" << 'EOF'
{
    "theme": "glassmorphism",
    "auto_scan": true,
    "cache_duration": 300,
    "show_hidden": false,
    "grid_columns": 4,
    "icon_size": 64
}
EOF
    
    print_success "User configuration created in $CONFIG_DIR"
}

# Main installation process
main() {
    echo ""
    print_status "Starting APEX Launcher installation..."
    echo ""
    
    # Check if running as root
    if [ "$EUID" -eq 0 ]; then
        print_error "Please do not run this installer as root!"
        print_status "Run as normal user - sudo will be used when needed."
        exit 1
    fi
    
    # Check for internet connection
    if ! curl -s --connect-timeout 5 https://google.com > /dev/null; then
        print_error "No internet connection available!"
        exit 1
    fi
    
    # Detect distribution and install dependencies
    detect_distro
    install_dependencies
    
    # Install APEX Launcher
    install_apex_launcher
    
    # Setup user configuration
    setup_user_config
    
    echo ""
    print_success "🚀 APEX LAUNCHER INSTALLATION COMPLETE!"
    echo ""
    echo -e "${BLUE}Launch Commands:${NC}"
    echo "  • Command line: ${GREEN}apex-launcher${NC}"
    echo "  • Applications menu: ${GREEN}APEX Launcher${NC}"
    echo "  • Desktop shortcut: ${GREEN}Created automatically${NC}"
    echo ""
    echo -e "${BLUE}Quick Start:${NC}"
    echo "  • Press ${GREEN}Ctrl+F${NC} to search applications"
    echo "  • Press ${GREEN}F5${NC} to refresh app list"
    echo "  • Click categories on the left to browse"
    echo ""
    echo -e "${PURPLE}Enjoy the ultimate Linux application launcher! 🎯${NC}"
    echo ""
}

# Run main installation
main
