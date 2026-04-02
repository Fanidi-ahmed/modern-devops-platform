from fastapi import FastAPI

from app.src.config import settings
from app.src.routes import health, users
from app.src.database import Base, engine
from prometheus_fastapi_instrumentator import Instrumentator

Instrumentator().instrument(app).expose(app)
Base.metadata.create_all(bind=engine)
app = FastAPI(title=settings.APP_NAME)

app.include_router(health.router)
app.include_router(users.router)