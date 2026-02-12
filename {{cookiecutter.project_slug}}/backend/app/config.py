"""Application configuration management using Pydantic Settings."""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Application settings
    APP_NAME: str = "{{ cookiecutter.project_name }}"
    APP_DESCRIPTION: str = "{{ cookiecutter.project_description }}"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False

    # Server configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database configuration
    {%- if cookiecutter.use_postgresql == 'y' %}
    DATABASE_URL: str = "postgresql+asyncpg://{{ cookiecutter.db_user }}:password@localhost:5432/{{ cookiecutter.db_name }}"
    {%- else %}
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    {%- endif %}

    # CORS configuration
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8001",
    ]

    # JWT configuration (optional)
    JWT_SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24

    # Email configuration (optional)
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""

    # Redis configuration (optional)
    REDIS_URL: str = "redis://localhost:6379"
    CACHE_ENABLED: bool = False

    # Logging
    LOG_LEVEL: str = "INFO"

    class Config:
        """Pydantic config."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


# Create global settings instance
settings = get_settings()
