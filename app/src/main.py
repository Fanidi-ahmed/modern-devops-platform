from fastapi import FastAPI

from app.src.config import settings
from app.src.database import Base, engine
from app.src.models.user import User
from app.src.routes import health, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.include_router(health.router)
app.include_router(users.router)