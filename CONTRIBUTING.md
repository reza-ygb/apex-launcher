# 🤝 Contributing to APEX Launcher

Thank you for your interest in contributing to APEX Launcher! We welcome contributions from everyone.

## 🚀 Quick Start

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/apex-launcher.git
   cd apex-launcher
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make** your changes
5. **Test** your changes:
   ```bash
   python3 apex_launcher.py     # Test GUI
   python3 smart_cli_launcher.py # Test CLI
   ```
6. **Commit** your changes:
   ```bash
   git commit -m "Add: your feature description"
   ```
7. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
8. **Create** a Pull Request

## 🐛 Bug Reports

When reporting bugs, please include:

- **OS and version** (e.g., Ubuntu 22.04, Arch Linux)
- **Python version** (`python3 --version`)
- **Error messages** (full traceback if available)
- **Steps to reproduce** the issue
- **Expected vs actual behavior**

Use our bug report template:

```markdown
**Bug Description:**
A clear description of the bug.

**Environment:**
- OS: [e.g., Ubuntu 22.04]
- Python: [e.g., 3.11.2]
- PyQt5: [e.g., 5.15.9]

**Steps to Reproduce:**
1. Launch apex-launcher
2. Click on '...'
3. See error

**Expected Behavior:**
What should happen.

**Actual Behavior:**
What actually happens.

**Error Messages:**
```
Paste any error messages here
```
```

## 💡 Feature Requests

We love new ideas! When suggesting features:

- **Check existing issues** first
- **Describe the use case** - why is this needed?
- **Provide examples** of how it would work
- **Consider backwards compatibility**

## 🔧 Development Guidelines

### Code Style

- **PEP 8** compliance (use `flake8` for linting)
- **Clear variable names** and functions
- **Comments** for complex logic
- **Docstrings** for public functions

### Architecture

The launcher has two main components:

1. **GUI Mode** (`apex_launcher.py`):
   - PyQt5-based interface
   - Application scanning and categorization
   - Icon generation system

2. **CLI Mode** (`smart_cli_launcher.py`):
   - Terminal-based interface  
   - Fallback for systems without GUI
   - Menu-driven navigation

### Key Design Principles

- **Lightweight** - Minimal RAM usage (target: <50MB)
- **Fast** - Quick startup and app detection
- **Reliable** - Never crash, graceful error handling
- **Universal** - Works on all Linux distributions
- **Simple** - Clean, intuitive interface

### Testing

Before submitting:

```bash
# Test CLI mode
python3 smart_cli_launcher.py

# Test GUI mode (if PyQt5 available)
python3 apex_launcher.py

# Check syntax
python3 -m py_compile apex_launcher.py
python3 -m py_compile smart_cli_launcher.py

# Run linter
flake8 *.py
```

### Docker Development

```bash
# Build development container
docker-compose --profile dev up

# Test CLI in Docker
docker-compose --profile cli run apex-launcher-cli

# Test GUI in Docker (Linux with X11)
xhost +local:docker
docker-compose --profile gui run apex-launcher-gui
```

## 📦 Areas for Contribution

### High Priority

- 🐛 **Bug fixes** - Always welcome
- ⚡ **Performance improvements** - Faster scanning, lower memory usage
- 🔍 **Better app detection** - Support for more app sources
- 🎨 **Icon improvements** - Better icon generation algorithms
- 📖 **Documentation** - README improvements, code comments

### Medium Priority

- 🌍 **Internationalization** - Multi-language support
- 🎯 **Better categorization** - Smarter app classification
- 🔧 **Configuration** - User-customizable settings
- 📊 **Statistics** - Usage tracking and analytics

### Ideas Welcome

- 🚀 **New features** - Suggest anything that fits the philosophy
- 🔌 **Plugin system** - Extensibility framework
- 🎨 **Themes** - Customizable appearance
- ⌨️ **Keyboard shortcuts** - Power user features

## 🎯 Contribution Types

### Code Contributions

- New features
- Bug fixes  
- Performance improvements
- Code cleanup and refactoring

### Documentation

- README improvements
- Code documentation
- Tutorials and guides
- Translation to other languages

### Testing

- Manual testing on different distributions
- Automated test development
- Performance benchmarking
- User experience testing

### Design

- UI/UX improvements
- Icon design
- Color scheme suggestions
- Logo and branding

## 📋 Pull Request Guidelines

### Before Submitting

- [ ] Code follows PEP 8 style guidelines
- [ ] All tests pass
- [ ] New features include documentation
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts with main branch

### PR Description Template

```markdown
## Changes Made
- Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Performance improvement
- [ ] Documentation update
- [ ] Code refactoring

## Testing
- [ ] Tested on my local machine
- [ ] GUI mode works
- [ ] CLI mode works
- [ ] No new errors or warnings

## Screenshots (if applicable)
<!-- Add screenshots for UI changes -->
```

### Review Process

1. **Automated checks** run first (CI tests)
2. **Code review** by maintainers
3. **Testing** on different systems
4. **Merge** after approval

## 🏆 Recognition

Contributors are recognized in:

- GitHub contributors list
- Release notes mentions
- README acknowledgments  
- Special contributor badges

## 📞 Getting Help

- **GitHub Issues** - Ask questions, report bugs
- **GitHub Discussions** - General discussion, ideas
- **Email** - Direct contact with maintainers

## 📜 Code of Conduct

Be respectful, inclusive, and helpful:

- 🤝 **Be welcoming** to newcomers
- 💬 **Communicate clearly** and constructively  
- 🎯 **Focus on the code**, not the person
- 🌟 **Help others learn** and grow
- 🚫 **No harassment** or discrimination

## 🎉 Thank You!

Every contribution matters, whether it's:

- 🐛 A bug report
- 💡 A feature idea  
- 🔧 A code improvement
- 📖 Documentation fixes
- ⭐ A GitHub star

**Together, we're building the ultimate Linux application launcher!** 🚀

---

Made with ❤️ by the Linux community