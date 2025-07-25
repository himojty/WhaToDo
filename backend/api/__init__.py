from fastapi import APIRouter

from .movies.views import router as movies_router

router = APIRouter()
router.include_router(router=movies_router)
