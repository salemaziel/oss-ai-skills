#!/usr/bin/env python3
"""Build and bundle spec-compliant native plugins for Claude Code, Codex CLI, and Antigravity CLI.

Reads canonical source skills in frameworks/, extend/, languages/, tool/ and compiles
self-contained, multi-agent plugins into plugins/<plugin-name>/ with:
- Claude Code manifest: .claude-plugin/plugin.json
- Codex CLI manifest: .codex-plugin/plugin.json
- Antigravity CLI manifest: plugin.json (strict schema)
- README.md: Usage and installation instructions for all three platforms
- Self-contained skills in skills/<skill-name>/

Also generates top-level GitHub-hosted marketplace catalogs:
- .claude-plugin/marketplace.json (Anthropic marketplace schema)
- .agents/plugins/marketplace.json (OpenAI Codex marketplace schema)
"""

import argparse
import json
import os
import re
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GITHUB_USER = "salemaziel"
GITHUB_REPO_URL = f"https://github.com/{GITHUB_USER}/oss-ai-skills"
GITHUB_GIT_URL = f"https://github.com/{GITHUB_USER}/oss-ai-skills.git"
DEFAULT_BRANCH = "master"
AUTHOR = {
    "name": "salemaziel",
    "email": "mymainemail0501@gmail.com",
    "url": f"https://github.com/{GITHUB_USER}",
}

