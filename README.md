# Paul's FastAPI Task Manager 📋

Ein progressives FastAPI Lernprojekt mit drei Schwierigkeitsstufen.

## 📂 Projekt Struktur

Dieses Repository enthält drei verschiedene Implementierungen der gleichen Task API:

### 🟢 Easy (`/easy/`)
Die Basis-Version mit allen wichtigen Features:
- Vollständige REST API Implementation
- CRUD Operationen (Create, Read, Update, Delete)
- Professional HTTP Status Codes
- Pydantic Datenvalidierung
- Swagger/OpenAPI Dokumentation

### 🟡 Intermediate (`/intermediate/`)
*Work in Progress - Erweiterte Features geplant*

### � Advanced (`/advanced/`)  
*Work in Progress - Fortgeschrittene Features geplant*

## � Quick Start

Wähle eine Version und starte:

```bash
# Easy Version
cd easy
pip install -r requirements.txt
uvicorn main:app --reload

# Intermediate Version (wenn fertig)
cd intermediate
pip install -r requirements.txt
uvicorn main:app --reload

# Advanced Version (wenn fertig)
cd advanced
pip install -r requirements.txt
uvicorn main:app --reload
```

Die API ist dann verfügbar unter:
- **API:** http://localhost:8000
- **Dokumentation:** http://localhost:8000/docs

## 📖 API Endpunkte (Easy Version)

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

## 🛠️ Technologien

- **FastAPI** - Modernes Python Web Framework
- **Pydantic** - Datenvalidierung und -serialisierung
- **Uvicorn** - ASGI Server

## 👨‍💻 Autor

Paul Schumacher

---

*Erstellt im November 2025* 🚀