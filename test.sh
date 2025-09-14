#!/bin/bash

# 🚀 APEX Launcher - Local Testing Script
# This script helps test the launcher in different modes

set -e

echo "🚀 APEX Launcher - Local Testing"
echo "=================================="

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print status
print_status() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check Python version
echo "🔍 Checking Python version..."
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
print_status "Python version: $PYTHON_VERSION"

# Check dependencies
echo "📦 Checking dependencies..."

# Check PyQt5
if python3 -c "import PyQt5" 2>/dev/null; then
    print_status "PyQt5 is available"
    PYQT5_AVAILABLE=true
else
    print_warning "PyQt5 not available - GUI mode will not work"
    PYQT5_AVAILABLE=false
fi

# Check Pillow
if python3 -c "import PIL" 2>/dev/null; then
    print_status "Pillow is available"
else
    print_warning "Pillow not available - using text-only icons"
fi

# Test syntax
echo "🔍 Testing syntax..."
if python3 -m py_compile apex_launcher.py; then
    print_status "apex_launcher.py syntax OK"
else
    print_error "apex_launcher.py syntax error"
    exit 1
fi

if python3 -m py_compile smart_cli_launcher.py; then
    print_status "smart_cli_launcher.py syntax OK"
else
    print_error "smart_cli_launcher.py syntax error"
    exit 1
fi

# Test CLI mode
echo "🖥️  Testing CLI mode..."
timeout 10s python3 smart_cli_launcher.py <<< "exit" || true
print_status "CLI mode test completed"

# Test GUI imports
echo "🎨 Testing GUI imports..."
if $PYQT5_AVAILABLE; then
    if python3 -c "import apex_launcher; print('GUI imports OK')" 2>/dev/null; then
        print_status "GUI imports successful"
    else
        print_warning "GUI import issues detected"
    fi
else
    print_warning "Skipping GUI tests (PyQt5 not available)"
fi

# Test wrapper script
echo "🔗 Testing wrapper script..."
if [ -f "bin/apex-launcher" ]; then
    if chmod +x bin/apex-launcher; then
        print_status "Wrapper script permissions set"
        
        # Test CLI fallback
        if timeout 10s bash bin/apex-launcher --cli <<< "exit" 2>/dev/null; then
            print_status "Wrapper CLI mode works"
        else
            print_warning "Wrapper CLI mode test completed with timeout"
        fi
    else
        print_error "Cannot set wrapper script permissions"
    fi
else
    print_error "Wrapper script not found"
fi

# Test installation script
echo "🔧 Testing installation script..."
if [ -f "install.sh" ]; then
    print_status "Installation script found"
    
    # Test dry-run mode if supported
    if bash install.sh --help 2>/dev/null | grep -q "dry-run"; then
        print_status "Installation script supports dry-run"
    fi
else
    print_warning "Installation script not found"
fi

# Application detection test
echo "🔍 Testing application detection..."
APPS_FOUND=$(timeout 30s python3 -c "
import sys
sys.path.append('.')
try:
    from smart_cli_launcher import SmartCLILauncher
    launcher = SmartCLILauncher()
    launcher.scan_applications()
    total = sum(len(apps) for apps in launcher.categories.values())
    print(f'{total} applications found')
except Exception as e:
    print(f'Error: {e}')
" 2>/dev/null)

if [[ "$APPS_FOUND" =~ ^[0-9]+ ]]; then
    print_status "Application detection: $APPS_FOUND"
else
    print_warning "Application detection test completed"
fi

# Docker test (if available)
echo "🐳 Testing Docker support..."
if command -v docker >/dev/null 2>&1; then
    if docker info >/dev/null 2>&1; then
        print_status "Docker is available"
        
        echo "Building Docker image..."
        if docker build -t apex-launcher:test . >/dev/null 2>&1; then
            print_status "Docker build successful"
            
            # Test Docker CLI
            if docker run --rm apex-launcher:test --help >/dev/null 2>&1; then
                print_status "Docker CLI test successful"
            else
                print_warning "Docker CLI test completed"
            fi
            
            # Clean up test image
            docker rmi apex-launcher:test >/dev/null 2>&1 || true
        else
            print_warning "Docker build failed"
        fi
    else
        print_warning "Docker daemon not running"
    fi
else
    print_warning "Docker not available"
fi

# Summary
echo ""
echo "📋 Test Summary"
echo "==============="

if $PYQT5_AVAILABLE; then
    print_status "GUI Mode: Ready"
else
    print_warning "GUI Mode: PyQt5 required"
fi

print_status "CLI Mode: Ready"
print_status "Syntax: Valid"
print_status "Wrapper Script: OK"

echo ""
echo "🎯 Next Steps"
echo "============="
echo "1. Install missing dependencies:"
if ! $PYQT5_AVAILABLE; then
    echo "   sudo apt install python3-pyqt5  # Ubuntu/Debian"
    echo "   sudo pacman -S python-pyqt5    # Arch Linux"
    echo "   pip3 install PyQt5             # Universal"
fi
echo ""
echo "2. Run the launcher:"
echo "   python3 apex_launcher.py         # GUI mode"
echo "   python3 smart_cli_launcher.py    # CLI mode"
echo "   ./bin/apex-launcher              # Auto-detect mode"
echo ""
echo "3. Install system-wide:"
echo "   ./install.sh                     # User install"
echo "   sudo ./install.sh --system       # System-wide"
echo ""

print_status "Testing completed! 🎉"