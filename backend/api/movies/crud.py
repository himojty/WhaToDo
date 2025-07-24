from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from core.models import Movie


async def create_movie(session: AsyncSession, movie_in: dict) -> Movie:
    movie = Movie(**movie_in.model_dump())
    session.add(movie)
    await session.commit()
    return movie


async def get_movies(session: AsyncSession) -> list[Movie] | None:
    stmt = select(Movie).order_by(Movie.id)
    result: Result = await session.execute(stmt)
    movies = result.scalars().all()
    return movies
