from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.movies import MovieCreate, MovieUpdate, MovieSchema, Movie
from . import crud
from .dependencies import movie_by_id

router = APIRouter(prefix="/movies", tags=["Movies"])


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
)
async def create_movie(
    movie: MovieCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Movie:
    return await crud.create_movie(session=session, movie_in=movie)


@router.get("/")
async def get_movies(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_movies(session=session)


@router.put("/{movie_id}/", response_model=MovieSchema)
async def update_movie(
    movie_update: MovieUpdate,
    movie: Movie = Depends(movie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_movie(
        session=session, movie_update=movie_update, movie=movie
    )


@router.delete("/{movie_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(
    movie: Movie = Depends(movie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_movie(session=session, movie=movie)
