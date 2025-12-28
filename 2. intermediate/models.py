# type: ignore[import]
from sqlalchemy import Column, Integer, String, Boolean, DateTime  # type: ignore
from sqlalchemy.sql import func  # type: ignore
from database import Base  # type: ignore


class Task(Base):  # type: ignore
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # type: ignore
    title = Column(String(100), nullable=False, index=True)  # type: ignore
    done = Column(Boolean, default=False, nullable=False)  # type: ignore
    created_at = Column(  # type: ignore
        DateTime(timezone=True),
        server_default=func.now(),  # type: ignore
        nullable=False,
    )
    updated_at = Column(  # type: ignore
        DateTime(timezone=True),
        server_default=func.now(),  # type: ignore
        onupdate=func.now(),  # type: ignore
        nullable=False,
    )
