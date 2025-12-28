from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

# Starte die App mit mehr Informationen
app = FastAPI(
    title="Paul's Task API - Easy Version",
    description="Eine einfache Task-Management API",
    version="1.0.0",
)


# Definiere dein Datenmodell
class Task(BaseModel):
    id: Optional[int] = Field(None, description="Task ID (wird automatisch generiert)")
    title: str = Field(..., min_length=1, max_length=100, description="Task Titel")
    done: bool = Field(False, description="Status der Task")

    class Config:
        schema_extra = {"example": {"title": "Einkaufen gehen", "done": False}}  # type: ignore


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task Titel")
    done: bool = Field(False, description="Status der Task")


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        None, min_length=1, max_length=100, description="Neuer Task Titel"
    )
    done: Optional[bool] = Field(None, description="Neuer Status der Task")


# Temporärer Speicher (statt Datenbank)
tasks: List[Task] = []
next_id = 1


# Root-Endpunkt
@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to Paul's Task API!",
        "docs": "/docs",
        "version": "1.0.0",
    }


# GET alle Tasks
@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_tasks():
    """
    Gibt alle Tasks zurück
    """
    return tasks


# GET eine spezifische Task
@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: int):
    """
    Gibt eine spezifische Task basierend auf der ID zurück
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )
    return task


# POST neue Task
@app.post(
    "/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"]
)
def create_task(task_data: TaskCreate):
    """
    Erstellt eine neue Task
    """
    global next_id

    new_task = Task(id=next_id, title=task_data.title, done=task_data.done)

    tasks.append(new_task)
    next_id += 1

    return new_task


# PUT Task aktualisieren
@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, task_update: TaskUpdate):
    """
    Aktualisiert eine existierende Task
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    if task_update.title is not None:
        task.title = task_update.title
    if task_update.done is not None:
        task.done = task_update.done

    return task


# DELETE Task löschen
@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int):
    """
    Löscht eine Task basierend auf der ID
    """
    global tasks
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    tasks = [t for t in tasks if t.id != task_id]
    return None


# Gesonderte Endpunkte für Task-Status
@app.patch("/tasks/{task_id}/complete", response_model=Task, tags=["Tasks"])
def mark_task_complete(task_id: int):
    """
    Markiert eine Task als erledigt
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    task.done = True
    return task


@app.patch("/tasks/{task_id}/incomplete", response_model=Task, tags=["Tasks"])
def mark_task_incomplete(task_id: int):
    """
    Markiert eine Task als nicht erledigt
    """
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden",
        )

    task.done = False
    return task


# Hilfsfunktion um Tasks nach Status zu filtern
@app.get("/tasks/status/{status_filter}", response_model=List[Task], tags=["Tasks"])
def get_tasks_by_status(status_filter: str):
    """
    Filtert Tasks nach Status (completed/pending)
    """
    if status_filter not in ["completed", "pending"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Status muss 'completed' oder 'pending' sein",
        )

    if status_filter == "completed":
        return [task for task in tasks if task.done]
    else:
        return [task for task in tasks if not task.done]