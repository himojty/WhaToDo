from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from ..movie import Movie


class MovieRelationMixin:
    _movie_id_nullable: bool = False
    _movie_id_unique: bool = False
    _movie_back_populates: str | None = None

    @declared_attr
    def movie_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("movie.id"),
            unique=cls._movie_id_unique,
            nullable=cls._movie_id_nullable,
        )

    @declared_attr
    def movie(cls) -> Mapped["Movie"]:
        return relationship(
            "Movie",
            back_populates=cls._movie_back_populates,
        )
