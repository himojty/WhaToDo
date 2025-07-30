from fastapi import Query
from sqlalchemy import select, Result
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
    skip=0,
    limit: int = Query(20, le=100),
) -> list[Movie] | None:
    statement = (
        select(Movie)
        .options(joinedload(Movie.ratings), selectinload(Movie.sites))
        .order_by(Movie.id)
        .offset(skip)
        .limit(limit)
    )
    result: Result = await session.execute(statement=statement)
    movies = result.scalars().all()
    return list(movies)
