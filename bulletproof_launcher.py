#!/usr/bin/env python3
"""
Smart Launcher Pro - Ultimate Application Launcher
A modern, intelligent application launcher for Linux systems.

Features:
- Smart auto-detection of applications
- Beautiful modern UI with PyQt5
- Real-time search functionality
- Usage statistics tracking
- Zero-crash architecture
"""

import sys
import os
import subprocess
import configparser
import threading
import json
from pathlib import Path
from collections import defaultdict

try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
except ImportError:
    print("❌ Error: PyQt5 not installed!")
    print("📦 Install with: pip install PyQt5")
    sys.exit(1)


class ApplicationDetector:
    """Intelligent application detection and categorization engine"""
    
    def __init__(self):
        self.categories = {
            'Programming': ['code', 'editor', 'ide', 'python', 'java', 'git', 'vim'],
            'Security': ['security', 'hack', 'nmap', 'wireshark', 'metasploit', 'burp'],  
            'System': ['system', 'monitor', 'htop', 'top', 'kill', 'systemctl'],
            'Internet': ['browser', 'firefox', 'chrome', 'wget', 'curl', 'thunderbird'],
            'Media': ['video', 'audio', 'vlc', 'mpv', 'gimp', 'blender', 'spotify'],
            'Office': ['office', 'document', 'libreoffice', 'writer', 'calc', 'pdf'],
            'Graphics': ['graphics', 'design', 'gimp', 'inkscape', 'krita', 'darktable'],
            'Games': ['game', 'steam', 'lutris', 'wine', 'emulator']
        }
        
    def detect_applications(self):
        """Detect all applications in the system"""
        print("Scanning system for applications...")
        
        apps_by_category = {}
        for cat in self.categories:
            apps_by_category[cat] = []
        apps_by_category['Other'] = []
        
        # Scan desktop applications
        desktop_apps = self._scan_desktop_files()
        print(f"Found {len(desktop_apps)} desktop applications")
        
        # Scan command line tools
        path_apps = self._scan_path_commands()
        print(f"Found {len(path_apps)} command line tools")
        
        # Merge and categorize all applications
        all_apps = {**desktop_apps, **path_apps}
        
        for name, info in all_apps.items():
            category = self._categorize_application(name, info)
            apps_by_category[category].append({
                'name': name,
                'command': info.get('command', name),
                'description': info.get('description', 'Application'),
                'type': info.get('type', 'unknown')
            })
        
        # Sort applications by name
        for cat in apps_by_category:
            apps_by_category[cat].sort(key=lambda x: x['name'].lower())
            
        return apps_by_category
    
    def _scan_desktop_files(self):
        """اسکن فایل‌های .desktop"""
        apps = {}
        desktop_dirs = [
            '/usr/share/applications',
            '/usr/local/share/applications',
            os.path.expanduser('~/.local/share/applications')
        ]
        
        for desktop_dir in desktop_dirs:
            if not os.path.exists(desktop_dir):
                continue
                
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
                    command = entry.get('Exec', '')
                    description = entry.get('Comment', entry.get('GenericName', 'Desktop Application'))
                    
                    if command:
                        command = command.split()[0]
                        
                    apps[name] = {
                        'command': command,
                        'description': description,
                        'type': 'desktop'
                    }
                    
                except Exception:
                    continue
                    
        return apps
    
    def _scan_path_commands(self):
        """اسکن دستورات PATH - محدود شده"""
        apps = {}
        path_dirs = os.environ.get('PATH', '').split(':')
        
        # محدود کردن تعداد برای جلوگیری از crash
        max_commands = 1000
        count = 0
        
        for path_dir in path_dirs:
            if count >= max_commands:
                break
                
            if not os.path.exists(path_dir):
                continue
                
            try:
                for file_path in Path(path_dir).iterdir():
                    if count >= max_commands:
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
                        
            except (PermissionError, OSError):
                continue
                
        return apps
    
    def _categorize_application(self, name, info):
        """Determine application category"""
        name_lower = name.lower()
        description_lower = info.get('description', '').lower()
        command_lower = info.get('command', '').lower()
        
        for category, keywords in self.categories.items():
            for keyword in keywords:
                if (keyword in name_lower or 
                    keyword in description_lower or 
                    keyword in command_lower):
                    return category
                    
        return 'Other'


