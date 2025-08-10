from fastapi import FastAPI
import uvicorn
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api import router as api_router
from core.config import settings

app = FastAPI()
app.include_router(router=api_router, prefix=settings.api.prefix)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ['*'] Разрешить все домены
    allow_methods=["GET"],  # ['*'] Разрешить все методы (GET, POST и т.д.)
    # allow_headers=["*"],  # Разрешить все заголовки
)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
from pathlib import Path

BASE_DIR = Path(__file__).parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "env" / "static"),
    name="static",
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
    )
