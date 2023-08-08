import re
from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, HTTPException, Query, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.schemas import FullCharacterSchema, UserCharacterSchema
from app.api.schemas.responses import FullCharactersResponse, StandardResponse
from app.api.services import character_service
from app.database.session import get_session
from app.database.tables.entities import Character, User

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
async def get_characters(user: Annotated[User, Depends(validate_access_token)]):
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

    Returns
    -------
    response : FullCharactersResponse
        In development.
    """
    characters = []

    for user_character in await character_service.get_characters_by_user(user):
        # get character's ORM
        character: Character = await user_character.awaitable_attrs.character

        # compose argument-value pairs for FullCharacterSchema
        character_info = UserCharacterSchema.model_validate(user_character).model_dump()
        character_info.update(
            {
                "name": character.name,
                "legendary": character.legendary,
                "weapon": (await character.awaitable_attrs.weapon).title,
                "element": (await character.awaitable_attrs.element).title,
                "region": (await character.awaitable_attrs.region).title,
            }
        )

        characters.append(FullCharacterSchema(**character_info))

    return {"characters": characters}


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
        Positive feedback about character's attaching.
    """
    try:
        await character_service.add_character_to_user(session, user.id, character)
    except IntegrityError as integrity_error:
        await session.rollback()

        error_class = re.search(
            r"<class '[\w.]*\.(.*)'>", str(integrity_error.orig)
        ).group(1)

        match error_class:
            case "UniqueViolationError":
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail=f"Character with uuid={character.id} already attached to the user.",
                )
            case "ForeignKeyViolationError":
                # if a user isn't found, then 401 Error is raised by ``validate_access_token``
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Character with uuid={character.id} not found.",
                )
            case _:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incorrect request.",
                )

    return {"message": "Character appended successfully."}


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

    The method receives information about the user and the associated
    character, and then updates the record in the database.

    If the service does not find a matching update record, it returns None,
    after which the method returns HTTP code 404.

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
        Positive feedback about character's data updating.
    """
    if not await character_service.update_user_character(session, user.id, character):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Character with uuid={character.id} not found.",
        )

    return {"message": "Data updated successfully."}


@router.delete(
    "/delete",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Deleting character.",
)
async def delete_character(
    character_id: Annotated[
        UUID, Query(description="The UUID of the character to delete.")
    ],
    user: Annotated[User, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for deleting character from user's characters.

    The method gets information about the user and the character associated
    with him, and then deletes the entry in the database.

    If the service does not find a matching entry, it returns None,
    after which the method returns a 404 HTTP code.

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
        Positive feedback about character's data updating.
    """
    if not await character_service.delete_user_character(
        session, user.id, character_id
    ):
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Character with uuid={character_id} not found.",
        )

    return {"message": "Character deleted successfully."}
