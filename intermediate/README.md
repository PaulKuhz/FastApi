# Intermediate Task API

Die erweiterte Version von Paul's Task API mit SQLite Datenbank Integration.

## 🆕 Neue Features (vs. Easy Version)

### Datenbank Integration
- ✅ **SQLite Datenbank** statt In-Memory Speicher
- ✅ **Persistente Datenspeicherung** - Tasks bleiben nach Neustart erhalten
- ✅ **SQLAlchemy ORM** für Datenbank-Operations
- ✅ **Automatische Migrations** - Tabellen werden automatisch erstellt

### Erweiterte Datenmodelle
- ✅ **Timestamps** - `created_at` und `updated_at` für jede Task
- ✅ **Bessere Validierung** mit Pydantic v2
- ✅ **Separate Schema-Klassen** für verschiedene Operations
- ✅ **Database Constraints** - String-Längen, Nullable-Constraints

### Verbesserte API
- ✅ **Vollständige CRUD Operationen** mit Datenbankanbindung
- ✅ **Bessere Fehlerbehandlung** mit detaillierten Meldungen
- ✅ **Status-Filter Endpunkte** funktionieren mit der DB
- ✅ **Dependency Injection** für Database Sessions

## 🛠️ Installation & Setup

```bash
cd intermediate

# Virtual Environment erstellen (empfohlen)
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate  # Windows

# Dependencies installieren
pip install -r requirements.txt

# API starten
uvicorn main:app --reload
```

## 🚀 API verfügbar unter:
- **API:** http://localhost:8000
- **Dokumentation:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

## 📖 API Endpunkte

### Basis
- `GET /` - API Information & Versionsnummer

### Tasks CRUD (mit Datenbank)
- `GET /tasks` - Alle Tasks aus der Datenbank
- `GET /tasks/{id}` - Spezifische Task aus der DB
- `POST /tasks` - Neue Task in die DB speichern
- `PUT /tasks/{id}` - Task in der DB aktualisieren (partial updates)
- `DELETE /tasks/{id}` - Task aus der DB löschen

### Task Status Management
- `PATCH /tasks/{id}/complete` - Task als erledigt markieren
- `PATCH /tasks/{id}/incomplete` - Task als nicht erledigt markieren

### Filterung & Suche
- `GET /tasks/status/completed` - Nur erledigte Tasks aus der DB
- `GET /tasks/status/pending` - Nur offene Tasks aus der DB

## 📊 Datenmodell

```json
{
  "id": 1,
  "title": "Einkaufen gehen", 
  "done": false,
  "created_at": "2025-11-02T10:30:00Z",
  "updated_at": "2025-11-02T10:30:00Z"
}
```

## 🗄️ Datenbank

- **Engine:** SQLite 
- **Datei:** `tasks.db` (wird automatisch erstellt)
- **ORM:** SQLAlchemy
- **Migrations:** Automatisch bei App-Start

## 🔧 Tech Stack

- **FastAPI** 0.104.1 - Modern Python Web Framework
- **SQLAlchemy** 2.0.23 - Python SQL ORM 
- **Pydantic** 2.5.0 - Data validation using Python type annotations
- **Uvicorn** 0.24.0 - ASGI server implementation
- **SQLite** - File-based SQL database

## 🆚 Vergleich mit Easy Version

| Feature | Easy | Intermediate |
|---------|------|-------------|
| Datenspeicher | In-Memory | SQLite DB |
| Persistierung | ❌ | ✅ |
| Timestamps | ❌ | ✅ |
| DB Constraints | ❌ | ✅ |
| Partial Updates | ❌ | ✅ |
| Performance | Basic | Verbessert |

## 🎯 Nächste Schritte

Schaue dir die `advanced` Version an für:
- PostgreSQL Integration
- User Authentication & JWT
- File Uploads
- Background Tasks
- Rate Limiting
- API Versioning