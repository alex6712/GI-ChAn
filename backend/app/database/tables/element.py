import uuid
from typing import List

from sqlalchemy import PrimaryKeyConstraint, String, func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Uuid

from app.database import tables


class Element(tables.Base):
    __tablename__ = "element"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="element_pkey"),
        {
            "comment": "Table for elements in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))

    characters: Mapped[List["tables.Character"]] = relationship(
        "Character", back_populates="element"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"title={self.title!r}, "
            f")>"
        )
