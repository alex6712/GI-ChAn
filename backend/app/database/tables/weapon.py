import uuid
from typing import List

from sqlalchemy import (
    String,
    PrimaryKeyConstraint,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Uuid

from app.database import tables


class Weapon(tables.Base):
    __tablename__ = "weapon"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="weapon_pkey"),
        {
            "comment": "Table for weapon types in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))

    characters: Mapped[List["tables.Character"]] = relationship(back_populates="weapon")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"title={self.title!r}, " \
               f")>"
