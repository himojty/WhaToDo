from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Site
from core.schemas.sites import SiteCreate


async def create_site_link(
    session: AsyncSession,
    site_in: SiteCreate,
):
    site = Site(**site_in.model_dump())
    session.add(site)
    await session.commit()
    return site


async def get_sites_links(
    session: AsyncSession,
) -> list[Site] | None:
    stmt = select(Site).order_by(Site.id)
    result: Result = await session.execute(stmt)
    sites = result.scalars().all()
    return list(sites)
