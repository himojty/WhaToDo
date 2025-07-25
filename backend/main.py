from fastapi import FastAPI
import uvicorn

from api import router as api_router
from backend.core.config import settings

app = FastAPI()
app.include_router(router=api_router, prefix=settings.api_prefix)

if __name__ == "__main__":
    uvicorn.run(app="main:app")
