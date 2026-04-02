from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.src.config import settings
from app.src.routes import health, users

app = FastAPI(title=settings.APP_NAME)


Instrumentator().instrument(app).expose(app)


app.include_router(health.router)
app.include_router(users.router)