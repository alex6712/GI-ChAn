import uuid

from sqlalchemy import (
    String,
    PrimaryKeyConstraint,
    ForeignKeyConstraint,
    func,
    Boolean,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)
from sqlalchemy.types import Uuid

from .base import BaseModel


class CharacterModel(BaseModel):
    __tablename__ = "character"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="character_pk"),
        ForeignKeyConstraint(
            ["weapon_type"],
            ["weapon.id"],
            name="character_weapon_id_fk",
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        {
            "comment": "Table for Genshin Impact characters.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        server_default=func.gen_random_uuid(),
        comment="Character's Universal Unique Identifier.",
    )
    name: Mapped[str] = mapped_column(String(256), comment="Character's name.")
    legendary: Mapped[bool] = mapped_column(
        Boolean(),
        comment="If character is five star, this flag is True, False otherwise.",
    )
    weapon_type: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        comment="The foreign key to weapon_type UUID.",
    )
    element: Mapped[uuid.UUID] = mapped_column(Uuid(), comment="The foreign key to element UUID.")
    nation: Mapped[uuid.UUID] = mapped_column(
        Uuid(),
        comment="The nation's UUID where character comes from.",
    )

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"name={self.name!r}, " \
               f"legendary={self.legendary!r}, " \
               f"weapon_type={self.weapon_type!r}, " \
               f"element={self.element!r}" \
               f"nation={self.nation!r}" \
               f")>"
