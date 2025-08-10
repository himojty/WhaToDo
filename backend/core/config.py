from pydantic import BaseModel
from pydantic_settings import BaseSettings


class ApiSettings(BaseModel):
    prefix: str = "/api"


class DbSettings(BaseModel):
    url: str = "postgresql+asyncpg://app:password@postgres:5432/film-library"
    echo: bool = False


class Settings(BaseSettings):
    api: ApiSettings = ApiSettings()
    db: DbSettings = DbSettings()


settings = Settings()
