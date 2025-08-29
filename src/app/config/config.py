import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("ENV")
APP_NAME = os.getenv("APP_NAME")
APP_HOST = os.getenv("APP_HOST")
APP_PORT = os.getenv("APP_PORT")

ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "").split(",")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_WEBHOOK_URL = os.getenv("TELEGRAM_WEBHOOK_URL")
TELEGRAM_WEBHOOK_SECRET_TOKEN = os.getenv("TELEGRAM_WEBHOOK_SECRET_TOKEN")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

REDIS_URL = os.getenv("REDIS_URL")

JWT_SECRET = os.getenv("JWT_SECRET")
JWT_ALG = os.getenv("JWT_ALG", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
