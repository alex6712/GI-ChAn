import uuid
from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint, func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Boolean, String, Uuid

from app.database.tables.base import Base

if TYPE_CHECKING:  # only processed by mypy
    from app.database.tables.junctions import UserCharacter


class Character(Base):
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
        comment="If character is five stars, this flag is True, False otherwise.",
    )
    weapon_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    element_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    region_id: Mapped[uuid.UUID] = mapped_column(Uuid())

    weapon: Mapped["Weapon"] = relationship("Weapon", back_populates="characters")
    element: Mapped["Element"] = relationship("Element", back_populates="characters")
    region: Mapped["Region"] = relationship("Region", back_populates="characters")
    users: Mapped[List["UserCharacter"]] = relationship(
        "UserCharacter", back_populates="character"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"legendary={self.legendary!r}, "
            f"weapon_id={self.weapon_id!r}, "
            f"element_id={self.element_id!r}, "
            f"region_id={self.region_id!r}"
            f")>"
        )


class Element(Base):
    __tablename__ = "element"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="element_pkey"),
        {
            "comment": "Table for elements in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))

    characters: Mapped[List["Character"]] = relationship(
        "Character", back_populates="element"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"title={self.title!r}"
            f")>"
        )


class Region(Base):
    __tablename__ = "region"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="region_pkey"),
        {
            "comment": "Table for regions in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))

    characters: Mapped[List["Character"]] = relationship(
        "Character", back_populates="region"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"title={self.title!r}"
            f")>"
        )


class Weapon(Base):
    __tablename__ = "weapon"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="weapon_pkey"),
        {
            "comment": "Table for weapon types in Genshin Impact.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))

    characters: Mapped[List["Character"]] = relationship(
        "Character", back_populates="weapon"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"title={self.title!r}"
            f")>"
        )
