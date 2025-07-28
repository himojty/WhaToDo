from pydantic import BaseModel


class RatingSchema(BaseModel):
    rating: float

    movie_id: int


class Rating(RatingSchema):
    id: int


class RatingCreate(RatingSchema):
    pass
