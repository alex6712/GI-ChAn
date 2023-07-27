from typing import Annotated, List
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.schemas import FullCharacterSchema, UserCharacterSchema
from app.api.schemas.responses import FullCharactersResponse, StandardResponse
from app.api.services import character_service
from app.database.session import get_session
from app.database.tables import Character, User, UserCharacter

router = APIRouter(
    prefix="/characters",
    tags=["characters"],
)


@router.get(
    "/get",
    response_model=FullCharactersResponse,
    status_code=status.HTTP_200_OK,
    summary="Returns user's characters.",
)
async def get_characters(
    user: Annotated[User, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """A method for obtaining information about the user's characters.

    The method gets the user's ORM from the dependency on authorization,
    after which it makes a request to get information about users
    associated with characters.

    Further, general information about the attached characters is
    obtained and combined into FullCharacterSchema.

    Parameters
    ----------
    user : User
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    response : FullCharactersResponse
        In development.
    """
    user_characters: List[
        UserCharacter
    ] = await character_service.get_characters_by_user(user)  # lol, black, what are you doing?

    result = []
    for user_character in user_characters:
        id_: UUID = user_character.character_id

        # get character ORM by id
        character: Character = await character_service.get_character_by_id(session, id_)

        # get attached weapon, element and region
        weapon = await character.awaitable_attrs.weapon
        element = await character.awaitable_attrs.element
        region = await character.awaitable_attrs.region

        # compose argument-value pairs for FullCharacterSchema
        character_info = UserCharacterSchema.model_validate(user_character).model_dump()
        character_info.update(
            {
                "name": character.name,
                "legendary": character.legendary,
                "weapon": weapon.title,
                "element": element.title,
                "region": region.title,
            }
        )

        result.append(FullCharacterSchema(**character_info))

    return {"characters": result}


@router.post(
    "/append",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Append character to user's characters.",
)
async def append_character(
    character: Annotated[UserCharacterSchema, Body()],
    user: Annotated[User, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for adding a character.

    Parameters
    ----------
    character : UserCharacterSchema
        Character's data to append.
    user : User
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    response : StandardResponse
        In development.
    """
    return {"message": "In development."}


@router.put(
    "/put",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Update character's data.",
)
async def put_character(
    character: Annotated[UserCharacterSchema, Body()],
    user: Annotated[User, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for updating an existing character's data.

    Parameters
    ----------
    character : UserCharacterSchema
        Character's data to update.
    user : User
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    response : StandardResponse
        In development.
    """
    return {"message": "In development."}


@router.delete(
    "/delete",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Deleting character.",
)
async def delete_character(
    character_id: Annotated[
        UUID, Path(description="The UUID of the character to delete.")
    ],
    user: Annotated[User, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for deleting character from user's characters.

    Parameters
    ----------
    character_id : UUID
        The UUID of the character to delete.
    user : User
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    response : StandardResponse
        In development.
    """
    return {"message": "In development."}
