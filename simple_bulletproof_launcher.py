#!/usr/bin/env python3
"""
🚀 ENHANCED BULLETPROOF LAUNCHER - SIMPLIFIED VERSION
💪 Works with minimal dependencies - Maximum compatibility
🎯 Automatic icon generation and smart organization

Requirements:
- Python 3.7+
- PyQt5 (system package recommended)
- Optional: Pillow for advanced icons
"""

import sys
import os
import subprocess
import configparser
import json
import hashlib
import time
import sqlite3
from pathlib import Path
from collections import defaultdict

# Core imports
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    HAS_PYQT5 = True
except ImportError:
    print("❌ PyQt5 not found!")
    print("📦 Install with:")
    print("  Ubuntu/Debian: sudo apt install python3-pyqt5")
    print("  Arch: sudo pacman -S python-pyqt5") 
    print("  Fedora: sudo dnf install python3-qt5")
    sys.exit(1)

# Optional imports
try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("ℹ️  Pillow not found - using text-based icons")

print(f"🚀 Enhanced Bulletproof Launcher v3.0")
print(f"📦 PyQt5: ✅  PIL: {'✅' if HAS_PIL else '❌'}")


class SimpleIconGenerator:
    """🎨 Simple Icon Generator - Works with or without PIL"""
    
    def __init__(self):
        self.cache_dir = Path.home() / '.cache' / 'bulletproof-launcher'
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        # Category styling
        self.category_styles = {
            'Programming': {'emoji': '💻', 'color': '#4CAF50'},
            'Security': {'emoji': '🔒', 'color': '#F44336'},
            'System': {'emoji': '⚙️', 'color': '#FF9800'},
            'Internet': {'emoji': '🌐', 'color': '#2196F3'},
            'Media': {'emoji': '🎬', 'color': '#9C27B0'},
            'Office': {'emoji': '📄', 'color': '#607D8B'},
            'Graphics': {'emoji': '🎨', 'color': '#E91E63'},
            'Games': {'emoji': '🎮', 'color': '#3F51B5'},
            'Development': {'emoji': '🔧', 'color': '#009688'},
            'Education': {'emoji': '📚', 'color': '#795548'},
            'Other': {'emoji': '📁', 'color': '#9E9E9E'}
        }
        
        # App-specific emojis
        self.app_emojis = {
            'firefox': '🔥', 'chrome': '🌎', 'chromium': '🌎',
            'code': '💻', 'vscode': '💻', 'vim': '📝',
            'terminal': '⚡', 'konsole': '⚡', 'gnome-terminal': '⚡',
            'nautilus': '📁', 'dolphin': '📁', 'thunar': '📁',
            'gimp': '🎨', 'inkscape': '🎨', 'blender': '🎬',
            'vlc': '▶️', 'spotify': '🎵', 'discord': '💬',
            'steam': '🎮', 'wine': '🍷', 'lutris': '🎮',
            'libreoffice': '📄', 'writer': '📝', 'calc': '📊',
            'thunderbird': '📧', 'telegram': '📱',
            'virtualbox': '📦', 'docker': '📦',
            'wireshark': '🔍', 'nmap': '🔍'
        }
    
    def get_icon_info(self, app_name, category='Other'):
        """Get icon information for an app"""
        app_lower = app_name.lower()
        
        # Check for app-specific emoji
        emoji = None
        for app_key, app_emoji in self.app_emojis.items():
            if app_key in app_lower:
                emoji = app_emoji
                break
        
        # Use category emoji if no specific one found
        if not emoji:
            style = self.category_styles.get(category, self.category_styles['Other'])
            emoji = style['emoji']
        
        style = self.category_styles.get(category, self.category_styles['Other'])
        
        return {
            'emoji': emoji,
            'color': style['color'],
            'category': category
        }


