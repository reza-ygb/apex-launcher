#!/bin/bash

# 📦 APEX Launcher - AUR Package Test Script
# This script helps test the AUR package locally

set -e

echo "📦 APEX Launcher - AUR Package Test"
echo "===================================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if we're on Arch Linux
if ! command -v pacman >/dev/null 2>&1; then
    print_error "This script is for Arch Linux only (requires pacman)"
    exit 1
fi

print_status "Running on Arch Linux"

# Check dependencies
echo "🔍 Checking build dependencies..."

MISSING_DEPS=()

if ! command -v makepkg >/dev/null 2>&1; then
    MISSING_DEPS+=("base-devel")
fi

if ! command -v git >/dev/null 2>&1; then
    MISSING_DEPS+=("git")
fi

if [ ${#MISSING_DEPS[@]} -ne 0 ]; then
    print_warning "Missing dependencies: ${MISSING_DEPS[*]}"
    echo "Installing missing dependencies..."
    sudo pacman -S --needed "${MISSING_DEPS[@]}"
fi

print_status "All build dependencies present"

# Create temporary directory for testing
TEMP_DIR=$(mktemp -d)
cd "$TEMP_DIR"

print_status "Working in: $TEMP_DIR"

# Copy AUR files
echo "📋 Copying AUR files..."
cp /workspaces/apex-launcher/aur/* .

print_status "AUR files copied"

# Validate PKGBUILD
echo "🔍 Validating PKGBUILD..."
if makepkg --printsrcinfo > .SRCINFO.test; then
    print_status "PKGBUILD syntax is valid"
    
    # Compare with existing .SRCINFO
    if diff -u .SRCINFO .SRCINFO.test >/dev/null; then
        print_status ".SRCINFO is up to date"
    else
        print_warning ".SRCINFO needs updating"
        echo "Differences:"
        diff -u .SRCINFO .SRCINFO.test || true
    fi
else
    print_error "PKGBUILD has syntax errors"
    exit 1
fi

# Check if source is available (skip download for now)
echo "🌐 Checking source availability..."
SOURCE_URL=$(grep "^source=" PKGBUILD | sed 's/source=(//' | sed 's/)//' | tr -d '"')
echo "Source URL: $SOURCE_URL"

# We can't actually download since the release doesn't exist yet
print_warning "Skipping source download (release not created yet)"

echo ""
echo "📋 AUR Package Summary"
echo "======================"
echo "Package Name: apex-launcher-bin"
echo "Version: $(grep "^pkgver=" PKGBUILD | cut -d'=' -f2)"
echo "Release: $(grep "^pkgrel=" PKGBUILD | cut -d'=' -f2)"
echo "Architecture: $(grep "^arch=" PKGBUILD | cut -d'=' -f2 | tr -d '()')"

echo ""
echo "📝 Dependencies:"
grep "^depends=" PKGBUILD | sed 's/depends=(//' | sed 's/)//' | tr -d "'" | tr ' ' '\n' | while read dep; do
    [ -n "$dep" ] && echo "  - $dep"
done

echo ""
echo "📝 Optional Dependencies:"
grep "^optdepends=" PKGBUILD -A 10 | grep "'" | sed 's/.*'"'"'/  - /' | sed 's/'"'"'.*//'

echo ""
echo "🎯 Next Steps for AUR Submission"
echo "================================="
echo "1. Create GitHub release v1.0.0"
echo "2. Update sha256sum in PKGBUILD:"
echo "   wget $SOURCE_URL"
echo "   sha256sum v1.0.0.tar.gz"
echo "3. Update PKGBUILD with correct checksum"
echo "4. Test build with: makepkg -si"
echo "5. Submit to AUR:"
echo "   git clone ssh://aur@aur.archlinux.org/apex-launcher-bin.git"
echo "   cp PKGBUILD .SRCINFO apex-launcher.install apex-launcher-bin/"
echo "   cd apex-launcher-bin && git add . && git commit -m 'Initial commit'"
echo "   git push origin master"

print_status "AUR package validation completed! 📦"

# Cleanup
cd /
rm -rf "$TEMP_DIR"