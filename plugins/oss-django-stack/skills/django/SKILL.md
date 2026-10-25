---
name: django
description: Use when building Django applications - security hardening, authentication and permissions, ORM optimization, PostgreSQL features, Django 6.0, migrations, testing, and ecosystem libraries
metadata:
  author: mte90
  version: 3.1.0
  tags:
    - python
    - django
    - security
    - orm
    - postgresql
    - admin
    - authentication
    - sessions
---

# Django

Comprehensive guide to Django covering security, ORM optimization, PostgreSQL features, async views, modern settings, testing, and ecosystem tools.

## Overview

Django provides a batteries-included web framework with robust features out of the box:
- **Security** — CSRF protection, session management, password hashing, security middleware, and CSP headers.
- **ORM** — Database abstraction with eager loading, window functions, and query optimization.
- **PostgreSQL Features** — Full-text search, pgvector, JSONB fields, and range types.
- **Async Execution** — ASGI views, StreamingHttpResponse, and async DB operations.
- **Django 6.0 Moderns** — Built-in Background Tasks framework, GeneratedField, and security middleware updates.

## Specialized Skills

For deep coverage of dedicated sub-domains, route to these specialized skills:

- ↳ **[django-admin](../django-admin/SKILL.md)** — Admin customizations, `save_formset`, `get_search_results`, and fieldsets.
- ↳ **[django-transaction](../django-transaction/SKILL.md)** — Transactions, `atomic`, `select_for_update`, `on_commit`, and concurrency control.

---

## Core ORM Optimization Patterns

### 1. Eliminating N+1 Queries

Always distinguish between single-object joins and multi-object prefetching:

```python
# select_related for single-valued relationships (ForeignKey, OneToOne) -> SQL JOIN
queryset = Article.objects.select_related("author", "category").filter(is_published=True)

# prefetch_related for multi-valued relationships (ManyToMany, reverse ForeignKey) -> Separate queries
queryset = Article.objects.prefetch_related(
    "tags",
    Prefetch("comments", queryset=Comment.objects.select_related("user").order_by("-created_at")),
)
```

### 2. Restricting Loaded Columns (Memory & Network)

Avoid pulling entire text/JSON columns into memory when only IDs or names are needed:

```python
# Load only specific fields
queryset = User.objects.only("id", "username", "email")

# Defer expensive columns
queryset = Document.objects.defer("raw_content", "binary_data")

# Avoid model instantiation overhead for read-only aggregation
summaries = Article.objects.values("category__name").annotate(count=Count("id"))
```

### 3. Bulk Batch Operations

Never save models inside loops; batch operations reduce database roundtrips:

```python
# Bulk insertion with batch sizing
articles = [Article(title=f"Article {i}", author_id=user_id) for i in range(1000)]
Article.objects.bulk_create(articles, batch_size=200, ignore_conflicts=True)

# Bulk update with targeted fields
for article in existing_articles:
    article.is_reviewed = True
Article.objects.bulk_update(existing_articles, fields=["is_reviewed"], batch_size=200)
```

### 4. Streaming Large Datasets

Prevent process OOM when exporting or processing massive tables:

```python
# Stream querysets with fixed chunk buffer
for record in LargeDataset.objects.iterator(chunk_size=2000):
    process_record(record)
```

---

## Modern Production Settings Baseline

Configure robust security and connection pooling in `settings.py`:

```python
import os

# Security headers & SSL
SECURE_SSL_REDIRECT = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"

# Persistent database connections (PostgreSQL)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "app_db"),
        "USER": os.environ.get("DB_USER", "postgres"),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
        "CONN_MAX_AGE": 600,  # Re-use connections up to 10 minutes
        "CONN_HEALTH_CHECKS": True,
    }
}
```

---

## Async Views & Sync-Async Boundary

Django supports native `async def` views under ASGI. When interacting with the synchronous ORM, always use async ORM methods or `sync_to_async`:

```python
from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.shortcuts import aget_object_or_404
from .models import Article

# Native async view
async def article_detail_view(request, pk: int):
    # Use native async ORM methods (Django 4.2+)
    article = await aget_object_or_404(Article, pk=pk)
    
    # Wrap synchronous library calls with sync_to_async
    payload = await sync_to_async(external_billing_check)(article.author_id)
    
    return JsonResponse({"id": article.id, "title": article.title, "status": payload})
```

---

## Testing with pytest-django

Use `pytest-django` fixtures for isolated, transaction-safe tests:

```python
import pytest
from django.urls import reverse
from .models import Article

@pytest.mark.django_db
def test_article_published_filtering(client, user_factory):
    author = user_factory.create()
    Article.objects.create(title="Draft", author=author, is_published=False)
    published = Article.objects.create(title="Published", author=author, is_published=True)

    url = reverse("articles:list")
    response = client.get(url)

    assert response.status_code == 200
    assert len(response.context["articles"]) == 1
    assert response.context["articles"][0].id == published.id
```

---

## Common Pitfalls & Antipatterns

| Antipattern | Problem | Recommended Solution |
|---|---|---|
| Query evaluation inside template loops | Hidden N+1 queries during rendering | Pre-fetch related objects using `select_related` / `prefetch_related` in view. |
| In-memory filtering of QuerySets (`[a for a in qs if a.x]`) | Loads entire table into Python memory | Apply filter in database: `qs.filter(x=True)`. |
| `count()` after `len(qs)` | Double evaluation | Use `len(qs)` if you will iterate anyway; use `qs.count()` if checking size only. |
| Raw SQL with string formatting `f"SELECT ... {id}"` | Critical SQL injection risk | Use parameter binding: `cursor.execute("SELECT ... WHERE id = %s", [id])`. |
| Long-running tasks inside views | Blocks request worker thread | Offload tasks to Celery or Django 6 Tasks framework. |

---

## Deep Dives

Load these reference files on demand for in-depth coverage:

- ↳ **[references/security.md](references/security.md)** — CSRF protection, sessions, security middleware, and field-level encryption.
- ↳ **[references/authentication-permissions.md](references/authentication-permissions.md)** — Auth views, custom backends, password hashing, and permissions.
- ↳ **[references/orm-performance.md](references/orm-performance.md)** — Deep ORM optimization, query explain, and caching patterns.
- ↳ **[references/postgresql.md](references/postgresql.md)** — pgvector, GeneratedField, GeoDjango, and PostgreSQL features.
- ↳ **[references/django6-modern.md](references/django6-modern.md)** — Django Tasks framework, 6.0 essentials, and multi-DB routing.
- ↳ **[references/testing-migrations.md](references/testing-migrations.md)** — Testing optimization, migration squashing, signals, and StreamingHttpResponse.
- ↳ **[references/external-api.md](references/external-api.md)** — Operational dashboards and third-party API integration.
- ↳ **[references/ecosystem.md](references/ecosystem.md)** — Curated Django ecosystem packages and extensions.
