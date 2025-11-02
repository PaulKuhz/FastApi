# Easy Task API

Die Basis-Version von Paul's Task API - vollständige REST API Implementation.

## Features
- ✅ Vollständige CRUD Operationen (Create, Read, Update, Delete)
- ✅ Professionelle HTTP Status Codes
- ✅ Umfassende Fehlerbehandlung
- ✅ Pydantic Datenvalidierung
- ✅ API Dokumentation mit Swagger/OpenAPI
- ✅ Task Status Management (complete/incomplete)
- ✅ Task Filterung nach Status

## Installation

```bash
cd easy
pip install -r requirements.txt
uvicorn main:app --reload
```

## API Endpunkte

### Basis
- `GET /` - Willkommensnachricht
- `GET /docs` - Automatische API Dokumentation

### Tasks CRUD
- `GET /tasks` - Alle Tasks abrufen
- `GET /tasks/{id}` - Spezifische Task abrufen
- `POST /tasks` - Neue Task erstellen
- `PUT /tasks/{id}` - Task aktualisieren
- `DELETE /tasks/{id}` - Task löschen

### Task Status
- `PATCH /tasks/{id}/complete` - Task als erledigt markieren
- `PATCH /tasks/{id}/incomplete` - Task als nicht erledigt markieren
- `GET /tasks/status/completed` - Nur erledigte Tasks
- `GET /tasks/status/pending` - Nur offene Tasks

## Nächste Schritte

Schaue dir die `intermediate` und `advanced` Versionen an für erweiterte Features!
