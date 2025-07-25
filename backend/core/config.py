from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = "postgresql+asyncpg://app:password@localhost:5432/film-library"
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api/"

    db: DBSettings = DBSettings()


settings = Settings()
