#!/bin/bash

# 🚀 APEX LAUNCHER - Quick Start Script
# Download and run APEX LAUNCHER without installation

echo "🚀 APEX LAUNCHER - Quick Start"
echo "=============================="
echo ""

# Create temp directory
TEMP_DIR="/tmp/apex-launcher-$$"
mkdir -p "$TEMP_DIR"
cd "$TEMP_DIR"

echo "📥 Downloading APEX LAUNCHER..."

# Download main files
curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/apex_launcher.py -o apex_launcher.py
curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/simple_bulletproof_launcher.py -o simple_launcher.py

echo "🔍 Checking dependencies..."

# Check PyQt5
if python3 -c "import PyQt5" 2>/dev/null; then
    echo "✅ PyQt5 found - using full launcher"
    LAUNCHER="apex_launcher.py"
else
    echo "⚠️ PyQt5 not found - using simple launcher"
    echo "💡 Install PyQt5 for best experience:"
    echo "   Ubuntu: sudo apt install python3-pyqt5"
    echo "   Arch:   sudo pacman -S python-pyqt5"
    echo "   Fedora: sudo dnf install python3-qt5"
    echo ""
    LAUNCHER="simple_launcher.py"
fi

echo "🚀 Starting APEX LAUNCHER..."
echo ""

# Run launcher
python3 "$LAUNCHER"

# Cleanup
cd /
rm -rf "$TEMP_DIR"

echo ""
echo "🎉 Thanks for trying APEX LAUNCHER!"
echo "💡 For permanent installation: curl -fsSL https://raw.githubusercontent.com/reza-ygb/apex-launcher/main/apex_install.sh | bash"
