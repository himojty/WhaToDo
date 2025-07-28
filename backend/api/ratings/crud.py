from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Rating
from core.schemas.ratings import RatingCreate


async def create_rating(
    session: AsyncSession,
    rating_in: RatingCreate,
):
    rating = Rating(**rating_in.model_dump())
    session.add(rating)
    await session.commit()
    return rating


async def get_ratings(
    session: AsyncSession,
) -> list[Rating] | None:
    stmt = select(Rating).order_by(Rating.id)
    result: Result = await session.execute(stmt)
    rating = result.scalars().all()
    return list(rating)


async def delete_rating(
    session: AsyncSession,
    rating: Rating,
) -> None:
    await session.delete(rating)
    await session.commit()
