from typing import List
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.schemas import (
    CharacterSchema,
    FullCharacterSchema,
)
from app.database.tables import Character, Element, Region, UserCharacter, Weapon


async def get_full_characters_by_user_id(
    session: AsyncSession, uuid_: UUID
) -> List[FullCharacterSchema]:
    """The function of obtaining a complete description of all user's characters.

    It accepts the user's UUID as input, forms a query to the user_character
    association table and receives information about all the user's characters.

    Complements the information by making additional queries on the
    character table with basic character information.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    uuid_ : UUID
        User's UUID.

    Returns
    -------
    characters : List[FullCharacterSchema]
        List of complete user's characters' representations.
    """
    user_characters_info: List[UserCharacter] = [
        *await session.scalars(
            select(UserCharacter).where(UserCharacter.user_id == uuid_)
        )
    ]

    result = []
    for user_character_info in user_characters_info:
        character_info: CharacterSchema = await get_character_by_id(
            session, user_character_info.character_id
        )

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


async def get_character_by_id(session: AsyncSession, uuid_: UUID) -> CharacterSchema:
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
    uuid_ : UUID
        Character's UUID.

    Returns
    -------
    character : CharacterSchema
        General information about character.
    """
    character_info: Character = await session.scalar(
        select(Character).where(Character.id == uuid_)
    )

    weapon: str = await session.scalar(
        select(Weapon.title).where(Weapon.id == character_info.weapon_id)
    )
    element: str = await session.scalar(
        select(Element.title).where(Element.id == character_info.element_id)
    )
    region: str = await session.scalar(
        select(Region.title).where(Region.id == character_info.region_id)
    )

    return CharacterSchema(
        id=uuid_,
        name=character_info.name,
        legendary=character_info.legendary,
        weapon=weapon,
        element=element,
        region=region,
    )
