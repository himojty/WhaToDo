from fastapi import APIRouter

from .movies.views import router as movies_router
from .ratings.views import router as ratings_router

router = APIRouter()
router.include_router(router=movies_router)
router.include_router(router=ratings_router)
