from fastapi import FastAPI
from app.src.config import settings
from app.src.routes import health


app = FastAPI(title=settings.APP_NAME)

app.include_router(health.router)