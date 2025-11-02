from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session  # type: ignore[import]
from typing import List
import models
import schemas
from database import SessionLocal, engine  # type: ignore

# Tabellen erzeugen (falls noch nicht vorhanden)
models.Base.metadata.create_all(bind=engine)  # type: ignore

app = FastAPI(
    title="Paul's Task API - Intermediate Version",
    description="Eine erweiterte Task-Management API mit SQLite Datenbank",
    version="2.0.0",
)


# DB-Session bereitstellen
def get_db():  # type: ignore
    db = SessionLocal()  # type: ignore
    try:
        yield db
    finally:
        db.close()  # type: ignore


# Root-Endpunkt
@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to Paul's Intermediate Task API!",
        "docs": "/docs",
        "version": "2.0.0",
        "database": "SQLite",
    }


# CREATE - Neue Task erstellen
@app.post(
    "/tasks",
    response_model=schemas.Task,
    status_code=status.HTTP_201_CREATED,
    tags=["Tasks"],
)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):  # type: ignore
    """Erstellt eine neue Task in der Datenbank"""
    db_task = models.Task(title=task.title, done=task.done)  # type: ignore
    db.add(db_task)  # type: ignore
    db.commit()  # type: ignore
    db.refresh(db_task)  # type: ignore
    return db_task


# READ ALL - Alle Tasks abrufen
@app.get("/tasks", response_model=List[schemas.Task], tags=["Tasks"])
def get_tasks(db: Session = Depends(get_db)):  # type: ignore
    """Gibt alle Tasks aus der Datenbank zurück"""
    return db.query(models.Task).all()  # type: ignore


# READ ONE - Eine spezifische Task abrufen
@app.get("/tasks/{task_id}", response_model=schemas.Task, tags=["Tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):  # type: ignore
    """Gibt eine spezifische Task basierend auf der ID zurück"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()  # type: ignore
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )
    return task  # type: ignore


# UPDATE - Task aktualisieren
@app.put("/tasks/{task_id}", response_model=schemas.Task, tags=["Tasks"])
def update_task(  # type: ignore
    task_id: int, updated_task: schemas.TaskUpdate, db: Session = Depends(get_db)  # type: ignore
):
    """Aktualisiert eine existierende Task"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()  # type: ignore
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    # Nur aktualisieren, wenn Werte angegeben sind
    if updated_task.title is not None:
        task.title = updated_task.title  # type: ignore
    if updated_task.done is not None:
        task.done = updated_task.done  # type: ignore

    db.commit()  # type: ignore
    db.refresh(task)  # type: ignore
    return task  # type: ignore


# DELETE - Task löschen
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):  # type: ignore
    """Löscht eine Task basierend auf der ID"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()  # type: ignore
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )
    db.delete(task)  # type: ignore
    db.commit()  # type: ignore
    return None


# PATCH - Task als erledigt markieren
@app.patch("/tasks/{task_id}/complete", response_model=schemas.Task, tags=["Tasks"])
def mark_task_complete(task_id: int, db: Session = Depends(get_db)):  # type: ignore
    """Markiert eine Task als erledigt"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()  # type: ignore
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    task.done = True  # type: ignore
    db.commit()  # type: ignore
    db.refresh(task)  # type: ignore
    return task  # type: ignore


# PATCH - Task als nicht erledigt markieren
@app.patch("/tasks/{task_id}/incomplete", response_model=schemas.Task, tags=["Tasks"])
def mark_task_incomplete(task_id: int, db: Session = Depends(get_db)):  # type: ignore
    """Markiert eine Task als nicht erledigt"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()  # type: ignore
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    task.done = False  # type: ignore
    db.commit()  # type: ignore
    db.refresh(task)  # type: ignore
    return task  # type: ignore


# GET - Tasks nach Status filtern
@app.get(
    "/tasks/status/{status_filter}", response_model=List[schemas.Task], tags=["Tasks"]
)
def get_tasks_by_status(status_filter: str, db: Session = Depends(get_db)):  # type: ignore
    """Filtert Tasks nach Status (completed/pending)"""
    if status_filter not in ["completed", "pending"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Status muss 'completed' oder 'pending' sein",
        )

    if status_filter == "completed":
        return db.query(models.Task).filter(models.Task.done.is_(True)).all()  # type: ignore
    else:
        return db.query(models.Task).filter(models.Task.done.is_(False)).all()  # type: ignore
