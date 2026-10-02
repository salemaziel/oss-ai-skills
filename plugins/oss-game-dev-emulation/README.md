# OSS Game Dev & Modding (`oss-game-dev-emulation`)

> 2D game development in Python (pygame), GBA Lua game engine, mGBA emulator automation, and OpenRCT2 modding.

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
| **pygame** | Use when building 2D games in Python with pygame - game loop and delta time, sprites and groups, collision detection, drawing and surfaces, events and input, sound and fonts, camera, or performance optimization | [`skills/pygame/SKILL.md`](skills/pygame/SKILL.md) |
| **bpcore-engine** | Use when building GBA games with the BPCore Lua engine - entity, sprite and tilemap functions, SRAM save and load, link cable multiplayer protocol, camera and scrolling, or optimization patterns | [`skills/bpcore-engine/SKILL.md`](skills/bpcore-engine/SKILL.md) |
| **mgba** | Use when scripting mGBA emulator automation in Lua - console API, ROM and save state operations, frame callbacks, input handling, memory reading for cheats and RAM watches, sockets, or TAS and speedrunner tooling | [`skills/mgba/SKILL.md`](skills/mgba/SKILL.md) |
| **openrct2** | Use when developing OpenRCT2 plugins in TypeScript - plugin registration and game actions, window and widget UI, event hooks, park, map, ride and entity access, network API, storage, or ES5 runtime constraints | [`skills/openrct2/SKILL.md`](skills/openrct2/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-game-dev-emulation@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-game-dev-emulation
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-game-dev-emulation@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-game-dev-emulation ~/.codex/plugins/oss-game-dev-emulation
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-game-dev-emulation
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-game-dev-emulation
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-game-dev-emulation ~/.gemini/config/plugins/oss-game-dev-emulation
```

## Starter Prompts

- `"Use oss-game-dev-emulation to build a 2D game loop with sprite collision in pygame."`
- `"Use oss-game-dev-emulation to script mGBA emulator automation and RAM watching in Lua."`
- `"Use oss-game-dev-emulation to create OpenRCT2 game action plugins in TypeScript."`
