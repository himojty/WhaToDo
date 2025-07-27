from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, LargeBinary

from .base import Base
from .mixins import IdIntPkMixin

if TYPE_CHECKING:
    from .site import Site


class Movie(Base, IdIntPkMixin):
    title: Mapped[str | None] = mapped_column(
        String(128),
    )
    origin_title: Mapped[str] = mapped_column(String(128), unique=True)
    description: Mapped[str | None] = mapped_column(
        Text(),
    )
    release: Mapped[str | None]
    image: Mapped[bytes | None] = mapped_column(LargeBinary())

    sites: Mapped["Site"] = relationship(back_populates="movies")
