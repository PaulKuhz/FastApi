# Paul's FastAPI Task Manager 📋

Ein **progressives FastAPI Lernprojekt** mit drei Schwierigkeitsstufen – von einfacher In-Memory API über Datenbankanbindung bis hin zu Authentifizierung und Docker-Deployment.

## 🎯 Übersicht

Jede Stufe baut auf der vorherigen auf und lehrt neue Konzepte:

| Stufe | Ordner | Fokus | Features |
|-------|--------|-------|----------|
| **Easy** | `1. easy/` | Grundlagen | REST API, CRUD, Pydantic, OpenAPI |
| **Intermediate** | `2. intermediate/` | Persistenz | SQLite, SQLAlchemy ORM, Timestamps, Sessions |
| **Advanced** | `3. advanced/` | Production | JWT Auth, PostgreSQL, User-Isolation, Docker, Tests |

---

## 🟢 **Easy Version** — Die Basics

**Ideal zum Lernen:** Alles läuft in-memory, keine DB nötig.

### Features
- ✅ Vollständige REST API (GET, POST, PUT, PATCH, DELETE)
- ✅ Pydantic Datenmodelle & Validierung
- ✅ Professional HTTP Status Codes (201, 204, 404, 400)
- ✅ Swagger/OpenAPI Dokumentation (`/docs`)
- ✅ Task Status Management (complete/incomplete)
- ✅ Status Filterung (completed/pending)

### Tech Stack
- FastAPI 0.104.1
- Pydantic 2.5.0
- Uvicorn 0.24.0

### Quick Start
```bash
cd "1. easy"
pip install -r requirements.txt
uvicorn main:app --reload
```

**Docs:** http://localhost:8000/docs

[→ Detailliert: Easy README](1.%20easy/README.md)

---

## 🟡 **Intermediate Version** — Datenbank Integration

**Erste echte Persistenz:** SQLite + SQLAlchemy ORM, Sessions, Dependency Injection.

### Neue Features (vs. Easy)
- ✅ SQLite Datenbank (Tasks überleben Restarts)
- ✅ SQLAlchemy ORM für sichere DB-Zugriffe
- ✅ Timestamps (`created_at`, `updated_at`) auto server-side
- ✅ Database Sessions via Dependency Injection
- ✅ Saubere Schema-Separation (Models, Schemas)
- ✅ Bessere Fehlerbehandlung

### Tech Stack
- FastAPI 0.104.1
- SQLAlchemy 2.0.23
- Pydantic 2.5.0
- SQLite (datei-basiert)

### Quick Start
```bash
cd "2. intermediate"
pip install -r requirements.txt
uvicorn main:app --reload
```

**Docs:** http://localhost:8000/docs  
**DB:** `tasks.db` (automatisch erstellt)

[→ Detailliert: Intermediate README](2.%20intermediate/README.md)

---

## 🔴 **Advanced Version** — Production Ready

**Alles inklusive:** JWT Auth, PostgreSQL, User-Isolation, Docker, Tests, Pagination.

### Neue Features (vs. Intermediate)
- ✅ **JWT Login & Registration** (bcrypt Hashing)
- ✅ **PostgreSQL** (via Docker, SQLite-Fallback lokal)
- ✅ **User-Task Relation** (Jede Task gehört einem User)
- ✅ **CORS konfigurierbar** (per Env)
- ✅ **Pagination & Filtering** (limit, offset, status_filter)
- ✅ **Docker & docker-compose** (Production-style Setup)
- ✅ **Pytest Tests** (Smoke Tests, erweiterbar)
- ✅ **Environment-basierte Config** (`.env` Support)

### Tech Stack
- FastAPI 0.104.1
- SQLAlchemy 2.0.23
- PostgreSQL 15 (oder SQLite-Fallback)
- JWT / python-jose / passlib (bcrypt)
- Docker & docker-compose
- Pytest

### Quick Start (SQLite-Fallback, lokal)
```bash
cd "3. advanced"
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Quick Start (PostgreSQL via Docker)
```bash
cd "3. advanced"
docker compose up --build
```

**Docs:** http://localhost:8000/docs  
**Postgres:** `localhost:5432` (user: postgres, pwd: postgres)

[→ Detailliert: Advanced README](3.%20advanced/README.md)

---

## 📊 Feature Vergleich

```
                    Easy    Intermediate  Advanced
