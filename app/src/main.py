from fastapi import FastAPI

from app.src.config import settings
from app.src.routes import health, users

app = FastAPI(title=settings.APP_NAME)

app.include_router(health.router)
app.include_router(users.router)