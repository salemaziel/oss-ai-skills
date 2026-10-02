#!/usr/bin/env python3
"""Validation suite for native Claude Code, Codex CLI, and Antigravity plugins.

Checks:
- Antigravity strict schema (plugin.json at plugin root)
- Claude Code plugin manifest (.claude-plugin/plugin.json)
- Codex CLI plugin manifest (.codex-plugin/plugin.json)
- Claude Code marketplace catalog (.claude-plugin/marketplace.json)
- Codex CLI marketplace catalog (.agents/plugins/marketplace.json)
- Skill structure (SKILL.md, frontmatter name, description, internal link integrity)
"""

import json
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGINS_DIR = os.path.join(REPO_ROOT, "plugins")

ANTIGRAV_NAME_RE = re.compile(r"^[a-zA-Z0-9-_]+$")
FM_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)


def check(cond, msg, errors):
    if not cond:
        errors.append(msg)


def parse_frontmatter(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return None, ""
    m = FM_RE.match(content)
    if not m:
        return None, content
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
    return data, content[m.end():]


def validate_antigravity_manifest(plugin_path, errors):
    man_path = os.path.join(plugin_path, "plugin.json")
    check(os.path.isfile(man_path), f"Missing Antigravity plugin.json at {man_path}", errors)
    if not os.path.isfile(man_path):
        return
    try:
        with open(man_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"Antigravity plugin.json invalid JSON: {e}")
        return

    # Check allowed keys (additionalProperties: false per schema)
    allowed_keys = {"$schema", "name", "description"}
    extra_keys = set(data.keys()) - allowed_keys
    check(len(extra_keys) == 0, f"Antigravity plugin.json contains unexpected extra keys: {extra_keys}", errors)

    # Check name
    name = data.get("name")
    check(isinstance(name, str) and bool(ANTIGRAV_NAME_RE.match(name)), f"Antigravity plugin name '{name}' invalid regex pattern", errors)
    check(name == os.path.basename(plugin_path), f"Antigravity plugin name '{name}' does not match directory '{os.path.basename(plugin_path)}'", errors)

    # Check description
    desc = data.get("description")
    if desc is not None:
        check(isinstance(desc, str) and len(desc) > 0, "Antigravity plugin description must be non-empty string", errors)


def validate_claude_manifest(plugin_path, errors):
    man_path = os.path.join(plugin_path, ".claude-plugin", "plugin.json")
    check(os.path.isfile(man_path), f"Missing Claude Code .claude-plugin/plugin.json at {man_path}", errors)
    if not os.path.isfile(man_path):
        return
    try:
        with open(man_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"Claude Code plugin.json invalid JSON: {e}")
        return

    check(data.get("name") == os.path.basename(plugin_path), f"Claude plugin name mismatch: {data.get('name')}", errors)
    check(bool(data.get("version")), "Claude plugin version missing", errors)
    check(bool(data.get("description")), "Claude plugin description missing", errors)
    check(data.get("skills") == "./skills/", f"Claude plugin skills path should be './skills/', got {data.get('skills')}", errors)


def validate_codex_manifest(plugin_path, errors):
    man_path = os.path.join(plugin_path, ".codex-plugin", "plugin.json")
    check(os.path.isfile(man_path), f"Missing Codex .codex-plugin/plugin.json at {man_path}", errors)
    if not os.path.isfile(man_path):
        return
    try:
        with open(man_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"Codex plugin.json invalid JSON: {e}")
        return

    check(data.get("name") == os.path.basename(plugin_path), f"Codex plugin name mismatch: {data.get('name')}", errors)
    check(bool(data.get("version")), "Codex plugin version missing", errors)
    check(bool(data.get("description")), "Codex plugin description missing", errors)
    check(data.get("skills") == "./skills/", f"Codex plugin skills path should be './skills/', got {data.get('skills')}", errors)

    # Check interface metadata
    interface = data.get("interface", {})
    check(isinstance(interface, dict) and bool(interface.get("displayName")), "Codex interface.displayName missing", errors)
    check(bool(interface.get("category")), "Codex interface.category missing", errors)
    check(isinstance(interface.get("defaultPrompt"), list) and len(interface.get("defaultPrompt")) > 0, "Codex interface.defaultPrompt missing", errors)


def validate_skills_in_plugin(plugin_path, errors):
    skills_dir = os.path.join(plugin_path, "skills")
    check(os.path.isdir(skills_dir), f"Missing skills/ directory at {plugin_path}", errors)
    if not os.path.isdir(skills_dir):
        return

    skill_folders = sorted(os.listdir(skills_dir))
    check(len(skill_folders) > 0, f"No skills found in {skills_dir}", errors)

    for sf in skill_folders:
        sf_path = os.path.join(skills_dir, sf)
        if not os.path.isdir(sf_path):
            continue
        skill_md = os.path.join(sf_path, "SKILL.md")
        check(os.path.isfile(skill_md), f"Missing SKILL.md in {sf_path}", errors)
        if not os.path.isfile(skill_md):
            continue

        fm, body = parse_frontmatter(skill_md)
        check(fm is not None, f"Missing YAML frontmatter in {skill_md}", errors)
        if fm:
            check(bool(fm.get("name")), f"Missing 'name' in frontmatter of {skill_md}", errors)
            check(bool(fm.get("description")), f"Missing 'description' in frontmatter of {skill_md}", errors)

        # Check internal relative markdown links outside code blocks
        body_no_fenced = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
        body_no_code = re.sub(r"`.*?`", "", body_no_fenced)
        for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", body_no_code):
            link = m.group(2).strip()
            # Skip external URLs, anchors, mailto
            if link.startswith("http://") or link.startswith("https://") or link.startswith("#") or link.startswith("mailto:"):
                continue
            # Remove anchor part if any
            clean_link = link.split("#")[0].strip()
            if not clean_link:
                continue
            target_path = os.path.normpath(os.path.join(sf_path, clean_link))
            check(os.path.exists(target_path), f"Broken relative link in {skill_md}: '{link}' -> '{target_path}' not found", errors)


def validate_marketplaces(errors):
    # 1. Claude marketplace
    claude_mkt = os.path.join(REPO_ROOT, ".claude-plugin", "marketplace.json")
    check(os.path.isfile(claude_mkt), f"Missing Claude marketplace at {claude_mkt}", errors)
    if os.path.isfile(claude_mkt):
        try:
            with open(claude_mkt, "r", encoding="utf-8") as f:
                cdata = json.load(f)
            check(cdata.get("name") == "oss-ai-skills", "Claude marketplace name mismatch", errors)
            plugins = cdata.get("plugins", [])
            check(len(plugins) == 10, f"Expected 10 plugins in Claude marketplace, found {len(plugins)}", errors)
            for p in plugins:
                src = os.path.join(REPO_ROOT, p.get("source", ""))
                check(os.path.isdir(src), f"Claude marketplace plugin source does not exist: {src}", errors)
        except Exception as e:
            errors.append(f"Claude marketplace invalid JSON: {e}")

    # 2. Codex marketplace
    codex_mkt = os.path.join(REPO_ROOT, ".agents", "plugins", "marketplace.json")
    check(os.path.isfile(codex_mkt), f"Missing Codex marketplace at {codex_mkt}", errors)
    if os.path.isfile(codex_mkt):
        try:
            with open(codex_mkt, "r", encoding="utf-8") as f:
                xdata = json.load(f)
            check(xdata.get("name") == "oss-ai-skills", "Codex marketplace name mismatch", errors)
            plugins = xdata.get("plugins", [])
            check(len(plugins) == 10, f"Expected 10 plugins in Codex marketplace, found {len(plugins)}", errors)
            for p in plugins:
                src_obj = p.get("source", {})
                check(src_obj.get("source") == "git-subdir", f"Codex plugin source should be 'git-subdir', got {src_obj.get('source')}", errors)
                check("github.com/salemaziel/oss-ai-skills" in src_obj.get("url", ""), f"Codex plugin url missing salemaziel/oss-ai-skills", errors)
                rel_path = src_obj.get("path", "")
                full_path = os.path.join(REPO_ROOT, rel_path)
                check(os.path.isdir(full_path), f"Codex marketplace plugin path does not exist: {full_path}", errors)
        except Exception as e:
            errors.append(f"Codex marketplace invalid JSON: {e}")


def main():
    print("🔍 Running multi-agent plugin validation suite...")
    errors = []

    if not os.path.isdir(PLUGINS_DIR):
        print(f"❌ plugins directory missing at {PLUGINS_DIR}")
        sys.exit(1)

    plugins = [p for p in sorted(os.listdir(PLUGINS_DIR)) if os.path.isdir(os.path.join(PLUGINS_DIR, p))]
    check(len(plugins) == 10, f"Expected 10 plugins, found {len(plugins)}", errors)

    for p in plugins:
        p_path = os.path.join(PLUGINS_DIR, p)
        print(f"  Validating {p}...")
        validate_antigravity_manifest(p_path, errors)
        validate_claude_manifest(p_path, errors)
        validate_codex_manifest(p_path, errors)
        validate_skills_in_plugin(p_path, errors)

    validate_marketplaces(errors)

    if errors:
        print(f"\n❌ Validation failed with {len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"\n✅ All 10 plugins, manifests, skills, and marketplaces passed 100% validation!")


if __name__ == "__main__":
    main()
