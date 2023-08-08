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


class Stat(tables.Base):
    __tablename__ = "stat"

    __table_args_ = (
        PrimaryKeyConstraint("id", "stat_pkey"),
        {
            "comment": "Table for Genshin Impact artifact stats.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    name: Mapped[str] = mapped_column(String(256))
    icon_url: Mapped[str] = mapped_column(String(256))

    artifacts: Mapped[List["tables.Artifact"]] = relationship(
        "Artifact", back_populates="main_stat"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"icon_url={self.icon_url!r}"
            f")>"
        )
