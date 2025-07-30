from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Site


async def get_sites_by_movie_id(session: AsyncSession, movie_id: int):
    statement = select(Site).where(Site.movie_id == movie_id)
    result = await session.execute(statement)
    sites = result.scalars().all()
    if sites is not None:
        return list(sites)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Sites with movie id {movie_id} not found!",
    )
