from pydantic import BaseModel, ConfigDict


class MovieSchema(BaseModel):
    title: str
    origin_title: str
    description: str
    release: str


class Movie(MovieBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class MovieCreate(MovieBase):
    pass


class MovieUpdate(MovieCreate):
    pass


class MovieUpdatePartial(MovieCreate):
    title: str | None
    origin_title: str | None
    description: str | None
    release: str | None
