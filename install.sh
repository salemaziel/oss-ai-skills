#!/usr/bin/env bash
# Quick installation helper for OSS AI Skills plugins across Claude Code, Codex CLI, and Antigravity CLI (agy).
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGINS_DIR="${SCRIPT_DIR}/plugins"
GITHUB_REPO_URL="https://github.com/salemaziel/oss-ai-skills"
GITHUB_GIT_URL="https://github.com/salemaziel/oss-ai-skills.git"

PLUGINS=(
    "oss-django-stack"
    "oss-python-backend"
    "oss-qt-desktop"
    "oss-rust-stack"
    "oss-web-frontend-testing"
    "oss-browser-extensions"
    "oss-game-dev-emulation"
    "oss-ai-agent-dev"
    "oss-linux-desktop-tools"
    "oss-app-extensibility"
)

usage() {
    cat <<EOF
OSS AI Skills — Multi-Agent Plugin Installer

Usage:
  ./install.sh list                       List available plugins
  ./install.sh claude-marketplace         Register GitHub marketplace with Claude Code
  ./install.sh codex-marketplace          Register GitHub marketplace with Codex CLI
  ./install.sh install-claude [PLUGIN]    Install plugin(s) into Claude Code (or 'all')
  ./install.sh install-codex [PLUGIN]     Install plugin(s) into Codex CLI (or 'all')
  ./install.sh install-agy [PLUGIN]       Install plugin(s) into Antigravity CLI (or 'all')
  ./install.sh link-all                   Link all 10 plugins locally into ~/.gemini and ~/.codex

Available plugins:
$(for p in "${PLUGINS[@]}"; do echo "  - $p"; done)

Examples:
  ./install.sh claude-marketplace
  claude plugin install oss-django-stack@oss-ai-skills

  ./install.sh install-agy oss-django-stack
  ./install.sh link-all
EOF
}

cmd_list() {
    echo "📦 Available Native OSS AI Skills Plugins:"
    echo "============================================"
    for p in "${PLUGINS[@]}"; do
        if [ -d "${PLUGINS_DIR}/${p}" ]; then
            skills_count=$(find "${PLUGINS_DIR}/${p}/skills" -mindepth 1 -maxdepth 1 -type d | wc -l)
            desc=$(grep '"description":' "${PLUGINS_DIR}/${p}/plugin.json" | head -n1 | cut -d'"' -f4)
            echo "• ${p} (${skills_count} skills)"
            echo "  ${desc}"
            echo ""
        fi
    done
}

cmd_claude_marketplace() {
    echo "🌐 Registering Claude Code marketplace: ${GITHUB_REPO_URL}..."
    if command -v claude >/dev/null 2>&1; then
        claude plugin marketplace add "${GITHUB_REPO_URL}"
        echo "✅ Marketplace registered! You can now run: claude plugin install <plugin>@oss-ai-skills"
    else
        echo "⚠️ 'claude' CLI not found in PATH. You can manually run:"
        echo "   claude plugin marketplace add ${GITHUB_REPO_URL}"
    fi
}

cmd_codex_marketplace() {
    echo "🌐 Registering Codex CLI marketplace: ${GITHUB_GIT_URL}..."
    if command -v codex >/dev/null 2>&1; then
        codex plugin marketplace add "${GITHUB_GIT_URL}"
        echo "✅ Marketplace registered! You can now run: codex plugin add <plugin>@oss-ai-skills"
    else
        echo "⚠️ 'codex' CLI not found in PATH. You can manually run:"
        echo "   codex plugin marketplace add ${GITHUB_GIT_URL}"
    fi
}

cmd_install_claude() {
    local target="${1:-all}"
    if [ "$target" = "all" ]; then
        for p in "${PLUGINS[@]}"; do
            echo "Installing ${p} into Claude Code..."
            if command -v claude >/dev/null 2>&1; then
                claude plugin install "${PLUGINS_DIR}/${p}" || true
            else
                echo "  claude plugin install ${PLUGINS_DIR}/${p}"
            fi
        done
    else
        echo "Installing ${target} into Claude Code..."
        if command -v claude >/dev/null 2>&1; then
            claude plugin install "${PLUGINS_DIR}/${target}"
        else
            echo "  claude plugin install ${PLUGINS_DIR}/${target}"
        fi
    fi
}

cmd_install_codex() {
    local target="${1:-all}"
    local dest_base="${HOME}/.codex/plugins"
    mkdir -p "${dest_base}"

    if [ "$target" = "all" ]; then
        for p in "${PLUGINS[@]}"; do
            echo "Staging ${p} into ~/.codex/plugins/${p}..."
            rm -rf "${dest_base}/${p}"
            cp -R "${PLUGINS_DIR}/${p}" "${dest_base}/${p}"
        done
        echo "✅ All plugins installed into ~/.codex/plugins/"
    else
        echo "Staging ${target} into ~/.codex/plugins/${target}..."
        rm -rf "${dest_base}/${target}"
        cp -R "${PLUGINS_DIR}/${target}" "${dest_base}/${target}"
        echo "✅ Installed ${target} into ~/.codex/plugins/${target}"
    fi
}

cmd_install_agy() {
    local target="${1:-all}"
    if [ "$target" = "all" ]; then
        for p in "${PLUGINS[@]}"; do
            echo "Installing ${p} into Antigravity CLI..."
            if command -v agy >/dev/null 2>&1; then
                agy plugin install "${PLUGINS_DIR}/${p}" || true
            else
                dest="${HOME}/.gemini/config/plugins/${p}"
                mkdir -p "$(dirname "$dest")"
                ln -sfn "${PLUGINS_DIR}/${p}" "$dest"
                echo "  Linked to ${dest}"
            fi
        done
    else
        echo "Installing ${target} into Antigravity CLI..."
        if command -v agy >/dev/null 2>&1; then
            agy plugin install "${PLUGINS_DIR}/${target}"
        else
            dest="${HOME}/.gemini/config/plugins/${target}"
            mkdir -p "$(dirname "$dest")"
            ln -sfn "${PLUGINS_DIR}/${target}" "$dest"
            echo "  Linked to ${dest}"
        fi
    fi
}

cmd_link_all() {
    echo "🔗 Linking all 10 plugins for Antigravity (~/.gemini/config/plugins/) and Codex (~/.codex/plugins/)..."
    local agy_dir="${HOME}/.gemini/config/plugins"
    local codex_dir="${HOME}/.codex/plugins"
    mkdir -p "${agy_dir}" "${codex_dir}"

    for p in "${PLUGINS[@]}"; do
        ln -sfn "${PLUGINS_DIR}/${p}" "${agy_dir}/${p}"
        echo "  [agy]   -> ${agy_dir}/${p}"
        ln -sfn "${PLUGINS_DIR}/${p}" "${codex_dir}/${p}"
        echo "  [codex] -> ${codex_dir}/${p}"
    done
    echo "✅ All plugins linked successfully!"
}

case "${1:-help}" in
    list) cmd_list ;;
    claude-marketplace) cmd_claude_marketplace ;;
    codex-marketplace) cmd_codex_marketplace ;;
    install-claude) cmd_install_claude "${2:-all}" ;;
    install-codex) cmd_install_codex "${2:-all}" ;;
    install-agy) cmd_install_agy "${2:-all}" ;;
    link-all) cmd_link_all ;;
    *) usage ;;
esac
