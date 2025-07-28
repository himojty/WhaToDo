from pydantic import BaseModel


class RatingSchema(BaseModel):
    rating: float


class Rating(RatingSchema):
    id: int


class RatingCreate(RatingSchema):
    pass