PLUGINS_CONFIG = [
    {
        "slug": "oss-django-stack",
        "displayName": "OSS Django Full-Stack Suite",
        "version": "1.0.0",
        "description": "Full-stack Django web development: core ORM, admin theming, REST APIs, HTMX, Celery background tasks, Redis, and pytest.",
        "shortDescription": "Full-stack Django development toolkit",
        "category": "Developer Tools",
        "keywords": [
            "django",
            "python",
            "orm",
            "htmx",
            "celery",
            "redis",
            "rest-api",
            "pytest",
            "tailwind",
        ],
        "defaultPrompts": [
            "Use oss-django-stack to build a high-performance REST API with Django Ninja.",
            "Use oss-django-stack to optimize database transactions and queries.",
            "Use oss-django-stack to configure Celery task queues with Redis.",
        ],
        "skills": [
            ("frameworks/django", "django"),
            ("frameworks/django-admin", "django-admin"),
            ("frameworks/django-transaction", "django-transaction"),
            ("frameworks/django-filter", "django-filter"),
            ("frameworks/django-allauth", "django-allauth"),
            ("frameworks/django-htmx", "django-htmx"),
            ("frameworks/django-ninja", "django-ninja"),
            ("frameworks/turbodrf", "turbodrf"),
            ("frameworks/django-bolt", "django-bolt"),
            ("frameworks/django-unfold", "django-unfold"),
            ("frameworks/django-storages", "django-storages"),
            ("frameworks/django-celery", "django-celery"),
            ("frameworks/celery", "celery"),
            ("tool/redis", "redis"),
            ("frameworks/django-tdd", "django-tdd"),
            ("frameworks/pytest", "pytest"),
            ("frameworks/pydantic", "pydantic"),
            ("frameworks/tailwind", "tailwind"),
        ],
    },
    {
        "slug": "oss-python-backend",
        "displayName": "OSS Python Backend & Services",
        "version": "1.0.0",
        "description": "Modern Python async microservices, HTTP APIs, database ORMs, caching, data validation, and automated testing.",
        "shortDescription": "Python async microservices and backend toolkit",
        "category": "Developer Tools",
        "keywords": [
            "python",
            "async",
            "aiohttp",
            "httpx",
            "sqlalchemy",
            "celery",
            "redis",
            "pytest",
            "ast-grep",
        ],
        "defaultPrompts": [
            "Use oss-python-backend to build an async HTTP microservice with aiohttp.",
            "Use oss-python-backend to design SQLAlchemy 2.0 async declarative models.",
            "Use oss-python-backend to validate inputs with Pydantic v2 and run pytest.",
        ],
        "skills": [
            ("frameworks/aiohttp", "aiohttp"),
            ("frameworks/httpx", "httpx"),
            ("frameworks/pydantic", "pydantic"),
            ("frameworks/sqlalchemy", "sqlalchemy"),
            ("frameworks/celery", "celery"),
            ("tool/redis", "redis"),
            ("frameworks/pytest", "pytest"),
            ("tool/ast-grep", "ast-grep"),
        ],
    },
    {
        "slug": "oss-qt-desktop",
        "displayName": "OSS Qt Desktop & GUI Suite",
        "version": "1.0.0",
        "description": "Cross-platform GUI development with Qt in Python (PyQt6/PySide6) and C++, plus KDE Plasma widgets and Kate editor extensions.",
        "shortDescription": "Qt and PyQt desktop application development toolkit",
        "category": "Developer Tools",
        "keywords": [
            "qt",
            "pyqt",
            "pyside",
            "gui",
            "desktop",
            "c++",
            "cmake",
            "kde",
            "plasma",
            "widgets",
        ],
        "defaultPrompts": [
            "Use oss-qt-desktop to build a desktop GUI application using PyQt6 widgets and QSS styling.",
            "Use oss-qt-desktop to manage worker threads with QThread and QThreadPool.",
            "Use oss-qt-desktop to develop a KDE Plasma 6 widget or Kate plugin.",
        ],
        "skills": [
            ("frameworks/pyqt", "pyqt"),
            ("frameworks/pyqt/core", "pyqt-core"),
            ("frameworks/pyqt/widgets", "pyqt-widgets"),
            ("frameworks/pyqt/dialogs", "pyqt-dialogs"),
            ("frameworks/pyqt/styling", "pyqt-styling"),
            ("frameworks/pyqt/threading", "pyqt-threading"),
            ("frameworks/pyqt/multimedia", "pyqt-multimedia"),
            ("frameworks/pyqt/testing", "pyqt-testing"),
            ("frameworks/qt-cpp", "qt-cpp"),
            ("extend/kde-plasmoid", "kde-plasmoid"),
            ("extend/kate-plugin", "kate-plugin"),
            ("frameworks/pytest", "pytest"),
        ],
    },
    {
        "slug": "oss-rust-stack",
        "displayName": "OSS Rust Systems & TUI",
        "version": "1.0.0",
        "description": "Idiomatic Rust systems engineering, high-performance terminal user interfaces with Ratatui, and structural AST code refactoring.",
        "shortDescription": "Rust systems and terminal UI development toolkit",
        "category": "Developer Tools",
        "keywords": [
            "rust",
            "systems",
            "tui",
            "ratatui",
            "cli",
            "ast-grep",
            "async",
            "performance",
        ],
        "defaultPrompts": [
            "Use oss-rust-stack to build an interactive terminal UI with Ratatui.",
            "Use oss-rust-stack to refactor Rust async code for maximum performance.",
            "Use oss-rust-stack to perform AST pattern search and rewriting.",
        ],
        "skills": [
            ("languages/rust-core", "rust-core"),
            ("frameworks/ratatui", "ratatui"),
            ("tool/ast-grep", "ast-grep"),
        ],
    },
    {
        "slug": "oss-web-frontend-testing",
        "displayName": "OSS Web Frontend & Visual QA",
        "version": "1.0.0",
        "description": "Web UI engineering with Tailwind CSS v4, visual regression testing with Playwright, dynamic reactive server UI with HTMX, and AST linting.",
        "shortDescription": "Frontend styling and Playwright visual QA toolkit",
        "category": "Developer Tools",
        "keywords": [
            "tailwind",
            "css",
            "playwright",
            "visual-regression",
            "htmx",
            "testing",
            "ast-grep",
        ],
        "defaultPrompts": [
            "Use oss-web-frontend-testing to style modern UI components with Tailwind CSS v4.",
            "Use oss-web-frontend-testing to set up Playwright visual regression tests with toHaveScreenshot.",
            "Use oss-web-frontend-testing to implement dynamic partial swapping with HTMX.",
        ],
        "skills": [
            ("frameworks/tailwind", "tailwind"),
            ("frameworks/playwright-visual-regression", "playwright-visual-regression"),
            ("frameworks/django-htmx", "django-htmx"),
            ("tool/ast-grep", "ast-grep"),
        ],
    },
    {
        "slug": "oss-browser-extensions",
        "displayName": "OSS Mozilla Browser & Mail Extensions",
        "version": "1.0.0",
        "description": "Browser and mail extension development for Firefox WebExtensions and Thunderbird MailExtensions with E2E visual regression testing.",
        "shortDescription": "Firefox and Thunderbird extension development toolkit",
        "category": "Developer Tools",
        "keywords": [
            "firefox",
            "webextension",
            "thunderbird",
            "mailextension",
            "mozilla",
            "playwright",
            "browser",
        ],
        "defaultPrompts": [
            "Use oss-browser-extensions to create a Manifest V3 Firefox WebExtension with web-ext.",
            "Use oss-browser-extensions to implement a Thunderbird mail extension using messenger.* APIs.",
            "Use oss-browser-extensions to write Playwright visual regression tests for extension popups.",
        ],
        "skills": [
            ("extend/firefox-extension", "firefox-extension"),
            ("extend/thunderbird-extension", "thunderbird-extension"),
            ("frameworks/playwright-visual-regression", "playwright-visual-regression"),
        ],
    },
    {
        "slug": "oss-game-dev-emulation",
        "displayName": "OSS Game Dev & Modding",
        "version": "1.0.0",
        "description": "2D game development in Python (pygame), GBA Lua game engine, mGBA emulator automation, and OpenRCT2 modding.",
        "shortDescription": "Game development, emulation, and modding toolkit",
        "category": "Developer Tools",
        "keywords": [
            "game-development",
            "pygame",
            "gba",
            "mgba",
            "lua",
            "emulator",
            "openrct2",
            "modding",
        ],
        "defaultPrompts": [
            "Use oss-game-dev-emulation to build a 2D game loop with sprite collision in pygame.",
            "Use oss-game-dev-emulation to script mGBA emulator automation and RAM watching in Lua.",
            "Use oss-game-dev-emulation to create OpenRCT2 game action plugins in TypeScript.",
        ],
        "skills": [
            ("frameworks/pygame", "pygame"),
            ("frameworks/bpcore-engine", "bpcore-engine"),
            ("extend/mgba", "mgba"),
            ("extend/openrct2", "openrct2"),
        ],
    },
    {
        "slug": "oss-ai-agent-dev",
        "displayName": "OSS AI Agent & RAG Engineering",
        "version": "1.0.0",
        "description": "AI agent engineering, RAG pipelines with LlamaIndex, OpenCode agent plugin architecture, and structured schema validation.",
        "shortDescription": "Autonomous AI agent and RAG architecture toolkit",
        "category": "Automation",
        "keywords": [
            "ai",
            "agent",
            "rag",
            "llamaindex",
            "opencode",
            "pydantic",
            "httpx",
            "mcp",
        ],
        "defaultPrompts": [
            "Use oss-ai-agent-dev to implement a LlamaIndex RAG retrieval pipeline with custom nodes.",
            "Use oss-ai-agent-dev to author an OpenCode v1 subagent tool plugin with MCP support.",
            "Use oss-ai-agent-dev to define type-safe agent schemas with Pydantic v2.",
        ],
        "skills": [
            ("frameworks/llama-index", "llama-index"),
            ("extend/opencode", "opencode"),
            ("frameworks/pydantic", "pydantic"),
            ("frameworks/httpx", "httpx"),
        ],
    },
    {
        "slug": "oss-linux-desktop-tools",
        "displayName": "OSS Linux Desktop & System Tools",
        "version": "1.0.0",
        "description": "Linux desktop utilities, Waydroid Android container integration, KDE Plasma 6 desktop widgets, and local Redis caching.",
        "shortDescription": "Linux desktop and system utilities toolkit",
        "category": "System",
        "keywords": [
            "linux",
            "waydroid",
            "android",
            "container",
            "kde",
            "plasma",
            "redis",
            "desktop",
        ],
        "defaultPrompts": [
            "Use oss-linux-desktop-tools to set up and troubleshoot Waydroid on Linux with GPU acceleration.",
            "Use oss-linux-desktop-tools to build a KDE Plasma 6 widget with Python backend.",
            "Use oss-linux-desktop-tools to configure local Redis for desktop caching and IPC.",
        ],
        "skills": [
            ("tool/waydroid", "waydroid"),
            ("extend/kde-plasmoid", "kde-plasmoid"),
            ("tool/redis", "redis"),
        ],
    },
    {
        "slug": "oss-app-extensibility",
        "displayName": "OSS Desktop App Extensibility & Modding",
        "version": "1.0.0",
        "description": "Scripting and extending open-source desktop software: GIMP 3.0+ Python plugins, Kate editor C++ plugins, OpenRCT2 game mods, and OpenCode tools.",
        "shortDescription": "Open-source application plugin and extension toolkit",
        "category": "Developer Tools",
        "keywords": [
            "plugin",
            "extensibility",
            "gimp",
            "kate",
            "openrct2",
            "opencode",
            "modding",
            "gegl",
        ],
        "defaultPrompts": [
            "Use oss-app-extensibility to develop a GIMP 3.0 Python plugin using GEGL procedures.",
            "Use oss-app-extensibility to create a Kate text editor plugin in C++.",
            "Use oss-app-extensibility to build an OpenRCT2 game mod in TypeScript.",
        ],
        "skills": [
            ("extend/gimp-plugin", "gimp-plugin"),
            ("extend/kate-plugin", "kate-plugin"),
            ("extend/openrct2", "openrct2"),
            ("extend/opencode", "opencode"),
        ],
    },
]


