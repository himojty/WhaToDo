from pydantic import BaseModel, ConfigDict


class MovieBase(BaseModel):
    title: str
    origin_title: str
    description: str
    release: datetime


class MovieSchema(MovieBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class MovieCreate(MovieSchema):
    pass


class MovieUpdate(MovieCreate):
    pass


class MovieUpdatePartial(MovieCreate):
    pass
