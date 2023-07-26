import uuid
from typing import List

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
    relationship,
)
from sqlalchemy.types import Uuid

from app.database import tables


class Character(tables.Base):
    __tablename__ = "character"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="character_pk"),
        ForeignKeyConstraint(
            ["weapon_id"],
            ["weapon.id"],
            name="character_weapon_id_fk",
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        ForeignKeyConstraint(
            ["element_id"],
            ["element.id"],
            name="character_element_id_fk",
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        ForeignKeyConstraint(
            ["region_id"],
            ["region.id"],
            name="character_region_id_fk",
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        {
            "comment": "Table for Genshin Impact characters.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    name: Mapped[str] = mapped_column(String(256))
    legendary: Mapped[bool] = mapped_column(
        Boolean(),
        comment="If character is five star, this flag is True, False otherwise.",
    )
    weapon_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    element_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    region_id: Mapped[uuid.UUID] = mapped_column(Uuid())

    weapon: Mapped["tables.Weapon"] = relationship(back_populates="characters")
    element: Mapped["tables.Element"] = relationship(back_populates="characters")
    region: Mapped["tables.Region"] = relationship(back_populates="characters")
    users: Mapped[List["tables.UserCharacter"]] = relationship(back_populates="character")

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"name={self.name!r}, " \
               f"legendary={self.legendary!r}, " \
               f"weapon_id={self.weapon_id!r}, " \
               f"element_id={self.element_id!r}" \
               f"region_id={self.region_id!r}" \
               f")>"
