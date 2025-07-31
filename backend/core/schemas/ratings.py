from pydantic import BaseModel


class RatingSchema(BaseModel):
    imdb: float
    kinopoisk: float

    movie_id: int


class Rating(RatingSchema):
    id: int


class RatingCreate(RatingSchema):
    pass
