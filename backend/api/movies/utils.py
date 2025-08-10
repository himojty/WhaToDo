from fastapi import Query
from sqlalchemy import select, Result, func
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from core.models import Movie


async def get_movies_with_ratings(
    session: AsyncSession,
) -> list[Movie] | None:
    statement = select(Movie).options(joinedload(Movie.ratings)).order_by(Movie.id)
    result: Result = await session.execute(statement=statement)
    movies = result.scalars().all()
    return list(movies)


async def get_movies_with_ratings_and_sites(
    session: AsyncSession,
) -> list[Movie] | None:
    statement = (
        select(Movie)
        .options(joinedload(Movie.ratings), selectinload(Movie.sites))
        .order_by(Movie.id)
    )
    result: Result = await session.execute(statement=statement)
    movies = result.scalars().all()
    return list(movies)


async def get_movies_pagination(
    session: AsyncSession,
    skip: int = 0,
    limit: int = Query(..., le=100),
) -> list[Movie] | None:
    statement = (
        select(Movie)
        .options(
            joinedload(Movie.ratings),
            joinedload(Movie.image_paths),
            selectinload(Movie.sites),
        )
        .order_by(func.random() * Movie.id)
        .offset(skip)
        .limit(limit)
    )
    result: Result = await session.execute(statement=statement)
    movies = result.scalars().all()
    return list(movies)


async def get_movie_with_relations(
    movie_id: int,
    session: AsyncSession,
) -> Movie | None:
    statement = (
        select(Movie)
        .options(
            joinedload(Movie.ratings),
            joinedload(Movie.image_paths),
            selectinload(Movie.sites),
        )
        .where(Movie.id == movie_id)
        .order_by(Movie.id)
    )
    result: Result = await session.execute(statement=statement)
    movies = result.scalars().one_or_none()
    return movies
