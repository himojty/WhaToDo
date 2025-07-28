from pydantic import BaseModel


class SiteSchema(BaseModel):
    site: str

    movie_id: int


class Site(SiteSchema):
    id: int


class SiteCreate(SiteSchema):
    pass
