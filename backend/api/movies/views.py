from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.db_helper import db_helper
from core.schemas.movies import MovieCreate
from . import crud

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_movie(
    movie: MovieCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_movie(session=session, movie_in=movie)


@router.get("/")
async def get_movies(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_movies(session=session)
