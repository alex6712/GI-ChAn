from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import UserCharacterSchema
from app.database.tables import Character, User, UserCharacter


async def get_characters_by_user(user: User) -> List[UserCharacter]:
    """The function of obtaining a complete description of all user's characters.

    It accepts the user's UUID as input, forms a query to the user_character
    association table and receives information about all the user's characters.

    Complements the information by making additional queries on the
    character table with basic character information.

    Parameters
    ----------
    user : User
        User's ORM.

    Returns
    -------
    characters : List[UserCharacter]
        List of user's characters' representations.
    """
    return [*await user.awaitable_attrs.characters]


async def get_character_by_id(session: AsyncSession, id_: UUID) -> Character:
    """Gets general information about the character by its uuid.

    Receives the character's ``uuid_`` as input and makes a request
    for general information about him.

    The attributes of ``weapon``, ``element`` and ``region``
    are stored in the database as foreign keys, so with the
    help of additional queries, we get their textual representation
    and form a response.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    id_ : UUID
        Character's UUID.

    Returns
    -------
    character : Character
        General information about character.
    """
    return await session.scalar(select(Character).where(Character.id == id_))


async def add_character_to_user(
        session: AsyncSession, user_id: UUID, data: UserCharacterSchema
):
    """Adds a character entry.

    The character table stores general information about the character,
    while user_character contains information about the individual user's
    character leveling.

    This function adds a record of the user's character leveling to the database.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    user_id : UUID
        User's UUID.
    data : UserCharacterSchema
        Character's info to add.
    """
    session.add(
        UserCharacter(
            user_id=user_id,
            **{"character_" + key: value for key, value in data.model_dump().items()},
        )
    )
    await session.commit()
