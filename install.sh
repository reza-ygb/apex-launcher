#!/bin/bash

# Enhanced Bulletproof Launcher - Simple Install Script
echo "🚀 Installing Enhanced Bulletproof Launcher..."

# Create directories
mkdir -p ~/.local/bin
mkdir -p ~/.local/share/applications

# Copy launcher
cp simple_bulletproof_launcher.py ~/.local/bin/
chmod +x ~/.local/bin/simple_bulletproof_launcher.py

# Create desktop entry
cat > ~/.local/share/applications/bulletproof-launcher.desktop << EOF
[Desktop Entry]
Name=Enhanced Bulletproof Launcher
Comment=Ultra-fast application launcher
Exec=python3 ~/.local/bin/simple_bulletproof_launcher.py
Icon=application-x-executable
Terminal=false
Type=Application
Categories=Utility;
EOF

# Create symlink
ln -sf ~/.local/bin/simple_bulletproof_launcher.py ~/.local/bin/bulletproof-launcher

echo "✅ Installation complete!"
echo "🚀 Run: bulletproof-launcher"

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3 first."
    exit 1
fi

PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
echo "✅ Found Python $PYTHON_VERSION"

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "� Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Make scripts executable
chmod +x launcher.sh
chmod +x bulletproof_launcher.py
chmod +x smart_cli_launcher.py

# Create desktop icon
echo "🎨 Creating application icon..."
python3 create_icon.py

# Install desktop file
echo "🖥️  Installing desktop integration..."
DESKTOP_DIR="$HOME/.local/share/applications"
mkdir -p "$DESKTOP_DIR"

# Update desktop file with correct paths
LAUNCHER_PATH="$(pwd)/bulletproof_launcher.py"
ICON_PATH="$(pwd)/bulletproof_launcher_icon.png"

sed "s|LAUNCHER_PATH|$LAUNCHER_PATH|g; s|ICON_PATH|$ICON_PATH|g" bulletproof-launcher.desktop > "$DESKTOP_DIR/bulletproof-launcher.desktop"

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    update-desktop-database "$DESKTOP_DIR"
fi

echo "✅ Installation complete!"
echo ""
echo "🎯 Available launchers:"
echo "   • GUI Launcher: python3 bulletproof_launcher.py"
echo "   • CLI Launcher: python3 smart_cli_launcher.py"
echo "   • Rofi Launcher: ./launcher.sh"
echo ""
echo "📱 The GUI launcher is now available in your applications menu!"
echo "   Look for 'Smart Launcher' in the Utilities category."
