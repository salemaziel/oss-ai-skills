# OSS Rust Systems & TUI (`oss-rust-stack`)

> Idiomatic Rust systems engineering, high-performance terminal user interfaces with Ratatui, and structural AST code refactoring.

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
| **rust-core** | > Use when writing, reviewing, or refactoring Rust code. Covers ownership, borrowing, error handling, async patterns, API design, memory optimization, performance, testing, and common anti-patterns. Targets Rust 1.80+ and Edition 2024. Invoke with /rust-core. | [`skills/rust-core/SKILL.md`](skills/rust-core/SKILL.md) |
| **ratatui** | "Use when building terminal user interfaces in Rust with the ratatui crate - layout system, widget usage, input/event handling, app state architecture, TUI testing, or migrating between ratatui 0.29 and 0.30" | [`skills/ratatui/SKILL.md`](skills/ratatui/SKILL.md) |
| **ast-grep** | Use when doing structural code search and rewriting - ast-grep linting, refactoring, multi-language patterns | [`skills/ast-grep/SKILL.md`](skills/ast-grep/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-rust-stack@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-rust-stack
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-rust-stack@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-rust-stack ~/.codex/plugins/oss-rust-stack
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-rust-stack
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-rust-stack
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-rust-stack ~/.gemini/config/plugins/oss-rust-stack
```

## Starter Prompts

- `"Use oss-rust-stack to build an interactive terminal UI with Ratatui."`
- `"Use oss-rust-stack to refactor Rust async code for maximum performance."`
- `"Use oss-rust-stack to perform AST pattern search and rewriting."`
