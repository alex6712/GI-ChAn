import uuid

from sqlalchemy import Float, ForeignKeyConstraint, PrimaryKeyConstraint, func
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy.types import Uuid

from app.database import tables


class Artifact(tables.Base):
    __tablename__ = "artifact"

    __table_args_ = (
        PrimaryKeyConstraint("id", "artifact_pkey"),
        ForeignKeyConstraint(
            ["set_id"],
            ["set.id"],
            name="artifact_set_id_fk",
            onupdate="CASCADE",
            ondelete="SET NULL",
        ),
        ForeignKeyConstraint(
            ["main_stat_id"],
            ["stat.id"],
            name="artifact_main_stat_id_fk",
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

    set: Mapped["tables.Set"] = relationship("Set", back_populates="artifacts")
    main_stat: Mapped["tables.Stat"] = relationship("Stat", back_populates="artifacts")

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__}("
            f"id={self.id!r}, "
            f"set_id={self.set_id!r}, "
            f"main_stat_id={self.main_stat_id!r}, "
            f"main_stat_value={self.main_stat_value!r}"
            f")>"
        )
