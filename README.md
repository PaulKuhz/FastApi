# Paul's FastAPI Task Manager 📋

Eine einfache Task-Management API erstellt mit FastAPI.

## ✨ Features

- ✅ CRUD Operationen für Tasks (Create, Read, Update, Delete)
- 🔍 Tasks nach Status filtern (completed/pending)
- 📚 Automatische API-Dokumentation
- ✏️ Vollständige Task-Verwaltung
- 🚀 Schnelle und moderne API mit FastAPI

## 🛠️ Installation

1. **Repository klonen:**
```bash
git clone https://github.com/DEIN-USERNAME/fastapi-task-api.git
cd fastapi-task-api
```

2. **Virtual Environment erstellen:**
```bash
python -m venv venv
source venv/bin/activate  # Auf Windows: venv\Scripts\activate
```

3. **Dependencies installieren:**
```bash
pip install fastapi uvicorn
```

## 🚀 Starten

```bash
uvicorn main:app --reload
```

Die API ist dann verfügbar unter:
- **API:** http://localhost:8000
- **Dokumentation:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

## 📖 API Endpunkte

### Tasks verwalten:
- `GET /tasks` - Alle Tasks abrufen
- `GET /tasks/{id}` - Eine spezifische Task abrufen
- `POST /tasks` - Neue Task erstellen
- `PUT /tasks/{id}` - Task aktualisieren
- `DELETE /tasks/{id}` - Task löschen

### Task Status:
- `PATCH /tasks/{id}/complete` - Task als erledigt markieren
- `PATCH /tasks/{id}/incomplete` - Task als nicht erledigt markieren
- `GET /tasks/status/completed` - Nur erledigte Tasks
- `GET /tasks/status/pending` - Nur offene Tasks

## 📝 Beispiel Verwendung

```python
# Neue Task erstellen
POST /tasks
{
    "title": "Einkaufen gehen",
    "done": false
}

# Task aktualisieren
PUT /tasks/1
{
    "title": "Einkaufen erledigt",
    "done": true
}
```

## 🛠️ Technologien

- **FastAPI** - Modernes Python Web Framework
- **Pydantic** - Datenvalidierung und -serialisierung
- **Uvicorn** - ASGI Server

## 👨‍💻 Autor

Paul Schumacher

---

*Erstellt im November 2025* 🚀