from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text

from .base import Base
from .mixins import IdIntPkMixin


class Movie(Base, IdIntPkMixin):
    title: Mapped[str | None] = mapped_column(
        String(128),
    )
    origin_title: Mapped[str | None] = mapped_column(
        String(128),
    )
    description: Mapped[str | None] = mapped_column(
        Text(),
    )
    release: Mapped[str | None]
    image: Mapped[bytes | None] = mapped_column(LargeBinary())
