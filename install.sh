#!/usr/bin/env bash
set -euo pipefail

APP_NAME="apex-launcher"
PREFIX="${PREFIX:-$HOME/.local}"
APPDIR="$PREFIX/share/$APP_NAME"
BIN="$PREFIX/bin"
DESKTOP_DIR="$HOME/.local/share/applications"

echo "🚀 Installing APEX Launcher into $PREFIX"

if ! command -v python3 >/dev/null 2>&1; then
    echo "❌ python3 is required. Please install Python 3." >&2
    exit 1
fi

mkdir -p "$APPDIR" "$BIN" "$DESKTOP_DIR"

# Install application files
cp -f "apex_launcher.py" "$APPDIR/"
cp -f "smart_cli_launcher.py" "$APPDIR/"
cp -f "apex-launcher.png" "$APPDIR/"

# Install wrapper
if [ -f "bin/apex-launcher" ]; then
    cp -f "bin/apex-launcher" "$BIN/"
else
    # Fallback: generate a minimal wrapper if running from tarball without bin/
    cat > "$BIN/apex-launcher" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
PKG_NAME="apex-launcher"
SHARE_DIR="$HOME/.local/share/$PKG_NAME"
if python3 -c "import PyQt5" >/dev/null 2>&1 && { [ -n "${DISPLAY:-}" ] || [ -n "${WAYLAND_DISPLAY:-}" ]; }; then
    exec python3 "$SHARE_DIR/apex_launcher.py" "$@"
else
    exec python3 "$SHARE_DIR/smart_cli_launcher.py" "$@"
fi
EOF
fi
chmod 0755 "$BIN/apex-launcher"

# Desktop entry
cp -f "apex-launcher.desktop" "$DESKTOP_DIR/"
sed -i "s|^Icon=.*|Icon=$APPDIR/apex-launcher.png|" "$DESKTOP_DIR/apex-launcher.desktop"

if command -v update-desktop-database >/dev/null 2>&1; then
    update-desktop-database "$HOME/.local/share/applications" || true
fi

echo "✅ Installed. Run: apex-launcher"

# Optional: check dependencies and hint
if ! python3 -c "import PyQt5" >/dev/null 2>&1; then
    echo "ℹ️  PyQt5 missing. GUI will not start; CLI will be used."
    echo "   Ubuntu/Debian: sudo apt install python3-pyqt5"
    echo "   Arch: sudo pacman -S python-pyqt5"
fi
