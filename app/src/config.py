import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "modern-devops-platform")
    ENV: str = os.getenv("ENV", "dev")
    PORT: int = int(os.getenv("PORT", 8000))

settings = Settings()