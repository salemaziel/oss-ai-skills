# oss-ai-skills — Curated Open Source AI Skills Repository & Multi-Agent Plugin Marketplace

One job: Maintain and curate task-focused, specification-compliant open source AI agent skills across frameworks, languages, tools, and extensions, and publish them as domain-bundled native plugins for Claude Code, Codex CLI, and Antigravity CLI (`agy`).

## Contract
- **Role**: Open-Source Agent Skills Collection & Multi-Agent Plugin Suite (`frameworks/`, `languages/`, `tool/`, `extend/`, `plugins/`)
- **Inputs**: Framework/library documentation, API references, common engineering pitfalls, and multi-agent plugin specifications (Claude Code, OpenAI Codex, Google Antigravity).
- **Process**: Author compact, trigger-oriented skills (`SKILL.md` ≤ 600 lines), bundle complementary skills into 10 self-contained plugins via `scripts/bundle_plugins.py`, and validate with `scripts/validate_plugins.py`.
- **Outputs**: Standardized Agent Skills and 10 native plugins discoverable and executable across Claude Code, Codex CLI, and Antigravity CLI (`agy`), published via GitHub marketplace (`salemaziel/oss-ai-skills`).
- **Human check**: Verify trigger-style `description` in frontmatter, run `python3 scripts/validate_plugins.py` for 100% multi-agent schema compliance, and verify internal link resolution.

For full authoring guidelines and formatting standards, see [AGENTS.md](AGENTS.md) and [README.md](README.md).

## Directory Structure
```
oss-ai-skills/
├── .agents/
│   └── plugins/
│       └── marketplace.json        # Codex CLI GitHub marketplace catalog
├── .claude-plugin/
│   └── marketplace.json            # Claude Code GitHub marketplace catalog
├── extend/                         # Canonical raw skills (extensions)
├── frameworks/                     # Canonical raw skills (frameworks)
├── languages/                      # Canonical raw skills (languages)
├── plugins/                        # 10 self-contained multi-agent plugins
│   ├── oss-ai-agent-dev/
│   ├── oss-app-extensibility/
│   ├── oss-browser-extensions/
│   ├── oss-django-stack/
│   ├── oss-game-dev-emulation/
│   ├── oss-linux-desktop-tools/
│   ├── oss-python-backend/
│   ├── oss-qt-desktop/
│   ├── oss-rust-stack/
│   └── oss-web-frontend-testing/
├── scripts/
│   ├── analyze_skills.py
│   ├── bundle_plugins.py           # Compiles plugins & marketplace catalogs
│   ├── skill_update_report.py
│   └── validate_plugins.py         # Multi-agent schema validator
├── tool/                           # Canonical raw skills (tools)
├── AGENTS.md
├── CONTEXT.md
├── LICENSE
├── README.md
└── install.sh                      # Helper to install/link plugins across agents
```

