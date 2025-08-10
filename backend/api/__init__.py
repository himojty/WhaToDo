from fastapi import APIRouter

from .movies.views import router as movies_router
from .ratings.views import router as ratings_router
from .sites.views import router as sites_router
from .images.views import router as images_router

router = APIRouter()
router.include_router(router=movies_router)
router.include_router(router=ratings_router)
router.include_router(router=sites_router)
router.include_router(router=images_router)
