# OSS Web Frontend & Visual QA (`oss-web-frontend-testing`)

> Web UI engineering with Tailwind CSS v4, visual regression testing with Playwright, dynamic reactive server UI with HTMX, and AST linting.

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
| **tailwind** | Use when styling with Tailwind CSS v4 - @theme syntax, design token architecture, dark mode strategy, bundle size optimization, component-layer discipline, or migrating from v3 | [`skills/tailwind/SKILL.md`](skills/tailwind/SKILL.md) |
| **playwright-visual-regression** | Use when setting up visual regression testing with Playwright - toHaveScreenshot baselines, masking dynamic content, handling animations, full-page and element screenshots, cross-browser runs, CI integration, VUDA MCP tooling, or debugging flaky visual diffs | [`skills/playwright-visual-regression/SKILL.md`](skills/playwright-visual-regression/SKILL.md) |
| **django-htmx** | Use when building dynamic Django web apps with htmx - partial rendering, HTMX responses, querystring tag, CSP | [`skills/django-htmx/SKILL.md`](skills/django-htmx/SKILL.md) |
| **ast-grep** | Use when doing structural code search and rewriting - ast-grep linting, refactoring, multi-language patterns | [`skills/ast-grep/SKILL.md`](skills/ast-grep/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-web-frontend-testing@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-web-frontend-testing
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-web-frontend-testing@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-web-frontend-testing ~/.codex/plugins/oss-web-frontend-testing
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-web-frontend-testing
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-web-frontend-testing
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-web-frontend-testing ~/.gemini/config/plugins/oss-web-frontend-testing
```

## Starter Prompts

- `"Use oss-web-frontend-testing to style modern UI components with Tailwind CSS v4."`
- `"Use oss-web-frontend-testing to set up Playwright visual regression tests with toHaveScreenshot."`
- `"Use oss-web-frontend-testing to implement dynamic partial swapping with HTMX."`
