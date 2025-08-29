from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyHttpUrl, SecretStr, field_validator
from typing import List

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    # General
    ENV: str = "development"
    APP_NAME: str = "fastapi-telegram-pro"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    ALLOWED_ORIGINS: List[AnyHttpUrl] = []

    # Telegram
    TELEGRAM_BOT_TOKEN: SecretStr
    TELEGRAM_WEBHOOK_URL: AnyHttpUrl
    TELEGRAM_WEBHOOK_SECRET_TOKEN: SecretStr

    # Database
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_NAME: str

    # Redis
    REDIS_URL: str

    # Security
    JWT_SECRET: SecretStr
    JWT_ALG: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # Logging
    LOG_LEVEL: str = "INFO"

    # Validator for ALLOWED_ORIGINS
    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def split_allowed_origins(cls, v):
        if isinstance(v, str):
            return [x.strip() for x in v.split(",")]
        return v

settings = Settings()
