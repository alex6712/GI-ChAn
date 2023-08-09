from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import CharacterDataSchema, CharacterDataWithIdSchema
from app.database.tables.entities import Character, User
from app.database.tables.junctions import UserCharacter


async def get_user_character_by_id(
    session: AsyncSession, id_: UUID
) -> UserCharacter | None:
    """The function of obtaining data about the user's character.

    It takes UserCharacter's UUID as input and returns a UserCharacter object.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    id_ : UUID
        UserCharacter's UUID.

    Returns
    -------
    character : UserCharacter
        User's character data.
    """
    return await session.get(UserCharacter, {"id": id_})


async def get_user_characters_by_user(user: User) -> List[UserCharacter]:
    """The function of obtaining all user's characters' data.

    It accepts the user's object as input, forms a query to the user_character
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
    return await user.awaitable_attrs.characters


async def get_character_by_id(session: AsyncSession, id_: UUID) -> Character:
    """Gets general information about the character by its uuid.

    Receives the character's ``id_`` as input and makes a request
    for general information about him.

    The attributes of ``weapon``, ``element`` and ``region``
    are stored in the database as foreign keys, so this attributes **must**
    be called with ``await character.awaitable_attrs.{attr}`` syntax.

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
    session: AsyncSession, user_id: UUID, data: CharacterDataWithIdSchema
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
    data : CharacterDataWithIdSchema
        Character's info to add.
    """
    session.add(
        UserCharacter(
            user_id=user_id,
            **data.model_dump(),
        )
    )
    await session.commit()


async def update_user_character(
    session: AsyncSession, user_character: UserCharacter, data: CharacterDataSchema
):
    """Updating a character entry.

    The function updates the record in the database about
    the character associated with the user.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    user_character : UserCharacter
        UserCharacter's ORM to update.
    data : CharacterDataSchema
        Character's info to put.
    """
    character_data = data.model_dump()

    for key in character_data:
        setattr(user_character, key, character_data.get(key))

    await session.commit()


async def delete_user_character(session: AsyncSession, user_character: UserCharacter):
    """Character removal function.

    Removes a character entry from the table containing information about the user's characters.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    user_character : UserCharacter
        UserCharacter's ORM to delete.
    """
    await session.delete(user_character)
    await session.commit()
