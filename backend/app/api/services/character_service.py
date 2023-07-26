from uuid import UUID
from typing import AnyStr, List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import (
    CharacterSchema,
    FullCharacterSchema,
)
from app.database.tables import (
    User,
    UserCharacter,
    Character,
    Weapon,
    Element,
    Region,
)


async def get_full_characters_by_username(session: AsyncSession, username: AnyStr) -> List[FullCharacterSchema]:
    """The function of obtaining a complete description of all user's characters.

    It accepts the user's login as input, forms a query to the user_character
    association table and receives information about all the user's characters.

    Complements the information by making additional queries on the
    character table with basic character information.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    username : AnyStr
        User login, unique name.

    Returns
    -------
    characters : List[FullCharacterSchema]
        List of complete user's characters' representations.
    """
    user_id: UUID = await session.scalar(select(User.id).where(User.username == username))

    user_characters_info: List[UserCharacter] = [
        *await session.scalars(
            select(UserCharacter)
            .where(UserCharacter.user_id == user_id)
        )
    ]

    result = []
    for user_character_info in user_characters_info:
        character_info: CharacterSchema = await get_character_by_id(session, user_character_info.character_id)

        result.append(
            FullCharacterSchema(
                **character_info.model_dump(),
                level=user_character_info.character_level,
                constellations=user_character_info.character_constellations,
                attack_level=user_character_info.character_attack_level,
                skill_level=user_character_info.character_skill_level,
                burst_level=user_character_info.character_burst_level,
            )
        )

    return result


async def get_character_by_id(session: AsyncSession, id_: UUID) -> CharacterSchema:
    """Gets general information about the character by its id.

    Receives the character's ``id_`` as input and makes a request
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
    character : CharacterSchema
        General information about character.
    """
    character_info: Character = await session.scalar(select(Character).where(Character.id == id_))

    weapon: str = await session.scalar(select(Weapon.title).where(Weapon.id == character_info.weapon_id))
    element: str = await session.scalar(select(Element.title).where(Element.id == character_info.element_id))
    region: str = await session.scalar(select(Region.title).where(Region.id == character_info.region_id))

    return CharacterSchema(
        name=character_info.name,
        legendary=character_info.legendary,
        weapon=weapon,
        element=element,
        region=region,
    )
