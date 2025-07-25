from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DbSettings(BaseModel):
    url: str = "postgresql+asyncpg://app:password@localhost:5432/film-library"
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api/"

    db: DbSettings = DbSettings()


settings = Settings()
