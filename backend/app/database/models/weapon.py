import uuid

from sqlalchemy import (
    String,
    PrimaryKeyConstraint,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.types import Uuid

from .base import BaseModel


class WeaponModel(BaseModel):
    __tablename__ = "weapon"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="weapon_pkey"),
        {
            "comment": "Table for weapon types in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        server_default=func.gen_random_uuid(),
        comment="Weapon's UUID.",
    )
    title: Mapped[str] = mapped_column(String(256), comment="The name of the type of weapon.")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"title={self.title!r}, " \
               f")>"
