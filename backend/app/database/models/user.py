from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from .base import BaseModel


class UserModel(BaseModel):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(256), nullable=False)
    password: Mapped[str] = mapped_column(String(256), nullable=False)
    email: Mapped[str] = mapped_column(String(256))
    phone: Mapped[str] = mapped_column(String(256))
    refresh_token: Mapped[str] = mapped_column(String())

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(" \
               f"id={self.id!r}, " \
               f"username={self.username!r}, " \
               f"password={self.password!r}, " \
               f"email={self.email!r}, " \
               f"phone={self.phone!r}" \
               f"refresh_token={self.refresh_token!r}" \
               f")>"
