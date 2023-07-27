import uuid

from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Integer, Uuid

from app.database import tables


class UserCharacter(tables.Base):
    __tablename__ = "user_character"

    __table_args__ = (
        PrimaryKeyConstraint("user_id", "character_id", name="user_character_pk"),
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

    user_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    character_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    character_level: Mapped[int] = mapped_column(Integer())
    character_constellations: Mapped[int] = mapped_column(Integer())
    character_attack_level: Mapped[int] = mapped_column(Integer())
    character_skill_level: Mapped[int] = mapped_column(Integer())
    character_burst_level: Mapped[int] = mapped_column(Integer())

    user: Mapped["tables.User"] = relationship("User", back_populates="characters")
    character: Mapped["tables.Character"] = relationship(
        "Character", back_populates="users"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"user_id={self.user_id!r}, "
            f"character_id={self.character_id!r}, "
            f"character_level={self.character_level!r}, "
            f"character_constellations={self.character_constellations!r}, "
            f"character_attack_level={self.character_attack_level!r}, "
            f"character_skill_level={self.character_skill_level!r}, "
            f"character_burst_level={self.character_burst_level!r}"
            f")>"
        )
