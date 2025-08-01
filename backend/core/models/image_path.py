from sqlalchemy.orm import Mapped

from core.models import Base
from core.models.mixins import IdIntPkMixin, MovieRelationMixin


class ImagePath(Base, IdIntPkMixin):

    path: Mapped[str]
