from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api import api_router
from app.core.config import settings
from app.db.session import Base, engine
import app.db.base  # noqa: F401

# Create tables (for simple setup; for production prefer migrations)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="Advanced Task API with auth, Postgres-ready DB, and user-owned tasks",
    version=settings.version,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to the Advanced Task API",
        "docs": "/docs",
        "version": settings.version,
    }


app.include_router(api_router)
