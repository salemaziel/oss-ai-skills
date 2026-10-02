# OSS AI Agent & RAG Engineering (`oss-ai-agent-dev`)

> AI agent engineering, RAG pipelines with LlamaIndex, OpenCode agent plugin architecture, and structured schema validation.

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
| **llama-index** | Use when building RAG or LLM applications with LlamaIndex - data loaders, node parsing, vector stores, retrievers and rerankers, query engines, agents and workflows, streaming, or evaluation | [`skills/llama-index/SKILL.md`](skills/llama-index/SKILL.md) |
| **opencode** | Use when developing plugins, tools, and extensions for OpenCode v1 - plugin contract, crash-prevention rules, ctx/event APIs, subagent lifecycle (abort races, compaction, orphan detection), MCP integration, testing patterns, or publishing to npm | [`skills/opencode/SKILL.md`](skills/opencode/SKILL.md) |
| **pydantic** | Use when validating and serializing Python data with Pydantic v2 - models, field and model validators, constrained and special types, TypeAdapter, discriminated unions, BaseSettings, or FastAPI integration | [`skills/pydantic/SKILL.md`](skills/pydantic/SKILL.md) |
| **httpx** | Use when making HTTP requests in Python with httpx - sync and async clients, connection pooling, timeouts, HTTP/2, retry patterns, transport configuration, or choosing between httpx/requests/aiohttp | [`skills/httpx/SKILL.md`](skills/httpx/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-ai-agent-dev@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-ai-agent-dev
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-ai-agent-dev@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-ai-agent-dev ~/.codex/plugins/oss-ai-agent-dev
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-ai-agent-dev
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-ai-agent-dev
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-ai-agent-dev ~/.gemini/config/plugins/oss-ai-agent-dev
```

## Starter Prompts

- `"Use oss-ai-agent-dev to implement a LlamaIndex RAG retrieval pipeline with custom nodes."`
- `"Use oss-ai-agent-dev to author an OpenCode v1 subagent tool plugin with MCP support."`
- `"Use oss-ai-agent-dev to define type-safe agent schemas with Pydantic v2."`
