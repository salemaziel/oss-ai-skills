# OSS Desktop App Extensibility & Modding (`oss-app-extensibility`)

> Scripting and extending open-source desktop software: GIMP 3.0+ Python plugins, Kate editor C++ plugins, OpenRCT2 game mods, and OpenCode tools.

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
| **gimp-plugin** | Use when developing GIMP 3.0+ plugins in Python 3 - procedure registration, image and layer operations, GEGL operations, PDB calls, dialogs and progress bars, file export, or batch processing plugins | [`skills/gimp-plugin/SKILL.md`](skills/gimp-plugin/SKILL.md) |
| **kate-plugin** | Use when developing C++ plugins for Kate - KTextEditor Framework, CMake/ECM, Qt threading, KDE plugin architecture | [`skills/kate-plugin/SKILL.md`](skills/kate-plugin/SKILL.md) |
| **openrct2** | Use when developing OpenRCT2 plugins in TypeScript - plugin registration and game actions, window and widget UI, event hooks, park, map, ride and entity access, network API, storage, or ES5 runtime constraints | [`skills/openrct2/SKILL.md`](skills/openrct2/SKILL.md) |
| **opencode** | Use when developing plugins, tools, and extensions for OpenCode v1 - plugin contract, crash-prevention rules, ctx/event APIs, subagent lifecycle (abort races, compaction, orphan detection), MCP integration, testing patterns, or publishing to npm | [`skills/opencode/SKILL.md`](skills/opencode/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-app-extensibility@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-app-extensibility
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-app-extensibility@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-app-extensibility ~/.codex/plugins/oss-app-extensibility
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-app-extensibility
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-app-extensibility
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-app-extensibility ~/.gemini/config/plugins/oss-app-extensibility
```

## Starter Prompts

- `"Use oss-app-extensibility to develop a GIMP 3.0 Python plugin using GEGL procedures."`
- `"Use oss-app-extensibility to create a Kate text editor plugin in C++."`
- `"Use oss-app-extensibility to build an OpenRCT2 game mod in TypeScript."`
