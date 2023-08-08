import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKeyConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Float, Uuid

from app.database.tables.base import Base

if TYPE_CHECKING:  # only processed by mypy
    from database.tables.entities import Artifact, Stat


class ArtifactSubStat(Base):
    __tablename__ = "artifact_sub_stat"

    __table_args__ = (
        PrimaryKeyConstraint("artifact_id", "sub_stat_id", name="artifact_stat_pk"),
        ForeignKeyConstraint(
            ["artifact_id"],
            ["artifact.id"],
            name="artifact_stat_artifact_id_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            ["sub_stat_id"],
            ["stat.id"],
            name="artifact_stat_stat_id_fk",
            onupdate="CASCADE",
            ondelete="CASCADE",
        ),
        {
            "comment": "Table representing many-to-many "
            "relation between artifact and stat tables.",
        },
    )

    artifact_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    sub_stat_id: Mapped[uuid.UUID] = mapped_column(Uuid())
    sub_stat_value: Mapped[float] = mapped_column(Float())

    artifact: Mapped["Artifact"] = relationship("Artifact", back_populates="stats")
    sub_stat: Mapped["Stat"] = relationship("Stat", back_populates="sub_stat_artifacts")

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"artifact_id={self.artifact_id!r}, "
            f"sub_stat_id={self.sub_stat_id!r}, "
            f"sub_stat_value={self.sub_stat_value!r}"
            f")>"
        )
