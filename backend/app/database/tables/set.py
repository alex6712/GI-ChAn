import uuid
from typing import List

from sqlalchemy import PrimaryKeyConstraint, String, Text, func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Uuid

from app.database import tables


class Set(tables.Base):
    __tablename__ = "set"

    __table_args__ = (
        PrimaryKeyConstraint("id", "set_pkey"),
        {
            "comment": "Table for Genshin Impact artifact sets.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())

    artifacts: Mapped[List["tables.Artifact"]] = relationship(
        "Artifact", back_populates="set"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"title={self.title!r}, "
            f"description={self.description!r}"
            f")>"
        )
