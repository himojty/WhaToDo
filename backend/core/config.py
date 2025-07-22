from pydantic import BaseModel
from pydantic_settings import BaseSettings
import os


class DBSettings(BaseModel):
    url: str = os.environ.get("DATABASE_URL")
    echo: bool = False


class Settings(BaseSettings):
    api_prefix: str = "/api/"

    db: DBSettings = DBSettings()


settings = Settings()