class SmartAppDetector:
    """🔍 Smart Application Detection - Ultra Fast"""
    
    def __init__(self):
        self.db_path = Path.home() / '.cache' / 'bulletproof-launcher' / 'apps.db'
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.init_database()
        
        # Smart categories
        self.categories = {
            'Programming': ['code', 'editor', 'ide', 'python', 'java', 'git', 'vim', 'dev'],
            'Security': ['security', 'hack', 'nmap', 'wireshark', 'burp', 'kali'],
            'System': ['system', 'monitor', 'htop', 'top', 'systemctl', 'mount'],
            'Internet': ['browser', 'firefox', 'chrome', 'mail', 'wget', 'curl'],
            'Media': ['video', 'audio', 'vlc', 'spotify', 'gimp', 'photo'],
            'Office': ['office', 'document', 'libreoffice', 'pdf', 'writer'],
            'Graphics': ['graphics', 'design', 'gimp', 'inkscape', 'photo'],
            'Games': ['game', 'steam', 'lutris', 'wine', 'play'],
            'Development': ['terminal', 'console', 'shell', 'ssh'],
            'Education': ['learn', 'education', 'study', 'tutorial']
        }
    
    def init_database(self):
        """Initialize app database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS apps (
                        name TEXT PRIMARY KEY,
                        command TEXT,
                        description TEXT,
                        category TEXT,
                        type TEXT,
                        last_scan INTEGER
                    )
                ''')
                conn.commit()
        except Exception:
            pass
    
    def scan_applications(self):
        """Scan for all applications"""
        print("🔍 Scanning applications...")
        
        apps = {}
        
        # Scan desktop files
        desktop_apps = self._scan_desktop_files()
        apps.update(desktop_apps)
        print(f"📱 Found {len(desktop_apps)} desktop apps")
        
        # Scan command line tools (limited)
        cli_apps = self._scan_cli_tools()
        apps.update(cli_apps)
        print(f"⚡ Found {len(cli_apps)} CLI tools")
        
        # Scan snap packages
        snap_apps = self._scan_snap_packages()
        apps.update(snap_apps)
        print(f"📦 Found {len(snap_apps)} snap packages")
        
        # Scan flatpak packages
        flatpak_apps = self._scan_flatpak_packages()
        apps.update(flatpak_apps)
        print(f"📦 Found {len(flatpak_apps)} flatpak apps")
        
        # Categorize all apps
        categorized = self._categorize_apps(apps)
        
        print(f"✅ Total: {sum(len(v) for v in categorized.values())} applications")
        return categorized
    
    def _scan_desktop_files(self):
        """Scan .desktop files"""
        apps = {}
        desktop_dirs = [
            '/usr/share/applications',
            '/usr/local/share/applications',
            os.path.expanduser('~/.local/share/applications')
        ]
        
        for desktop_dir in desktop_dirs:
            if not os.path.exists(desktop_dir):
                continue
                
            try:
                for file_path in Path(desktop_dir).glob('*.desktop'):
                    try:
                        config = configparser.ConfigParser()
                        config.read(file_path, encoding='utf-8')
                        
                        if 'Desktop Entry' not in config:
                            continue
                            
                        entry = config['Desktop Entry']
                        if entry.get('NoDisplay', '').lower() == 'true':
                            continue
                        
                        name = entry.get('Name', file_path.stem)
                        command = entry.get('Exec', '').split()[0] if entry.get('Exec') else ''
                        description = entry.get('Comment', entry.get('GenericName', 'Desktop Application'))
                        
                        apps[name] = {
                            'command': command,
                            'description': description,
                            'type': 'desktop'
                        }
                    except Exception:
                        continue
            except Exception:
                continue
                
        return apps
    
    def _scan_cli_tools(self):
        """Scan command line tools (limited for performance)"""
        apps = {}
        path_dirs = os.environ.get('PATH', '').split(':')
        
        # Limit to important directories
        important_dirs = [d for d in path_dirs if any(x in d for x in ['/usr/bin', '/bin', '/usr/local/bin'])]
        
        count = 0
        max_tools = 500  # Limit for performance
        
        for path_dir in important_dirs[:10]:
            if not os.path.exists(path_dir) or count >= max_tools:
                continue
                
            try:
                for file_path in Path(path_dir).iterdir():
                    if count >= max_tools:
                        break
                        
                    if (file_path.is_file() and 
                        os.access(file_path, os.X_OK) and
                        not file_path.name.startswith('.') and
                        len(file_path.name) > 2):
                        
                        name = file_path.name
                        apps[name] = {
                            'command': name,
                            'description': f'Command line tool',
                            'type': 'cli'
                        }
                        count += 1
            except Exception:
                continue
                
        return apps
    
    def _scan_snap_packages(self):
        """Scan snap packages"""
        apps = {}
        try:
            result = subprocess.run(['snap', 'list'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n')[1:]:
                    parts = line.split()
                    if len(parts) >= 1:
                        name = parts[0]
                        apps[f"{name} (Snap)"] = {
                            'command': name,
                            'description': f'Snap package',
                            'type': 'snap'
                        }
        except Exception:
            pass
        return apps
    
    def _scan_flatpak_packages(self):
        """Scan flatpak packages"""
        apps = {}
        try:
            result = subprocess.run(['flatpak', 'list', '--app'], 
                                  capture_output=True, text=True, timeout=5)
            if result.returncode == 0:
                for line in result.stdout.strip().split('\n'):
                    parts = line.split('\t')
                    if len(parts) >= 2:
                        name = parts[0]
                        app_id = parts[1]
                        apps[f"{name} (Flatpak)"] = {
                            'command': f'flatpak run {app_id}',
                            'description': f'Flatpak application',
                            'type': 'flatpak'
                        }
        except Exception:
            pass
        return apps
    
    def _categorize_apps(self, apps):
        """Categorize applications"""
        categorized = {cat: [] for cat in self.categories.keys()}
        categorized['Other'] = []
        
        icon_gen = SimpleIconGenerator()
        
        for name, info in apps.items():
            # Determine category
            category = self._get_category(name, info)
            
            # Get icon info
            icon_info = icon_gen.get_icon_info(name, category)
            
            app_entry = {
                'name': name,
                'command': info['command'],
                'description': info['description'],
                'type': info['type'],
                'icon_info': icon_info
            }
            
            categorized[category].append(app_entry)
        
        # Sort each category
        for category in categorized:
            categorized[category].sort(key=lambda x: x['name'].lower())
        
        return categorized
    
    def _get_category(self, name, info):
        """Determine app category"""
        text = f"{name.lower()} {info.get('description', '').lower()} {info.get('command', '').lower()}"
        
        category_scores = {}
        for category, keywords in self.categories.items():
            score = sum(1 for keyword in keywords if keyword in text)
            if score > 0:
                category_scores[category] = score
        
        if category_scores:
            return max(category_scores, key=category_scores.get)
        return 'Other'


class SimpleAppCard(QWidget):
    """🎨 Simple, beautiful app card"""
    
    clicked = pyqtSignal(dict)
    
    def __init__(self, app_data):
        super().__init__()
        self.app_data = app_data
        self.setup_ui()
    
    def setup_ui(self):
        self.setFixedSize(300, 80)
        self.setStyleSheet("""
            SimpleAppCard {
                background: rgba(255, 255, 255, 0.9);
                border: 2px solid rgba(0, 0, 0, 0.1);
                border-radius: 10px;
                margin: 4px;
            }
            SimpleAppCard:hover {
                background: rgba(33, 150, 243, 0.1);
                border: 2px solid #2196F3;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        layout.setSpacing(12)
        
        # Icon
        icon_label = QLabel()
        icon_label.setFixedSize(48, 48)
        icon_label.setAlignment(Qt.AlignCenter)
        
        # Use icon info
        icon_info = self.app_data.get('icon_info', {})
        emoji = icon_info.get('emoji', '📁')
        color = icon_info.get('color', '#9E9E9E')
        
        icon_label.setText(emoji)
        icon_label.setStyleSheet(f"""
            font-size: 24px;
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 {color}, stop: 1 {color}AA);
            border-radius: 8px;
            border: 1px solid {color};
            color: white;
        """)
        
        # Info
        info_widget = QWidget()
        info_layout = QVBoxLayout(info_widget)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(2)
        
        # Name
        name_label = QLabel(self.app_data['name'])
        name_label.setStyleSheet("font-weight: bold; color: #212529; font-size: 13px;")
        name_label.setWordWrap(True)
        
        # Description
        desc = self.app_data['description']
        if len(desc) > 45:
            desc = desc[:42] + '...'
        desc_label = QLabel(desc)
        desc_label.setStyleSheet("color: #6c757d; font-size: 11px;")
        desc_label.setWordWrap(True)
        
        # Type
        type_icons = {
            'desktop': '🖥️ Desktop',
            'cli': '⚡ CLI',
            'snap': '📦 Snap',
            'flatpak': '📦 Flatpak'
        }
        type_text = type_icons.get(self.app_data.get('type', 'unknown'), '📁 App')
        type_label = QLabel(type_text)
        type_label.setStyleSheet("color: #28a745; font-size: 10px; font-weight: bold;")
        
        info_layout.addWidget(name_label)
        info_layout.addWidget(desc_label)
        info_layout.addWidget(type_label)
        
        layout.addWidget(icon_label)
        layout.addWidget(info_widget)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.app_data)
    
    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
    
    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)


