from sqlalchemy.orm import Mapped

from core.models import Base
from core.models.mixins import IdIntPkMixin, MovieRelationMixin


class ImagePath(Base, IdIntPkMixin, MovieRelationMixin):
    _movie_back_populates = "image_paths"
    _movie_id_unique = True

    path: Mapped[str]
