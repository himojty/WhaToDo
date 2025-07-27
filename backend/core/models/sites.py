from sqlalchemy import ARRAY, String
from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins import IdIntPkMixin
from core.models.mixins.movie_relation_mixin import MovieRelationMixin


class Site(Base, IdIntPkMixin, MovieRelationMixin):
    _movie_id_unique = True
    _movie_back_populates = "sites"

    sites: Mapped[list[str]] = mapped_column(ARRAY(String))
