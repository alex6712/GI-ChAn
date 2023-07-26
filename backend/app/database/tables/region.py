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


class Region(tables.Base):
    __tablename__ = "region"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="region_pkey"),
        {
            "comment": "Table for regions in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))

    characters: Mapped[List["tables.Character"]] = relationship("Character", back_populates="region")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"title={self.title!r}, " \
               f")>"