────────────────────────────────────────────────────
In-Memory           ✅      ❌            ❌
SQLite              ❌      ✅            ✅
PostgreSQL          ❌      ❌            ✅
JWT Auth            ❌      ❌            ✅
User Isolation      ❌      ❌            ✅
Timestamps          ❌      ✅            ✅
Pagination          ❌      ❌            ✅
Docker              ❌      ❌            ✅
Tests               ❌      ❌            ✅
```

---

## 🚀 Wie funktioniert das Lernen?

1. **Starte mit Easy** – verstehe REST API & Pydantic
2. **Lese Intermediate** – lerne Datenbanken & ORM
3. **Experimentiere mit Advanced** – bau Auth & Docker ein

Jede Version ist **standalone lauffähig** – du kannst jederzeit switchen.

---

## 📋 Beispiel API Calls (Easy Version)

```bash
# Task erstellen
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Einkaufen gehen","done":false}'

# Alle Tasks abrufen
curl http://localhost:8000/tasks

# Task als erledigt markieren
curl -X PATCH http://localhost:8000/tasks/1/complete

# Nur offene Tasks
curl http://localhost:8000/tasks/status/pending
```

---

## 🔐 Beispiel Auth Flow (Advanced Version)

```bash
# User registrieren
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"secret123"}'

# Token holen
TOKEN=$(curl -s -X POST http://localhost:8000/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'username=alice@example.com&password=secret123' | jq -r .access_token)

# Task erstellen (mit Auth)
curl -X POST http://localhost:8000/tasks/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Wichtig","done":false}'

# Meine Tasks abrufen
curl http://localhost:8000/tasks -H "Authorization: Bearer $TOKEN"
```

---

## 📁 Repository Struktur

```
API Project/
├── 1. easy/
│   ├── main.py              # FastAPI App + Endpoints
│   ├── requirements.txt
│   └── README.md
├── 2. intermediate/
│   ├── main.py              # App mit DB-Integration
│   ├── database.py           # SQLAlchemy Engine/Session
│   ├── models.py             # Task ORM Model
│   ├── schemas.py            # Pydantic Schemas
│   ├── requirements.txt
│   └── README.md
├── 3. advanced/
│   ├── app/
│   │   ├── main.py           # App-Entry mit CORS/Tables
│   │   ├── core/
│   │   │   ├── config.py      # Pydantic Settings
│   │   │   ├── security.py    # JWT + Bcrypt
│   │   │   └── deps.py        # Auth Dependencies
│   │   ├── db/
│   │   │   ├── session.py     # Engine/Session
│   │   │   └── base.py        # ORM Base
│   │   ├── models/
│   │   │   ├── user.py        # User Model
│   │   │   └── task.py        # Task Model
│   │   ├── schemas/
│   │   │   ├── auth.py        # Token Schemas
│   │   │   ├── user.py        # User Schemas
│   │   │   └── task.py        # Task Schemas
│   │   └── api/
│   │       ├── api.py         # Router Registration
│   │       └── routes/
│   │           ├── auth.py    # Register/Login
│   │           ├── users.py   # Current User
│   │           ├── tasks.py   # CRUD + Filters
│   │           └── health.py  # Health Check
│   ├── tests/
│   │   └── test_smoke.py
│   ├── .env.example
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── requirements.txt
│   └── README.md
└── README.md (this file)
```

---

## 🎓 Was lernst du?

### Easy
- REST API Design (HTTP Verben, Status Codes)
- Pydantic Validation & Schemas
- FastAPI Basics (Routing, Dependencies)
- OpenAPI/Swagger Documentation

### Intermediate
- SQLAlchemy ORM & Sessions
- Datenbankdesign & Relationships
- Dependency Injection Pattern
- Server-side Timestamps & Constraints

### Advanced
- JWT Authentication & Authorization
- Password Hashing (bcrypt)
- User-based Data Isolation
- Environment-based Configuration
- Docker & containerization
- Testing Best Practices
- Production-ready Patterns

---

## 🔧 Anforderungen

- Python 3.10+ (3.11+ empfohlen)
- pip/venv
- Docker & docker-compose (nur für Advanced mit PostgreSQL)

---

## 💡 Tipps

- **Lokal schnell testen:** Nutze Easy oder Advanced mit SQLite-Fallback.
- **Mit Postgres experimentieren:** `cd "3. advanced" && docker compose up`.
- **Dokumentation anschauen:** Öffne `/docs` nach dem Start.
- **Weiterprogrammieren:** Verändere Schemas, Models, Routes und schau, was passiert.

---

## 📖 Weiterführende Ressourcen

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [SQLAlchemy Docs](https://docs.sqlalchemy.org/)
- [Python JWT](https://python-jose.readthedocs.io/)

---

## 👨‍💻 Autor

Paul Schumacher

---

**Viel Spaß beim Lernen!** 🚀
