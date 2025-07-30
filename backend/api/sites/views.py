from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from api.sites import crud
from core.models import db_helper
from core.schemas.sites import SiteCreate, SiteSchema

router = APIRouter(prefix="/sites", tags=["Sites"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_site_link(
    site_in: SiteCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_site_link(session=session, site_in=site_in)


@router.get("/")
async def get_sites_links(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_sites_links(session=session)
