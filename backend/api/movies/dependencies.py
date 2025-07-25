from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Movie
from . import crud


async def movie_by_id(
    movie_id: int,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Movie:
    movie = await crud.get_movie(session=session, movie_id=movie_id)
    if movie is not None:
        return movie

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {movie_id} not found!",
    )
