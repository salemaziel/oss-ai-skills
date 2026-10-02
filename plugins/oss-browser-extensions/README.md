# OSS Mozilla Browser & Mail Extensions (`oss-browser-extensions`)

> Browser and mail extension development for Firefox WebExtensions and Thunderbird MailExtensions with E2E visual regression testing.

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
| **firefox-extension** | Use when developing Firefox WebExtensions - Manifest V2/V3 configuration, WebExtension APIs, content security policy, web-ext CLI, cross-browser support with the polyfill, AMO submission, or debugging extensions | [`skills/firefox-extension/SKILL.md`](skills/firefox-extension/SKILL.md) |
| **thunderbird-extension** | Use when developing Thunderbird MailExtensions - Manifest V2/V3 configuration, messenger.* APIs for accounts, messages, folders and compose, UI actions, message display scripts, Experiment APIs, ATN submission, or migration from legacy extensions | [`skills/thunderbird-extension/SKILL.md`](skills/thunderbird-extension/SKILL.md) |
| **playwright-visual-regression** | Use when setting up visual regression testing with Playwright - toHaveScreenshot baselines, masking dynamic content, handling animations, full-page and element screenshots, cross-browser runs, CI integration, VUDA MCP tooling, or debugging flaky visual diffs | [`skills/playwright-visual-regression/SKILL.md`](skills/playwright-visual-regression/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-browser-extensions@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-browser-extensions
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-browser-extensions@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-browser-extensions ~/.codex/plugins/oss-browser-extensions
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-browser-extensions
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-browser-extensions
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-browser-extensions ~/.gemini/config/plugins/oss-browser-extensions
```

## Starter Prompts

- `"Use oss-browser-extensions to create a Manifest V3 Firefox WebExtension with web-ext."`
- `"Use oss-browser-extensions to implement a Thunderbird mail extension using messenger.* APIs."`
- `"Use oss-browser-extensions to write Playwright visual regression tests for extension popups."`
