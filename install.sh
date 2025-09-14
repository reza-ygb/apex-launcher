#!/usr/bin/env bash
set -euo pipefail

APP_NAME="apex-launcher"
REPO_URL="https://github.com/reza-ygb/apex-launcher"
PREFIX="${PREFIX:-$HOME/.local}"
APPDIR="$PREFIX/share/$APP_NAME"
BIN="$PREFIX/bin"
DESKTOP_DIR="$HOME/.local/share/applications"

echo "🚀 APEX Launcher Installation Script"
echo "====================================="

# Check if running from source directory or need to download
if [ -f "apex_launcher.py" ] && [ -f "smart_cli_launcher.py" ]; then
    echo "📁 Installing from source directory..."
    INSTALL_FROM_SOURCE=true
else
    echo "📥 Downloading latest release..."
    INSTALL_FROM_SOURCE=false
fi

# Check Python
if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ Python 3 is required. Please install Python 3.6+" >&2
    exit 1
fi

PYTHON_VERSION=$(python3 -c "import sys; print('.'.join(map(str, sys.version_info[:2])))")
echo "✅ Python $PYTHON_VERSION detected"

# Create directories
mkdir -p "$APPDIR" "$BIN" "$DESKTOP_DIR"

if [ "$INSTALL_FROM_SOURCE" = true ]; then
    # Install from current directory
    echo "📋 Installing application files..."
    
    # Check required files exist
    REQUIRED_FILES=("apex_launcher.py" "smart_cli_launcher.py" "bin/apex-launcher" "apex-launcher.desktop" "apex-launcher.png")
    for file in "${REQUIRED_FILES[@]}"; do
        if [ ! -f "$file" ]; then
            echo "❌ Required file missing: $file" >&2
            echo "   Please run from the apex-launcher source directory" >&2
            exit 1
        fi
    done
    
    # Install files
    cp -f "apex_launcher.py" "$APPDIR/"
    cp -f "smart_cli_launcher.py" "$APPDIR/"
    cp -f "apex-launcher.png" "$APPDIR/"
    cp -f "VERSION" "$APPDIR/" 2>/dev/null || echo "1.0.0" > "$APPDIR/VERSION"
    
    # Install wrapper script
    cp -f "bin/apex-launcher" "$BIN/"
    chmod +x "$BIN/apex-launcher"
    
    # Install desktop entry
    cp -f "apex-launcher.desktop" "$DESKTOP_DIR/"
    
    VERSION=$(cat VERSION 2>/dev/null || echo "1.0.0")
    echo "✅ Installed APEX Launcher v$VERSION from source"
    
else
    # Download and install from GitHub
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    
    echo "📥 Downloading latest release..."
    
    # Try to get latest release, fallback to main branch
    if command -v curl >/dev/null 2>&1; then
        if ! curl -fsSL "$REPO_URL/archive/main.tar.gz" | tar -xz; then
            echo "❌ Failed to download apex-launcher" >&2
            exit 1
        fi
    elif command -v wget >/dev/null 2>&1; then
        if ! wget -q -O - "$REPO_URL/archive/main.tar.gz" | tar -xz; then
            echo "❌ Failed to download apex-launcher" >&2
            exit 1
        fi
    else
        echo "❌ Neither curl nor wget available. Please install one of them." >&2
        exit 1
    fi
    
    cd apex-launcher-main/
    
    # Install files
    cp -f "apex_launcher.py" "$APPDIR/"
    cp -f "smart_cli_launcher.py" "$APPDIR/"
    cp -f "apex-launcher.png" "$APPDIR/"
    cp -f "VERSION" "$APPDIR/" 2>/dev/null || echo "1.0.0" > "$APPDIR/VERSION"
    
    # Install wrapper script
    cp -f "bin/apex-launcher" "$BIN/"
    chmod +x "$BIN/apex-launcher"
    
    # Install desktop entry
    cp -f "apex-launcher.desktop" "$DESKTOP_DIR/"
    
    VERSION=$(cat VERSION 2>/dev/null || echo "1.0.0")
    echo "✅ Downloaded and installed APEX Launcher v$VERSION"
    
    # Cleanup
    cd /
    rm -rf "$TEMP_DIR"
fi

# Fix desktop entry paths
sed -i "s|^Icon=.*|Icon=$APPDIR/apex-launcher.png|" "$DESKTOP_DIR/apex-launcher.desktop"
sed -i "s|^Exec=.*|Exec=$BIN/apex-launcher|" "$DESKTOP_DIR/apex-launcher.desktop"

# Update desktop database if available
if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database "$DESKTOP_DIR" 2>/dev/null || true
fi

# Check PyQt5 availability
if python3 -c "import PyQt5" >/dev/null 2>&1; then
    GUI_AVAILABLE="✅ GUI mode available"
else
    GUI_AVAILABLE="⚠️  GUI mode unavailable (PyQt5 not installed)"
fi

echo ""
echo "🎉 Installation completed successfully!"
echo "======================================"
echo "📦 Installed to: $APPDIR"
echo "🔗 Launcher: $BIN/apex-launcher"
echo "🖥️  Desktop entry: $DESKTOP_DIR/apex-launcher.desktop"
echo "$GUI_AVAILABLE"
echo ""
echo "🚀 Usage:"
echo "  apex-launcher          # GUI mode (if available)"
echo "  apex-launcher --cli    # CLI mode (always works)"
echo ""

if ! echo "$PATH" | grep -q "$BIN"; then
    echo "⚠️  Note: $BIN is not in your PATH"
    echo "   Add this to your ~/.bashrc or ~/.zshrc:"
    echo "   export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo ""
    echo "🔧 Adding to current session..."
    export PATH="$BIN:$PATH"
    echo "✅ PATH updated for this session"
    echo ""
fi

echo "💡 If GUI mode doesn't work, install PyQt5:"
echo "   # Ubuntu/Debian: sudo apt install python3-pyqt5"
echo "   # Arch: sudo pacman -S python-pyqt5"  
echo "   # Universal: pip3 install --user PyQt5"

echo "✅ Installed. Run: apex-launcher"

# Optional: check dependencies and hint
if ! python3 -c "import PyQt5" >/dev/null 2>&1; then
    echo "ℹ️  PyQt5 missing. GUI will not start; CLI will be used."
    echo "   Ubuntu/Debian: sudo apt install python3-pyqt5"
    echo "   Arch: sudo pacman -S python-pyqt5"
fi
