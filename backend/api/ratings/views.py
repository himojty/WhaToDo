from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.schemas.ratings import RatingCreate
from . import crud
from core.models import db_helper

router = APIRouter(prefix="/ratings", tags=["Ratings"])


@router.get("/")
async def get_ratings(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_ratings(session=session)


@router.post("/")
async def create_rating(
    rating_in: RatingCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_rating(session=session, rating_in=rating_in)
