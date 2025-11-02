from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

# FastAPI App mit mehr Details
app = FastAPI(
    title="Intermediate Task API",
    description="Eine erweiterte Task-Management API mit besserer Fehlerbehandlung",
    version="2.0.0",
)

# Erweiterte Datenmodelle
class Task(BaseModel):
    id: Optional[int] = None
    title: str = Field(..., min_length=1, max_length=100)
    done: bool = Field(default=False)
    
    class Config:
        schema_extra = {"example": {"title": "Einkaufen gehen", "done": False}}

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    done: bool = Field(default=False)

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    done: Optional[bool] = None

# Temporärer Speicher
tasks: List[Task] = []
next_id = 1

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to Intermediate Task API!",
        "docs": "/docs",
        "version": "2.0.0"
    }

@app.get("/tasks", response_model=List[Task], tags=["Tasks"])
def get_tasks():
    """Alle Tasks abrufen"""
    return tasks

@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: int):
    """Eine spezifische Task abrufen"""
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden"
        )
    return task

@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(task_data: TaskCreate):
    """Neue Task erstellen"""
    global next_id
    new_task = Task(id=next_id, title=task_data.title, done=task_data.done)
    tasks.append(new_task)
    next_id += 1
    return new_task

@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, task_update: TaskUpdate):
    """Task aktualisieren"""
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden"
        )
    
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.done is not None:
        task.done = task_update.done
    
    return task

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int):
    """Task löschen"""
    global tasks
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden"
        )
    
    tasks = [t for t in tasks if t.id != task_id]

@app.patch("/tasks/{task_id}/complete", response_model=Task, tags=["Tasks"])
def mark_task_complete(task_id: int):
    """Task als erledigt markieren"""
    task = next((t for t in tasks if t.id == task_id), None)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task mit ID {task_id} nicht gefunden"
        )
    
    task.done = True
    return task