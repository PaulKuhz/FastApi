from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.orm import sessionmaker, declarative_base  # type: ignore

# SQLite-Datenbank im Projektordner
DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})  # type: ignore
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # type: ignore

Base = declarative_base()  # type: ignore
