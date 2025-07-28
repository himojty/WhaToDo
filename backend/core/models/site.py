from sqlalchemy.orm import Mapped

from core.models import Base
from core.models.mixins import IdIntPkMixin, MovieRelationMixin


class Site(Base, IdIntPkMixin, MovieRelationMixin):
    _movie_back_populates = "sites"

    site: Mapped[str]
