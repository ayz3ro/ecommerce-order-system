from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    database_url: str

    db_pool_size: int = 10
    db_max_overflow: int = 20
    db_pool_timeout: int = 30
    db_pool_recycle: int = 1800
    db_echo: bool = False

    model_config = SettingsConfigDict(env_file="../.env", env_file_encoding="utf-8", case_sensitive=False,
        extra="ignore", )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
