import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENV = os.getenv("ENV", "development")
    APP_NAME = os.getenv("APP_NAME", "fastapi-telegram-pro")
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = int(os.getenv("APP_PORT", 8000))

    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "")
    if ALLOWED_ORIGINS:
        ALLOWED_ORIGINS = [o.strip() for o in ALLOWED_ORIGINS.split(",")]
    else:
        ALLOWED_ORIGINS = []

    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    TELEGRAM_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
    TELEGRAM_WEBHOOK_SECRET_TOKEN = os.getenv("TELEGRAM_WEBHOOK_SECRET_TOKEN")

    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 3306))
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")

    REDIS_URL = os.getenv("REDIS_URL")

    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALG = os.getenv("JWT_ALG", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

settings = Settings()
