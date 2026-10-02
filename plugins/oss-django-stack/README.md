# OSS Django Full-Stack Suite (`oss-django-stack`)

> Full-stack Django web development: core ORM, admin theming, REST APIs, HTMX, Celery background tasks, Redis, and pytest.

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
| **django** | Use when building Django applications - security hardening, authentication and permissions, ORM optimization, PostgreSQL features, Django 6.0, migrations, testing, and ecosystem libraries | [`skills/django/SKILL.md`](skills/django/SKILL.md) |
| **django-admin** | Use when customizing Django Admin - save_formset, get_search_results, formsets, queryset optimization, db_index, custom URLs | [`skills/django-admin/SKILL.md`](skills/django-admin/SKILL.md) |
| **django-transaction** | Use when handling Django transactions and concurrency - atomic, select_for_update, on_commit, upserts, M2M ordering | [`skills/django-transaction/SKILL.md`](skills/django-transaction/SKILL.md) |
| **django-filter** | Use when filtering Django querysets - FilterSet, custom filters, Django REST Framework integration, explicit fields | [`skills/django-filter/SKILL.md`](skills/django-filter/SKILL.md) |
| **django-allauth** | Use when implementing Django authentication - local accounts, OAuth, email verification, MFA, OIDC, django-organizations | [`skills/django-allauth/SKILL.md`](skills/django-allauth/SKILL.md) |
| **django-htmx** | Use when building dynamic Django web apps with htmx - partial rendering, HTMX responses, querystring tag, CSP | [`skills/django-htmx/SKILL.md`](skills/django-htmx/SKILL.md) |
| **django-ninja** | Use when building Django REST APIs with django-ninja - Pydantic schemas, routers, CRUD endpoints, authentication, pagination, file uploads, async views, OpenAPI docs, or migrating from DRF | [`skills/django-ninja/SKILL.md`](skills/django-ninja/SKILL.md) |
| **turbodrf** | Use when building Django REST APIs with TurboDRF - model Meta configuration, role-based and field-level permissions, multi-tenant predicates, router wiring, management commands, settings, or troubleshooting | [`skills/turbodrf/SKILL.md`](skills/turbodrf/SKILL.md) |
| **django-bolt** | Use when building high-performance APIs with django-bolt - routing, JWT auth, msgspec serializers, WebSockets, SSE streaming, file uploads, ORM patterns, runbolt deployment, or migrating from DRF | [`skills/django-bolt/SKILL.md`](skills/django-bolt/SKILL.md) |
| **django-unfold** | Use when theming the Django admin with django-unfold - settings and sidebar configuration, custom admin site, components and @display decorator, filters, actions, tabs, dark mode and styling, or Django 6.x compatibility | [`skills/django-unfold/SKILL.md`](skills/django-unfold/SKILL.md) |
| **django-storages** | Use when configuring django-storages for cloud file storage - STORAGES setting, Amazon S3, Google Cloud Storage and Azure backends, signed URLs, CDN and caching, multipart uploads, or storage testing | [`skills/django-storages/SKILL.md`](skills/django-storages/SKILL.md) |
| **django-celery** | Use when integrating Celery with Django - task definition and calling, django-celery-beat scheduling, worker deployment, Flower monitoring, testing tasks, batch processing, or choosing between cron and beat | [`skills/django-celery/SKILL.md`](skills/django-celery/SKILL.md) |
| **celery** | Use when running background tasks with Celery - worker and broker configuration (Redis, RabbitMQ), task routing by name vs queue, chains/groups/chords, retry patterns (autoretry_for, retry_backoff), acks_late semantics, failure detection, and monitoring with Flower | [`skills/celery/SKILL.md`](skills/celery/SKILL.md) |
| **redis** | Use when working with Redis - in-memory database, caching, pub/sub, sessions, rate limiting, RESP3, asyncio, Redis Stack | [`skills/redis/SKILL.md`](skills/redis/SKILL.md) |
| **django-tdd** | Use when testing Django applications with pytest - TDD workflow, pytest-django setup, factory_boy and model-bakery fixtures, DRF API testing, mocking and patching, integration tests, or coverage | [`skills/django-tdd/SKILL.md`](skills/django-tdd/SKILL.md) |
| **pytest** | Use when writing Python tests with pytest - fixtures, parametrization, markers, conftest layout, pytest-asyncio, pytest-django, coverage with pytest-cov, mocking with pytest-mock, parallel runs with xdist, or CI integration | [`skills/pytest/SKILL.md`](skills/pytest/SKILL.md) |
| **pydantic** | Use when validating and serializing Python data with Pydantic v2 - models, field and model validators, constrained and special types, TypeAdapter, discriminated unions, BaseSettings, or FastAPI integration | [`skills/pydantic/SKILL.md`](skills/pydantic/SKILL.md) |
| **tailwind** | Use when styling with Tailwind CSS v4 - @theme syntax, design token architecture, dark mode strategy, bundle size optimization, component-layer discipline, or migrating from v3 | [`skills/tailwind/SKILL.md`](skills/tailwind/SKILL.md) |

## Installation

### 1. Claude Code

**From GitHub Marketplace** (recommended):
```bash
claude plugin marketplace add https://github.com/salemaziel/oss-ai-skills
claude plugin install oss-django-stack@oss-ai-skills
```

**From Local Repository**:
```bash
claude plugin install ./plugins/oss-django-stack
```

### 2. OpenAI Codex CLI

**From GitHub Marketplace** (recommended):
```bash
codex plugin marketplace add https://github.com/salemaziel/oss-ai-skills
codex plugin add oss-django-stack@oss-ai-skills
```

**From Local Repository**:
```bash
mkdir -p ~/.codex/plugins
cp -R ./plugins/oss-django-stack ~/.codex/plugins/oss-django-stack
```

### 3. Google Antigravity CLI (`agy`)

**Using Antigravity CLI shell command**:
```bash
agy plugin install ./plugins/oss-django-stack
```

**Inside Antigravity interactive session**:
```text
/plugin install ./plugins/oss-django-stack
```

**Global workspace symlink**:
```bash
mkdir -p ~/.gemini/config/plugins
ln -s $(pwd)/plugins/oss-django-stack ~/.gemini/config/plugins/oss-django-stack
```

## Starter Prompts

- `"Use oss-django-stack to build a high-performance REST API with Django Ninja."`
- `"Use oss-django-stack to optimize database transactions and queries."`
- `"Use oss-django-stack to configure Celery task queues with Redis."`
