from uuid import UUID
from typing import List, TYPE_CHECKING

from sqlalchemy import (
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Integer, Uuid

from characters_analyzer.database.tables.base import Base

if TYPE_CHECKING:  # only processed by mypy
    from characters_analyzer.database.tables.entities import User, Character, Artifact


class UserCharacter(Base):
    __tablename__ = "user_character"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_character_pk"),
        UniqueConstraint("user_id", "character_id", name="user_character_ids_fk"),
        ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
            name="user_character_user_id_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            ["character_id"],
            ["character.id"],
            name="user_character_character_id_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        {
            "comment": "Table representing many-to-many "
            "relation between user and character tables.",
        },
    )

    id: Mapped[UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    user_id: Mapped[UUID] = mapped_column(Uuid())
    character_id: Mapped[UUID] = mapped_column(Uuid())
    level: Mapped[int] = mapped_column(Integer())
    constellations: Mapped[int] = mapped_column(Integer())
    attack_level: Mapped[int] = mapped_column(Integer())
    skill_level: Mapped[int] = mapped_column(Integer())
    burst_level: Mapped[int] = mapped_column(Integer())

    user: Mapped["User"] = relationship("User", back_populates="characters")
    character: Mapped["Character"] = relationship("Character", back_populates="users")
    artifacts: Mapped[List["Artifact"]] = relationship(
        "Artifact", back_populates="character"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"user_id={self.user_id!r}, "
            f"character_id={self.character_id!r}, "
            f"character_level={self.level!r}, "
            f"character_constellations={self.constellations!r}, "
            f"character_attack_level={self.attack_level!r}, "
            f"character_skill_level={self.skill_level!r}, "
            f"character_burst_level={self.burst_level!r}"
            f")>"
        )