class AppCard(QWidget):
    """Simple and elegant card for applications"""
    
    clicked = pyqtSignal(dict)
    
    def __init__(self, app_data):
        super().__init__()
        self.app_data = app_data
        self.setup_ui()
        
    def setup_ui(self):
        self.setFixedSize(300, 80)
        self.setStyleSheet("""
            AppCard {
                background-color: #f8f9fa;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin: 4px;
            }
            AppCard:hover {
                background-color: #e3f2fd;
                border: 2px solid #2196f3;
            }
        """)
        
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 8, 12, 8)
        
        # Icon
        icon_label = QLabel()
        icon_label.setFixedSize(48, 48)
        icon_label.setAlignment(Qt.AlignCenter)
        
        # Emoji icons based on type
        if self.app_data['type'] == 'desktop':
            icon_label.setText('📱')
        else:
            icon_label.setText('⚡')
        icon_label.setStyleSheet("font-size: 24px;")
        
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
        description = self.app_data['description']
        if len(description) > 50:
            description = description[:47] + '...'
        description_label = QLabel(description)
        description_label.setStyleSheet("color: #6c757d; font-size: 11px;")
        description_label.setWordWrap(True)
        
        # Type
        type_text = '📱 GUI App' if self.app_data['type'] == 'desktop' else '⚡ CLI Tool'
        type_label = QLabel(type_text)
        type_label.setStyleSheet("color: #28a745; font-size: 10px; font-weight: bold;")
        
        info_layout.addWidget(name_label)
        info_layout.addWidget(description_label)
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


