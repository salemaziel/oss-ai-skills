# OSS Linux Desktop & System Tools (`oss-linux-desktop-tools`)

> Linux desktop utilities, Waydroid Android container integration, KDE Plasma 6 desktop widgets, and local Redis caching.

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
| **waydroid** | Use when setting up or troubleshooting Waydroid on Linux - installation and initialization, waydroid CLI, GPU and networking setup, GApps and Play certification, ADB integration, file sharing, or desktop environment integration | [`skills/waydroid/SKILL.md`](skills/waydroid/SKILL.md) |
| **kde-plasmoid** | Use when building KDE Plasma 6 widgets with a Python backend - plasmoid structure, metadata.json, QML UI, configuration system, plasmapkg2 packaging, KDE Store submission, or plasmoid testing and debugging | [`skills/kde-plasmoid/SKILL.md`](skills/kde-plasmoid/SKILL.md) |
| **redis** | Use when working with Redis - in-memory database, caching, pub/sub, sessions, rate limiting, RESP3, asyncio, Redis Stack | [`skills/redis/SKILL.md`](skills/redis/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-linux-desktop-tools@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-linux-desktop-tools
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-linux-desktop-tools@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-linux-desktop-tools ~/.codex/plugins/oss-linux-desktop-tools
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-linux-desktop-tools
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-linux-desktop-tools
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-linux-desktop-tools ~/.gemini/config/plugins/oss-linux-desktop-tools
```

## Starter Prompts

- `"Use oss-linux-desktop-tools to set up and troubleshoot Waydroid on Linux with GPU acceleration."`
- `"Use oss-linux-desktop-tools to build a KDE Plasma 6 widget with Python backend."`
- `"Use oss-linux-desktop-tools to configure local Redis for desktop caching and IPC."`
