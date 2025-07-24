from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Movie


async def create_movie(session: AsyncSession, movie_in: dict):
    movie = Movie(**movie_in.model_dump())
    session.add(movie)
    await session.commit()
    return movie
