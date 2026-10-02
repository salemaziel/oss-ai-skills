# OSS Python Backend & Services (`oss-python-backend`)

> Modern Python async microservices, HTTP APIs, database ORMs, caching, data validation, and automated testing.

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
| **aiohttp** | Use when building Python async HTTP services or clients with aiohttp - web server routing, middleware, WebSocket, SSE, streaming, client sessions, pytest-aiohttp testing, or troubleshooting SSL and timeout issues | [`skills/aiohttp/SKILL.md`](skills/aiohttp/SKILL.md) |
| **httpx** | Use when making HTTP requests in Python with httpx - sync and async clients, connection pooling, timeouts, HTTP/2, retry patterns, transport configuration, or choosing between httpx/requests/aiohttp | [`skills/httpx/SKILL.md`](skills/httpx/SKILL.md) |
| **pydantic** | Use when validating and serializing Python data with Pydantic v2 - models, field and model validators, constrained and special types, TypeAdapter, discriminated unions, BaseSettings, or FastAPI integration | [`skills/pydantic/SKILL.md`](skills/pydantic/SKILL.md) |
| **sqlalchemy** | "Use when working with SQLAlchemy 2.0 in Python - declarative models, queries, sessions, async engines, Alembic migrations, relationship loading strategies, N+1 detection, pool exhaustion, or 2.0 migration" | [`skills/sqlalchemy/SKILL.md`](skills/sqlalchemy/SKILL.md) |
| **celery** | Use when running background tasks with Celery - worker and broker configuration (Redis, RabbitMQ), task routing by name vs queue, chains/groups/chords, retry patterns (autoretry_for, retry_backoff), acks_late semantics, failure detection, and monitoring with Flower | [`skills/celery/SKILL.md`](skills/celery/SKILL.md) |
| **redis** | Use when working with Redis - in-memory database, caching, pub/sub, sessions, rate limiting, RESP3, asyncio, Redis Stack | [`skills/redis/SKILL.md`](skills/redis/SKILL.md) |
| **pytest** | Use when writing Python tests with pytest - fixtures, parametrization, markers, conftest layout, pytest-asyncio, pytest-django, coverage with pytest-cov, mocking with pytest-mock, parallel runs with xdist, or CI integration | [`skills/pytest/SKILL.md`](skills/pytest/SKILL.md) |
| **ast-grep** | Use when doing structural code search and rewriting - ast-grep linting, refactoring, multi-language patterns | [`skills/ast-grep/SKILL.md`](skills/ast-grep/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-python-backend@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-python-backend
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-python-backend@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-python-backend ~/.codex/plugins/oss-python-backend
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-python-backend
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-python-backend
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-python-backend ~/.gemini/config/plugins/oss-python-backend
```

## Starter Prompts

- `"Use oss-python-backend to build an async HTTP microservice with aiohttp."`
- `"Use oss-python-backend to design SQLAlchemy 2.0 async declarative models."`
- `"Use oss-python-backend to validate inputs with Pydantic v2 and run pytest."`
