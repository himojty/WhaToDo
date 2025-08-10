from fastapi import APIRouter, Depends, UploadFile, File, status
from sqlalchemy.ext.asyncio import AsyncSession


from api.images import crud
from core.models import db_helper
from core.schemas.images import ImageCreate

router = APIRouter(prefix="/images", tags=["Movies", "Images"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def upload_movie_image(
    movie_id: int,
    image: UploadFile = File(...),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.upload_movie_image(
        session=session,
        image=image,
        movie_id=movie_id,
    )
