from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


# Basismodell
class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task Titel")
    done: bool = Field(False, description="Status der Task")


# Für POST (ohne ID)
class TaskCreate(TaskBase):
    pass


# Für PUT/PATCH - optionale Felder
class TaskUpdate(BaseModel):
    title: Optional[str] = Field(
        None, min_length=1, max_length=100, description="Neuer Task Titel"
    )
    done: Optional[bool] = Field(None, description="Neuer Status der Task")


# Für Antworten (mit ID und Timestamps)
class Task(TaskBase):
    id: int = Field(..., description="Task ID")
    created_at: datetime = Field(..., description="Erstellungszeitpunkt")
    updated_at: datetime = Field(..., description="Letzter Update")

    class Config:
        from_attributes = True  # Ersetzt orm_mode in Pydantic v2
