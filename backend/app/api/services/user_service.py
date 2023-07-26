from typing import AnyStr

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import UserWithPasswordSchema
from app.database.tables import User


async def get_user_by_username(session: AsyncSession, username: AnyStr) -> User:
    """Returns the user post model for further work.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    username : AnyStr
        User login, unique name.

    Returns
    -------
    user : User
        The model of the user record in the database.
    """
    return await session.scalar(select(User).where(User.username == username))


async def update_refresh_token(session: AsyncSession, username: AnyStr, refresh_token: AnyStr):
    """Overwrites the user's refresh token.

    Note
    ----
    In this case, the SQLAlchemy ORM features are used, which allow you
    to change the attribute value of the user record object,
    and at the next session commit, these changes will be saved in the database.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    username : AnyStr
        User login, unique name.
    refresh_token : AnyStr
        New refresh token.
    """
    (await get_user_by_username(session, username)).refresh_token = refresh_token


def add_user(session: AsyncSession, user: UserWithPasswordSchema):
    """Adds a user record to the database.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    user : UserWithPasswordSchema
        Schema of a user object with a password.
    """
    session.add(User(username=user.username, password=user.password, email=user.email, phone=user.phone))
