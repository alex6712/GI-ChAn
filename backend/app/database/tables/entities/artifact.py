import uuid
from typing import List, TYPE_CHECKING

from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint, func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Float, String, Text, Uuid

from app.database.tables.base import Base

if TYPE_CHECKING:  # only processed by mypy
    from app.database.tables.junctions import ArtifactSubStat, UserCharacter


class Artifact(Base):
    __tablename__ = "artifact"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="artifact_pkey"),
        ForeignKeyConstraint(
            ["set_id"],
            ["set.id"],
            name="artifact_set_id_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            ["main_stat_id"],
            ["stat.id"],
            name="artifact_main_stat_id_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            ["user_character_id"],
            ["user_character.id"],
            name="artifact_user_character_id_fk",
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        {
            "comment": "Table for Genshin Impact artifacts.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    set_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    main_stat_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    main_stat_value: Mapped[float] = mapped_column(Float())
    user_character_id: Mapped[uuid.UUID] = mapped_column(Uuid(), nullable=True)

    set: Mapped["Set"] = relationship("Set", back_populates="artifacts")
    main_stat: Mapped["Stat"] = relationship(
        "Stat", back_populates="main_stat_artifacts"
    )
    stats: Mapped["ArtifactSubStat"] = relationship(
        "ArtifactSubStat", back_populates="artifact"
    )
    character: Mapped["UserCharacter"] = relationship(
        "UserCharacter", back_populates="artifacts"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"set_id={self.set_id!r}, "
            f"main_stat_id={self.main_stat_id!r}, "
            f"main_stat_value={self.main_stat_value!r}"
            f")>"
        )


class Set(Base):
    __tablename__ = "set"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="set_pkey"),
        {
            "comment": "Table for Genshin Impact artifact sets.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    title: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())

    artifacts: Mapped[List["Artifact"]] = relationship("Artifact", back_populates="set")

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"title={self.title!r}, "
            f"description={self.description!r}"
            f")>"
        )


class Stat(Base):
    __tablename__ = "stat"

    __table_args__ = (
        PrimaryKeyConstraint("id", name="stat_pkey"),
        {
            "comment": "Table for Genshin Impact artifact stats.",
        },
    )

    id: Mapped[uuid.UUID] = mapped_column(Uuid(), server_default=func.gen_random_uuid())
    name: Mapped[str] = mapped_column(String(256))
    icon_url: Mapped[str] = mapped_column(String(256))

    main_stat_artifacts: Mapped[List["Artifact"]] = relationship(
        "Artifact", back_populates="main_stat"
    )
    sub_stat_artifacts: Mapped[List["ArtifactSubStat"]] = relationship(
        "ArtifactSubStat", back_populates="sub_stat"
    )

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"name={self.name!r}, "
            f"icon_url={self.icon_url!r}"
            f")>"
        )