class SimpleBulletproofLauncher(QMainWindow):
    """🚀 Simple Bulletproof Launcher - Maximum Compatibility"""
    
    def __init__(self):
        super().__init__()
        self.detector = SmartAppDetector()
        self.all_apps = {}
        self.current_category = 'All'
        self.setup_ui()
        self.load_apps()
    
    def setup_ui(self):
        self.setWindowTitle("🚀 Enhanced Bulletproof Launcher")
        self.setMinimumSize(1000, 700)
        self.resize(1200, 800)
        
        # Simple, beautiful styling
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #667eea, stop: 1 #764ba2);
            }
        """)
        
        central = QWidget()
        self.setCentralWidget(central)
        
        layout = QHBoxLayout(central)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Sidebar
        self.create_sidebar(layout)
        
        # Content
        self.create_content(layout)
        
        # Status bar
        self.statusBar().setStyleSheet("""
            QStatusBar {
                background-color: rgba(0, 0, 0, 0.8);
                color: white;
                font-weight: bold;
            }
        """)
        self.statusBar().showMessage("🚀 Ready to launch applications!")
    
    def create_sidebar(self, main_layout):
        """Create sidebar"""
        sidebar = QWidget()
        sidebar.setFixedWidth(250)
        sidebar.setStyleSheet("""
            QWidget {
                background: rgba(44, 62, 80, 0.95);
                color: white;
            }
            QPushButton {
                background: rgba(52, 152, 219, 0.3);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 8px;
                color: white;
                font-weight: bold;
                padding: 10px;
                margin: 2px;
                text-align: left;
            }
            QPushButton:hover {
                background: rgba(52, 152, 219, 0.8);
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.setSpacing(8)
        
        # Title
        title = QLabel("🚀 BULLETPROOF")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(title)
        
        subtitle = QLabel("Enhanced Launcher")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 11px; color: #bdc3c7; margin-bottom: 20px;")
        layout.addWidget(subtitle)
        
        # Category buttons
        self.category_buttons = {}
        
        # All button
        all_btn = QPushButton("📋 All Applications")
        all_btn.clicked.connect(lambda: self.set_category('All'))
        self.category_buttons['All'] = all_btn
        layout.addWidget(all_btn)
        
        # Category buttons
        icons = {
            'Programming': '💻', 'Security': '🔒', 'System': '⚙️',
            'Internet': '🌐', 'Media': '🎬', 'Office': '📄',
            'Graphics': '🎨', 'Games': '🎮', 'Development': '🔧',
            'Education': '📚', 'Other': '📁'
        }
        
        for category in self.detector.categories.keys():
            icon = icons.get(category, '📁')
            btn = QPushButton(f"{icon} {category}")
            btn.clicked.connect(lambda checked, cat=category: self.set_category(cat))
            self.category_buttons[category] = btn
            layout.addWidget(btn)
        
        # Other button
        other_btn = QPushButton("📁 Other")
        other_btn.clicked.connect(lambda: self.set_category('Other'))
        self.category_buttons['Other'] = other_btn
        layout.addWidget(other_btn)
        
        layout.addStretch()
        
        # Stats
        self.stats_label = QLabel("📊 Loading...")
        self.stats_label.setStyleSheet("""
            background: rgba(46, 204, 113, 0.2);
            border: 1px solid #2ecc71;
            border-radius: 6px;
            padding: 8px;
            font-size: 11px;
        """)
        self.stats_label.setWordWrap(True)
        layout.addWidget(self.stats_label)
        
        main_layout.addWidget(sidebar)
    
    def create_content(self, main_layout):
        """Create content area"""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Header
        header = QHBoxLayout()
        
        # Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Search applications...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background: rgba(255, 255, 255, 0.95);
                border: 2px solid #3498db;
                border-radius: 10px;
                font-size: 14px;
                padding: 10px 15px;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
                background: white;
            }
        """)
        self.search_input.textChanged.connect(self.filter_apps)
        
        # Refresh
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background: #27ae60;
                border: none;
                border-radius: 8px;
                color: white;
                font-weight: bold;
                padding: 10px 15px;
            }
            QPushButton:hover {
                background: #2ecc71;
            }
        """)
        refresh_btn.clicked.connect(self.load_apps)
        
        header.addWidget(self.search_input)
        header.addWidget(refresh_btn)
        layout.addLayout(header)
        
        # Category title
        self.category_title = QLabel("📋 All Applications")
        self.category_title.setStyleSheet("""
            background: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 8px;
        """)
        layout.addWidget(self.category_title)
        
        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("""
            QScrollArea {
                background: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 4px;
                width: 8px;
            }
            QScrollBar::handle:vertical {
                background: #3498db;
                border-radius: 4px;
            }
        """)
        
        # Apps widget
        self.apps_widget = QWidget()
        self.apps_layout = QVBoxLayout(self.apps_widget)
        self.apps_layout.setSpacing(8)
        self.apps_layout.setContentsMargins(5, 5, 5, 5)
        
        scroll.setWidget(self.apps_widget)
        layout.addWidget(scroll)
        
        main_layout.addWidget(content)
    
    def load_apps(self):
        """Load applications"""
        self.search_input.setEnabled(False)
        self.search_input.setPlaceholderText("🔄 Loading applications...")
        self.statusBar().showMessage("🔍 Scanning for applications...")
        
        # Use QTimer to keep UI responsive
        QTimer.singleShot(100, self._do_load_apps)
    
    def _do_load_apps(self):
        """Actually load the apps"""
        try:
            self.all_apps = self.detector.scan_applications()
            
            # Update stats
            total = sum(len(apps) for apps in self.all_apps.values())
            categories = len([cat for cat, apps in self.all_apps.items() if apps])
            
            stats_text = f"""📊 Statistics:
• {total} Applications
• {categories} Categories

🔥 Top Categories:"""
            
            # Top categories
            cat_counts = [(cat, len(apps)) for cat, apps in self.all_apps.items() if apps]
            cat_counts.sort(key=lambda x: x[1], reverse=True)
            
            for cat, count in cat_counts[:4]:
                stats_text += f"\n• {cat}: {count}"
            
            self.stats_label.setText(stats_text)
            
            self.search_input.setEnabled(True)
            self.search_input.setPlaceholderText("🔍 Search applications...")
            self.statusBar().showMessage(f"🚀 Ready! Found {total} applications")
            
            # Show all apps
            self.set_category('All')
            
        except Exception as e:
            self.statusBar().showMessage(f"❌ Error loading apps: {e}")
            self.search_input.setEnabled(True)
    
    def set_category(self, category):
        """Set active category"""
        self.current_category = category
        
        # Update button styles
        for cat, btn in self.category_buttons.items():
            if cat == category:
                btn.setStyleSheet("""
                    QPushButton {
                        background: #3498db;
                        border: 2px solid #2980b9;
                        border-radius: 8px;
                        color: white;
                        font-weight: bold;
                        padding: 10px;
                        margin: 2px;
                        text-align: left;
                    }
                """)
            else:
                btn.setStyleSheet("")
        
        # Update title
        icons = {
            'All': '📋', 'Programming': '💻', 'Security': '🔒',
            'System': '⚙️', 'Internet': '🌐', 'Media': '🎬',
            'Office': '📄', 'Graphics': '🎨', 'Games': '🎮',
            'Development': '🔧', 'Education': '📚', 'Other': '📁'
        }
        icon = icons.get(category, '📁')
        
        if category == 'All':
            total = sum(len(apps) for apps in self.all_apps.values())
            self.category_title.setText(f"{icon} All Applications ({total})")
        else:
            count = len(self.all_apps.get(category, []))
            self.category_title.setText(f"{icon} {category} ({count})")
        
        self.filter_apps()
    
    def filter_apps(self):
        """Filter and display apps"""
        search_text = self.search_input.text().lower().strip()
        
        # Get apps for current category
        if self.current_category == 'All':
            apps = []
            for app_list in self.all_apps.values():
                apps.extend(app_list)
        else:
            apps = self.all_apps.get(self.current_category, [])
        
        # Filter by search
        if search_text:
            filtered = []
            for app in apps:
                if (search_text in app['name'].lower() or
                    search_text in app['description'].lower() or
                    search_text in app['command'].lower()):
                    filtered.append(app)
            apps = filtered
        
        self.display_apps(apps)
    
    def display_apps(self, apps):
        """Display apps in grid"""
        # Clear previous
        for i in reversed(range(self.apps_layout.count())):
            child = self.apps_layout.itemAt(i).widget()
            if child:
                child.setParent(None)
        
        if not apps:
            empty = QLabel("😔 No applications found!")
            empty.setAlignment(Qt.AlignCenter)
            empty.setStyleSheet("font-size: 16px; color: rgba(255, 255, 255, 0.7); padding: 50px;")
            self.apps_layout.addWidget(empty)
            return
        
        # Create grid (3 per row)
        apps_per_row = 3
        for i in range(0, len(apps), apps_per_row):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(10)
            
            for j in range(apps_per_row):
                if i + j < len(apps):
                    app = apps[i + j]
                    card = SimpleAppCard(app)
                    card.clicked.connect(self.launch_app)
                    row_layout.addWidget(card)
                else:
                    row_layout.addStretch()
            
            self.apps_layout.addWidget(row_widget)
        
        self.apps_layout.addStretch()
        self.statusBar().showMessage(f"📋 Showing {len(apps)} applications")
    
    def launch_app(self, app_data):
        """Launch an application"""
        command = app_data.get('command', '')
        name = app_data.get('name', 'Unknown')
        app_type = app_data.get('type', 'unknown')
        
        if not command:
            QMessageBox.warning(self, "Error", f"No command for {name}")
            return
        
        try:
            if app_type == 'flatpak':
                subprocess.Popen(command.split(),
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            elif app_type == 'snap':
                subprocess.Popen(['snap', 'run', command],
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            else:
                subprocess.Popen(command, shell=True,
                               stdout=subprocess.DEVNULL,
                               stderr=subprocess.DEVNULL)
            
            self.statusBar().showMessage(f"🚀 Launched: {name}", 3000)
            
        except Exception as e:
            QMessageBox.critical(self, "Launch Error", f"Failed to launch {name}:\n{str(e)}")


def main():
    """Main function"""
    app = QApplication(sys.argv)
    app.setApplicationName("Enhanced Bulletproof Launcher")
    app.setApplicationVersion("3.0")
    
    # Set icon if available
    icon_path = Path(__file__).parent / "bulletproof_launcher_icon_64.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    
    launcher = SimpleBulletproofLauncher()
    launcher.show()
    
    # Center window
    screen = app.primaryScreen().geometry()
    launcher.move(
        (screen.width() - launcher.width()) // 2,
        (screen.height() - launcher.height()) // 2
    )
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
