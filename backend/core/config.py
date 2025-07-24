from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    url: str = "postgresql+asyncpg://guest:guest@lochalhost:5432/movies"
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api/"

    db: DBSettings = DBSettings()


settings = Settings()
