from typing import Annotated
from uuid import UUID

from fastapi import APIRouter, Body, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.schemas import FullCharacterSchema, UserSchema
from app.api.schemas.responses import FullCharactersResponse, StandardResponse
from app.api.services import character_service
from app.database.session import get_session

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
    user: Annotated[UserSchema, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """A method for obtaining information about the user's characters.

    Parameters
    ----------
    user : UserSchema
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    response : StandardResponse
        In development.
    """
    return {
        "characters": await character_service.get_full_characters_by_user_id(
            session,
            user.id,
        )
    }


@router.post(
    "/append",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Append character to user's characters.",
)
async def append_character(
    character: Annotated[FullCharacterSchema, Body()],
    user: Annotated[UserSchema, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for adding a character.

    Parameters
    ----------
    character : FullCharacterSchema
        Character's data to append.
    user : UserSchema
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
    character: Annotated[FullCharacterSchema, Body()],
    user: Annotated[UserSchema, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for updating an existing character's data.

    Parameters
    ----------
    character : FullCharacterSchema
        Character's data to update.
    user : UserSchema
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
    user: Annotated[UserSchema, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    """Method for deleting character from user's characters.

    Parameters
    ----------
    character_id : UUID
        The UUID of the character to delete.
    user : UserSchema
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    response : StandardResponse
        In development.
    """
    return {"message": "In development."}