def parse_frontmatter(file_path):
    """Extract name, description, and metadata from SKILL.md."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not m:
        return {}
    block = m.group(1)
    data = {}
    current_key = None
    buf = []
    for line in block.splitlines():
        km = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if km:
            if current_key:
                data[current_key] = " ".join(buf).strip()
            current_key = km.group(1).strip()
            buf = [km.group(2).strip()]
        elif current_key and (line.startswith("  ") or line.startswith("\t")):
            buf.append(line.strip())
    if current_key:
        data[current_key] = " ".join(buf).strip()
    return data


def copy_skill(src_rel_path, dest_skill_dir):
    """Copy a skill folder, handling nested sub-skills (like frameworks/pyqt) cleanly."""
    src_abs = os.path.join(REPO_ROOT, src_rel_path)
    os.makedirs(dest_skill_dir, exist_ok=True)

    # 1. Copy SKILL.md
    src_skill_md = os.path.join(src_abs, "SKILL.md")
    if not os.path.isfile(src_skill_md):
        raise FileNotFoundError(f"Missing SKILL.md at {src_skill_md}")

    with open(src_skill_md, "r", encoding="utf-8") as f:
        skill_text = f.read()

    # For pyqt hub skill: adjust links from core/SKILL.md to ../pyqt-core/SKILL.md
    if src_rel_path == "frameworks/pyqt":
        for sub in ["core", "widgets", "threading", "dialogs", "testing", "styling", "multimedia"]:
            skill_text = skill_text.replace(f"[{sub}/SKILL.md]({sub}/SKILL.md)", f"[../pyqt-{sub}/SKILL.md](../pyqt-{sub}/SKILL.md)")

    # For django skill: adjust links from frameworks/django-* to ../django-*/SKILL.md
    if src_rel_path == "frameworks/django":
        skill_text = skill_text.replace("frameworks/django-admin/SKILL.md", "../django-admin/SKILL.md")
        skill_text = skill_text.replace("frameworks/django-transaction/SKILL.md", "../django-transaction/SKILL.md")

    dest_skill_md = os.path.join(dest_skill_dir, "SKILL.md")
    with open(dest_skill_md, "w", encoding="utf-8") as f:
        f.write(skill_text)

    # 2. Copy standard subdirectories: references, scripts, rules
    for sub in ["references", "scripts", "rules"]:
        sub_src = os.path.join(src_abs, sub)
        if os.path.isdir(sub_src):
            sub_dest = os.path.join(dest_skill_dir, sub)
            if os.path.exists(sub_dest):
                shutil.rmtree(sub_dest)
            shutil.copytree(sub_src, sub_dest)


def generate_plugin_readme(plugin_config, skills_info):
    """Generate user-facing README.md for the plugin bundle."""
    slug = plugin_config["slug"]
    display_name = plugin_config["displayName"]
    description = plugin_config["description"]
    version = plugin_config["version"]

    lines = [
        f"# {display_name} (`{slug}`)",
        "",
        f"> {description}",
        "",
        f"- **Version**: {version}",
        f"- **License**: GPL-3.0",
        f"- **Repository**: [{GITHUB_REPO_URL}]({GITHUB_REPO_URL})",
        "",
        "## Compatibility",
        "",
        "This plugin is natively compatible with:",
        "- 🟣 **Claude Code** (`.claude-plugin/plugin.json`)",
        "- 🟢 **OpenAI Codex CLI** (`.codex-plugin/plugin.json`)",
        "- 🔵 **Google Antigravity CLI (`agy`)** (`plugin.json`)",
        "",
        "## Bundled Skills",
        "",
        "| Skill | Trigger / Description | Entry Point |",
        "|---|---|---|",
    ]

    for name, desc in skills_info:
        # Clean description
        d = desc.replace("\n", " ").strip()
        lines.append(f"| **{name}** | {d} | [`skills/{name}/SKILL.md`](skills/{name}/SKILL.md) |")

    lines.extend([
        "",
        "## Installation",
        "",
        "### 1. Claude Code",
        "",
        "**From GitHub Marketplace** (recommended):",
        "```bash",
        f"claude plugin marketplace add {GITHUB_REPO_URL}",
        f"claude plugin install {slug}@oss-ai-skills",
        "```",
        "",
        "**From Local Repository**:",
        "```bash",
        f"claude plugin install ./plugins/{slug}",
        "```",
        "",
        "### 2. OpenAI Codex CLI",
        "",
        "**From GitHub Marketplace** (recommended):",
        "```bash",
        f"codex plugin marketplace add {GITHUB_REPO_URL}",
        f"codex plugin add {slug}@oss-ai-skills",
        "```",
        "",
        "**From Local Repository**:",
        "```bash",
        f"mkdir -p ~/.codex/plugins",
        f"cp -R ./plugins/{slug} ~/.codex/plugins/{slug}",
        "```",
        "",
        "### 3. Google Antigravity CLI (`agy`)",
        "",
        "**Using Antigravity CLI shell command**:",
        "```bash",
        f"agy plugin install ./plugins/{slug}",
        "```",
        "",
        "**Inside Antigravity interactive session**:",
        "```text",
        f"/plugin install ./plugins/{slug}",
        "```",
        "",
        "**Global workspace symlink**:",
        "```bash",
        f"mkdir -p ~/.gemini/config/plugins",
        f"ln -s $(pwd)/plugins/{slug} ~/.gemini/config/plugins/{slug}",
        "```",
        "",
        "## Starter Prompts",
        "",
    ])

    for prompt in plugin_config["defaultPrompts"]:
        lines.append(f"- `\"{prompt}\"`")

    lines.append("")
    return "\n".join(lines)


def build_plugins(dry_run=False):
    plugins_dir = os.path.join(REPO_ROOT, "plugins")
    if not dry_run:
        os.makedirs(plugins_dir, exist_ok=True)

    claude_marketplace_plugins = []
    codex_marketplace_plugins = []

    for cfg in PLUGINS_CONFIG:
        slug = cfg["slug"]
        display_name = cfg["displayName"]
        version = cfg["version"]
        desc = cfg["description"]
        short_desc = cfg["shortDescription"]
        category = cfg["category"]
        keywords = cfg["keywords"]
        prompts = cfg["defaultPrompts"]

        plugin_dest = os.path.join(plugins_dir, slug)
        print(f"📦 Packaging bundle: {slug} ({display_name})...")

        skills_info = []
        if not dry_run:
            os.makedirs(plugin_dest, exist_ok=True)
            skills_dest_dir = os.path.join(plugin_dest, "skills")
            os.makedirs(skills_dest_dir, exist_ok=True)

        for src_path, dest_name in cfg["skills"]:
            src_full = os.path.join(REPO_ROOT, src_path, "SKILL.md")
            fm = parse_frontmatter(src_full)
            skill_name = fm.get("name", dest_name)
            skill_desc = fm.get("description", "")
            skills_info.append((dest_name, skill_desc))

            if not dry_run:
                dest_skill_folder = os.path.join(plugin_dest, "skills", dest_name)
                copy_skill(src_path, dest_skill_folder)

        if not dry_run:
            # 1. Claude Code manifest
            claude_plugin_dir = os.path.join(plugin_dest, ".claude-plugin")
            os.makedirs(claude_plugin_dir, exist_ok=True)
            claude_manifest = {
                "name": slug,
                "displayName": display_name,
                "version": version,
                "description": desc,
                "author": AUTHOR,
                "homepage": f"{GITHUB_REPO_URL}/tree/{DEFAULT_BRANCH}/plugins/{slug}",
                "repository": GITHUB_REPO_URL,
                "license": "GPL-3.0",
                "keywords": keywords,
                "skills": "./skills/",
            }
            with open(os.path.join(claude_plugin_dir, "plugin.json"), "w", encoding="utf-8") as f:
                json.dump(claude_manifest, f, indent=2, ensure_ascii=False)
                f.write("\n")

            # 2. Codex CLI manifest
            codex_plugin_dir = os.path.join(plugin_dest, ".codex-plugin")
            os.makedirs(codex_plugin_dir, exist_ok=True)
            codex_manifest = {
                "name": slug,
                "version": version,
                "description": desc,
                "author": AUTHOR,
                "homepage": f"{GITHUB_REPO_URL}/tree/{DEFAULT_BRANCH}/plugins/{slug}",
                "repository": GITHUB_REPO_URL,
                "license": "GPL-3.0",
                "keywords": keywords,
                "skills": "./skills/",
                "interface": {
                    "displayName": display_name,
                    "shortDescription": short_desc,
                    "longDescription": desc,
                    "developerName": AUTHOR["name"],
                    "category": category,
                    "capabilities": ["Instructions"],
                    "websiteURL": f"{GITHUB_REPO_URL}/tree/{DEFAULT_BRANCH}/plugins/{slug}",
                    "defaultPrompt": prompts,
                },
            }
            with open(os.path.join(codex_plugin_dir, "plugin.json"), "w", encoding="utf-8") as f:
                json.dump(codex_manifest, f, indent=2, ensure_ascii=False)
                f.write("\n")

            # 3. Antigravity CLI manifest (strict schema)
            antigravity_manifest = {
                "$schema": "https://antigravity.google/schemas/v1/plugin.json",
                "name": slug,
                "description": desc,
            }
            with open(os.path.join(plugin_dest, "plugin.json"), "w", encoding="utf-8") as f:
                json.dump(antigravity_manifest, f, indent=2, ensure_ascii=False)
                f.write("\n")

            # 4. Plugin README
            readme_content = generate_plugin_readme(cfg, skills_info)
            with open(os.path.join(plugin_dest, "README.md"), "w", encoding="utf-8") as f:
                f.write(readme_content)

        # Marketplace entries
        claude_marketplace_plugins.append({
            "name": slug,
            "source": f"./plugins/{slug}",
            "description": desc,
            "version": version,
        })

        codex_marketplace_plugins.append({
            "name": slug,
            "source": {
                "source": "git-subdir",
                "url": GITHUB_GIT_URL,
                "path": f"./plugins/{slug}",
                "ref": DEFAULT_BRANCH,
            },
            "policy": {
                "installation": "AVAILABLE",
                "authentication": "ON_INSTALL",
            },
            "category": category,
        })

    if not dry_run:
        # Write Claude marketplace: .claude-plugin/marketplace.json
        claude_mkt_dir = os.path.join(REPO_ROOT, ".claude-plugin")
        os.makedirs(claude_mkt_dir, exist_ok=True)
        claude_marketplace = {
            "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
            "name": "oss-ai-skills",
            "description": "Open Source AI Skills — domain-bundled plugins for Claude Code, Codex CLI, and Antigravity.",
            "owner": {
                "name": AUTHOR["name"],
                "email": AUTHOR["email"],
            },
            "plugins": claude_marketplace_plugins,
        }
        with open(os.path.join(claude_mkt_dir, "marketplace.json"), "w", encoding="utf-8") as f:
            json.dump(claude_marketplace, f, indent=2, ensure_ascii=False)
            f.write("\n")

        # Write Codex marketplace: .agents/plugins/marketplace.json
        codex_mkt_dir = os.path.join(REPO_ROOT, ".agents", "plugins")
        os.makedirs(codex_mkt_dir, exist_ok=True)
        codex_marketplace = {
            "name": "oss-ai-skills",
            "interface": {
                "displayName": "OSS AI Skills Marketplace",
            },
            "plugins": codex_marketplace_plugins,
        }
        with open(os.path.join(codex_mkt_dir, "marketplace.json"), "w", encoding="utf-8") as f:
            json.dump(codex_marketplace, f, indent=2, ensure_ascii=False)
            f.write("\n")

    print("✅ All 10 plugins and marketplace catalogs compiled successfully!")


def main():
    parser = argparse.ArgumentParser(description="Compile and bundle native plugins.")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without writing files.")
    args = parser.parse_args()
    build_plugins(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
