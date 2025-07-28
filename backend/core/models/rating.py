from sqlalchemy.orm import Mapped

from core.models import Base
from core.models.mixins import IdIntPkMixin, MovieRelationMixin


class Rating(Base, IdIntPkMixin, MovieRelationMixin):
    _movie_back_populates = "rating"

    imdb: Mapped[float]
    kinopoisk: Mapped[float]
