# Advanced Task API

Voll ausgestattete Version mit Authentifizierung, PostgreSQL (oder SQLite-Fallback), JWT, usergebundenen Tasks und Docker-Setup.

## Features
- JWT Login & Registrierung (bcrypt Hashing)
- User/Task-Relation (jede Task gehört einem User)
- PostgreSQL-ready (Standard), SQLite-Fallback für schnellen Start
- CRUD + Statuswechsel + Filter + Pagination
- Timestamps und DB-Constraints
- CORS konfigurierbar per Env
- Dockerfile & docker-compose für lokalen Start

## Struktur (Kern)
- `app/main.py` – FastAPI App, Routing, CORS, Table-Creation
- `app/core` – Config (`pydantic-settings`), Security (JWT, Password Hashing), Dependencies
- `app/db` – Engine/Session/Base
- `app/models` – SQLAlchemy Modelle (`User`, `Task`)
- `app/schemas` – Pydantic Schemas (Auth/User/Task)
- `app/api/routes` – Auth, Users, Tasks, Health

## Lokaler Start (SQLite-Fallback)
```bash
cd "3. advanced"
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Start mit Postgres via Docker
```bash
cd "3. advanced"
docker compose up --build
```
API läuft unter http://localhost:8000, Docs unter http://localhost:8000/docs.

## Env-Variablen
Kopiere `.env.example` nach `.env` (für Docker optional, da compose schon Variablen setzt):
- `SECRET_KEY` – starker Key für JWT
- `ACCESS_TOKEN_EXPIRE_MINUTES` – Token-Lebensdauer
- `DATABASE_URL` – z.B. `postgresql+psycopg2://postgres:postgres@db:5432/tasks`
- `CORS_ORIGINS` – Kommagetrennte Liste oder `*`

## Beispiel-Flow (per curl)
```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"alice@example.com","password":"secret123"}'

# Login (token holen)
TOKEN=$(curl -s -X POST http://localhost:8000/auth/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'username=alice@example.com&password=secret123' | jq -r .access_token)

# Task anlegen
curl -X POST http://localhost:8000/tasks/ \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"title":"Einkaufen"}'

# Tasks filtern (pending)
curl "http://localhost:8000/tasks?status_filter=pending" -H "Authorization: Bearer $TOKEN"
```

## Hinweise
- Für Produktion migrations (Alembic) hinzufügen; aktuell werden Tabellen beim Start erstellt.
- Für Postgres lokal ggf. Ports anpassen (`5432`).
- Tests: füge bei Bedarf Pytest-Suites hinzu; httpx ist bereits installiert.
