# OSS Qt Desktop & GUI Suite (`oss-qt-desktop`)

> Cross-platform GUI development with Qt in Python (PyQt6/PySide6) and C++, plus KDE Plasma widgets and Kate editor extensions.

- **Version**: 1.0.0
- **License**: GPL-3.0
- **Repository**: [https://github.com/salemaziel/oss-ai-skills](https://github.com/salemaziel/oss-ai-skills)

## Compatibility

This plugin is natively compatible with:
- 🟣 **Claude Code** (`.claude-plugin/plugin.json`)
- 🟢 **OpenAI Codex CLI** (`.codex-plugin/plugin.json`)
- 🔵 **Google Antigravity CLI (`agy`)** (`plugin.json`)

## Bundled Skills

| Skill | Trigger / Description | Entry Point |
|---|---|---|
| **pyqt** | Use when building cross-platform desktop apps with PyQt6 or PySide6 - hub for installation, project structure, signals and slots basics, and pointers to widgets, styling, dialogs, threading, and testing sub-skills | [`skills/pyqt/SKILL.md`](skills/pyqt/SKILL.md) |
| **pyqt-core** | Use when working with PyQt/PySide6 QtCore - signals, slots, properties, timers, settings, file I/O | [`skills/pyqt-core/SKILL.md`](skills/pyqt-core/SKILL.md) |
| **pyqt-widgets** | Use when building PyQt/PySide6 UIs with QtWidgets - display, input and container widgets, buttons, item views like QListWidget and QTableWidget, layout management, or event handling (mouse/keyboard events, event filters, shortcuts) | [`skills/pyqt-widgets/SKILL.md`](skills/pyqt-widgets/SKILL.md) |
| **pyqt-dialogs** | Use when implementing PyQt/PySide6 dialogs - standard dialogs (QFileDialog, QMessageBox, QInputDialog, QColorDialog, QFontDialog), custom QDialog patterns, modal vs modeless dialogs, input validation, Qt 6 dialog APIs | [`skills/pyqt-dialogs/SKILL.md`](skills/pyqt-dialogs/SKILL.md) |
| **pyqt-styling** | "Use when styling PyQt/PySide6 widgets with QSS - selectors and pseudo-states, stylesheet application, common style properties, widget-specific styling, or building a dark theme" | [`skills/pyqt-styling/SKILL.md`](skills/pyqt-styling/SKILL.md) |
| **pyqt-threading** | Use when handling PyQt/PySide6 threading - QThread patterns, QThreadPool/QRunnable, thread safety rules, moveToThread, Qt Concurrent, QTimer, testing threaded code, lifecycle management | [`skills/pyqt-threading/SKILL.md`](skills/pyqt-threading/SKILL.md) |
| **pyqt-multimedia** | "Use when adding multimedia to PyQt/PySide6 apps - audio and video playback with QMediaPlayer, camera capture with QCamera and QMediaCaptureSession, audio/video recording with QMediaRecorder, GStreamer backend setup, or codec and platform compatibility issues" | [`skills/pyqt-multimedia/SKILL.md`](skills/pyqt-multimedia/SKILL.md) |
| **pyqt-testing** | Use when testing PyQt/PySide6 applications with pytest-qt - qtbot fixture, signal/wait patterns, mouse/keyboard simulation, dialog testing, model/view testing, threaded code testing, or manual debugging techniques | [`skills/pyqt-testing/SKILL.md`](skills/pyqt-testing/SKILL.md) |
| **qt-cpp** | Use when developing desktop applications with Qt in C++ - CMake setup, signals and slots, QThread and QtConcurrent, QML integration, model/view programming, Qt5 to Qt6 migration, or windeployqt/macdeployqt/linuxdeployqt deployment | [`skills/qt-cpp/SKILL.md`](skills/qt-cpp/SKILL.md) |
| **kde-plasmoid** | Use when building KDE Plasma 6 widgets with a Python backend - plasmoid structure, metadata.json, QML UI, configuration system, plasmapkg2 packaging, KDE Store submission, or plasmoid testing and debugging | [`skills/kde-plasmoid/SKILL.md`](skills/kde-plasmoid/SKILL.md) |
| **kate-plugin** | Use when developing C++ plugins for Kate - KTextEditor Framework, CMake/ECM, Qt threading, KDE plugin architecture | [`skills/kate-plugin/SKILL.md`](skills/kate-plugin/SKILL.md) |
| **pytest** | Use when writing Python tests with pytest - fixtures, parametrization, markers, conftest layout, pytest-asyncio, pytest-django, coverage with pytest-cov, mocking with pytest-mock, parallel runs with xdist, or CI integration | [`skills/pytest/SKILL.md`](skills/pytest/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-qt-desktop@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-qt-desktop
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-qt-desktop@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-qt-desktop ~/.codex/plugins/oss-qt-desktop
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-qt-desktop
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-qt-desktop
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-qt-desktop ~/.gemini/config/plugins/oss-qt-desktop
```

## Starter Prompts

- `"Use oss-qt-desktop to build a desktop GUI application using PyQt6 widgets and QSS styling."`
- `"Use oss-qt-desktop to manage worker threads with QThread and QThreadPool."`
- `"Use oss-qt-desktop to develop a KDE Plasma 6 widget or Kate plugin."`
