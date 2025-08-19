from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    app_name: str = "Diario Animado"
    secret_key: str = "supersecret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    database_url: str = "sqlite:///./data.db"
    retention_days: int = 30

    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()
