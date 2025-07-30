from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from core.schemas.movies import MovieCreate, MovieUpdate, Movie
from . import crud, utils
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
    skip: int = 0,
    limit: int = 20,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await utils.get_movies_pagination(session=session, skip=skip, limit=limit)


@router.get("/{movie_id}/")
async def get_movie(movie: Movie = Depends(movie_by_id)) -> Movie | None:
    return movie


@router.put("/{movie_id}/", response_model=MovieUpdate)
async def update_movie(
    movie_update: MovieUpdate,
    movie: Movie = Depends(movie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_movie(
        session=session, movie_update=movie_update, movie=movie
    )


@router.patch("/{movie_id}/", response_model=MovieUpdate)
async def update_movie_partial(
    movie_update: MovieUpdate,
    movie: Movie = Depends(movie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_movie(
        session=session, movie_update=movie_update, movie=movie, partial=True
    )


@router.delete("/{movie_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_movie(
    movie: Movie = Depends(movie_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> None:
    await crud.delete_movie(session=session, movie=movie)