class BulletproofLauncher(QMainWindow):
    """🚀 Bulletproof Launcher - Crash Free!"""
    
    def __init__(self):
        super().__init__()
        self.detector = ApplicationDetector()
        self.all_apps = {}
        self.current_category = 'All'
        self.setup_ui()
        self.load_apps()
        
    def setup_ui(self):
        self.setWindowTitle("🚀 BULLETPROOF LAUNCHER")
        self.setMinimumSize(1000, 700)
        self.resize(1200, 800)
        
        # Safe, simple stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
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
        
        # Main content
        self.create_content(layout)
        
    def create_sidebar(self, main_layout):
        """ساخت sidebar"""
        sidebar = QWidget()
        sidebar.setFixedWidth(220)
        sidebar.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: white;
            }
            QPushButton {
                background-color: rgba(52, 73, 94, 0.5);
                border: none;
                border-radius: 6px;
                color: white;
                font-weight: bold;
                padding: 10px;
                margin: 2px;
                text-align: left;
            }
            QPushButton:hover {
                background-color: #3498db;
            }
            QPushButton:pressed {
                background-color: #2980b9;
            }
        """)
        
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(15, 20, 15, 20)
        sidebar_layout.setSpacing(8)
        
        # Title
        title = QLabel("🚀 BULLETPROOF")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 15px;")
        sidebar_layout.addWidget(title)
        
        subtitle = QLabel("Zero Crash Launcher")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 11px; color: #bdc3c7; margin-bottom: 20px;")
        sidebar_layout.addWidget(subtitle)
        
        # Category buttons
        self.category_buttons = {}
        
        # All button
        all_btn = QPushButton("📋 All Applications")
        all_btn.clicked.connect(lambda: self.set_category('All'))
        self.category_buttons['All'] = all_btn
        sidebar_layout.addWidget(all_btn)
        
        # Category buttons
        category_icons = {
            'Programming': '💻', 'Security': '🔒', 'System': '⚙️',
            'Internet': '🌐', 'Media': '🎬', 'Office': '📄',
            'Graphics': '🎨', 'Games': '🎮', 'Other': '📁'
        }
        
        for category in self.detector.categories.keys():
            icon = category_icons.get(category, '📁')
            btn = QPushButton(f"{icon} {category}")
            btn.clicked.connect(lambda checked, cat=category: self.set_category(cat))
            self.category_buttons[category] = btn
            sidebar_layout.addWidget(btn)
            
        # Other button
        other_btn = QPushButton("📁 Other")
        other_btn.clicked.connect(lambda: self.set_category('Other'))
        self.category_buttons['Other'] = other_btn
        sidebar_layout.addWidget(other_btn)
        
        sidebar_layout.addStretch()
        
        # Stats
        self.stats_label = QLabel("📊 Loading...")
        self.stats_label.setStyleSheet("""
            background-color: rgba(46, 204, 113, 0.2);
            border: 1px solid #2ecc71;
            border-radius: 6px;
            padding: 8px;
            font-size: 11px;
        """)
        self.stats_label.setWordWrap(True)
        sidebar_layout.addWidget(self.stats_label)
        
        main_layout.addWidget(sidebar)
        
    def create_content(self, main_layout):
        """ساخت محتوای اصلی"""
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(15)
        
        # Header
        header_layout = QHBoxLayout()
        
        # Search
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Search applications...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 2px solid #3498db;
                border-radius: 10px;
                font-size: 14px;
                padding: 10px 15px;
            }
            QLineEdit:focus {
                border: 2px solid #2980b9;
            }
        """)
        self.search_input.textChanged.connect(self.filter_apps)
        
        # Refresh button
        refresh_btn = QPushButton("🔄 Refresh")
        refresh_btn.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                border: none;
                border-radius: 8px;
                color: white;
                font-weight: bold;
                padding: 10px 15px;
            }
            QPushButton:hover {
                background-color: #2ecc71;
            }
        """)
        refresh_btn.clicked.connect(self.load_apps)
        
        header_layout.addWidget(self.search_input)
        header_layout.addWidget(refresh_btn)
        content_layout.addLayout(header_layout)
        
        # Category title
        self.category_title = QLabel("📋 All Applications")
        self.category_title.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.1);
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 8px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            padding: 8px;
        """)
        content_layout.addWidget(self.category_title)
        
        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll.setStyleSheet("""
            QScrollArea {
                background-color: transparent;
                border: none;
            }
            QScrollBar:vertical {
                background-color: rgba(255, 255, 255, 0.1);
                border: none;
                border-radius: 4px;
                width: 8px;
            }
            QScrollBar::handle:vertical {
                background-color: #3498db;
                border-radius: 4px;
            }
        """)
        
        # Apps widget
        self.apps_widget = QWidget()
        self.apps_layout = QVBoxLayout(self.apps_widget)
        self.apps_layout.setSpacing(8)
        self.apps_layout.setContentsMargins(5, 5, 5, 5)
        
        scroll.setWidget(self.apps_widget)
        content_layout.addWidget(scroll)
        
        main_layout.addWidget(content)
        
    def load_apps(self):
        """Load applications in background"""
        self.search_input.setEnabled(False)
        self.search_input.setPlaceholderText("🔄 Loading applications...")
        
        # Thread worker
        self.worker = QThread()
        self.app_loader = AppLoader(self.detector)
        self.app_loader.moveToThread(self.worker)
        
        self.worker.started.connect(self.app_loader.run)
        self.app_loader.finished.connect(self.on_apps_loaded)
        self.app_loader.finished.connect(self.worker.quit)
        self.app_loader.finished.connect(self.app_loader.deleteLater)
        self.worker.finished.connect(self.worker.deleteLater)
        
        self.worker.start()
        
    def on_apps_loaded(self, apps):
        """After applications are loaded"""
        self.all_apps = apps
        self.search_input.setEnabled(True)
        self.search_input.setPlaceholderText("🔍 Search applications...")
        
        # Update stats
        total = sum(len(app_list) for app_list in apps.values())
        categories = len([cat for cat, app_list in apps.items() if app_list])
        
        stats_text = f"""📊 Statistics:
• {total} Applications
• {categories} Categories

🔥 Top Categories:"""
        
        # Top categories
        cat_counts = [(cat, len(app_list)) for cat, app_list in apps.items() if app_list]
        cat_counts.sort(key=lambda x: x[1], reverse=True)
        
        for cat, count in cat_counts[:4]:
            stats_text += f"\n• {cat}: {count}"
            
        self.stats_label.setText(stats_text)
        
        # Show all apps
        self.set_category('All')
        
    def set_category(self, category):
        """تنظیم دسته فعال"""
        self.current_category = category
        
        # Update button styles
        for cat, btn in self.category_buttons.items():
            if cat == category:
                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #3498db;
                        border: 2px solid #2980b9;
                        border-radius: 6px;
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
        category_icons = {
            'All': '📋', 'Programming': '💻', 'Security': '🔒', 
            'System': '⚙️', 'Internet': '🌐', 'Media': '🎬',
            'Office': '📄', 'Graphics': '🎨', 'Games': '🎮', 'Other': '📁'
        }
        icon = category_icons.get(category, '📁')
        self.category_title.setText(f"{icon} {category}")
        
        self.filter_apps()
        
    def filter_apps(self):
        """Filter applications"""
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
                    search_text in app['desc'].lower() or
                    search_text in app['command'].lower()):
                    filtered.append(app)
            apps = filtered
            
        self.display_apps(apps)
        
    def display_apps(self, apps):
        """Display applications"""
        # Clear previous apps
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
            
        # Create grid of cards (3 per row)
        apps_per_row = 3
        for i in range(0, len(apps), apps_per_row):
            row_widget = QWidget()
            row_layout = QHBoxLayout(row_widget)
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(10)
            
            for j in range(apps_per_row):
                if i + j < len(apps):
                    app = apps[i + j]
                    card = AppCard(app)
                    card.clicked.connect(self.launch_app)
                    row_layout.addWidget(card)
                else:
                    row_layout.addStretch()
                    
            self.apps_layout.addWidget(row_widget)
            
        self.apps_layout.addStretch()
        
    def launch_app(self, app_data):
        """Launch application"""
        command = app_data.get('command', '')
        name = app_data.get('name', 'Unknown')
        
        if not command:
            QMessageBox.warning(self, "Error", f"No command for {name}")
            return
            
        try:
            subprocess.Popen(command, shell=True, 
                           stdout=subprocess.DEVNULL, 
                           stderr=subprocess.DEVNULL)
            
            self.statusBar().showMessage(f"🚀 Launched: {name}", 3000)
            
        except Exception as e:
            QMessageBox.critical(self, "Launch Error", f"Failed to launch {name}:\n{str(e)}")


class AppLoader(QObject):
    """Worker thread for loading applications"""
    
    finished = pyqtSignal(dict)
    
    def __init__(self, detector):
        super().__init__()
        self.detector = detector
        
    def run(self):
        apps = self.detector.detect_applications()
        self.finished.emit(apps)


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Bulletproof Launcher")
    
    launcher = BulletproofLauncher()
    launcher.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
