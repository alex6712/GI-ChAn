from typing import Annotated, AnyStr

from fastapi import (
    APIRouter,
    Depends,
    status,
    Path,
)
from fastapi.responses import RedirectResponse
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.schemas import UserSchema
from app.api.schemas.responses import UserResponse
from app.api.services import user_service
from app.database.session import get_session

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK, summary="Personal page.")
async def me(user: Annotated[UserSchema, Depends(validate_access_token)]):
    """User's personal page method.

    Returns information about the owner of the token.

    Parameters
    ----------
    user : UserSchema
        The user is received from dependence on authorization.

    Returns
    -------
    user : UserSchema
        User schema without a password.
    """
    return user


@router.get(
    "/{username}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    summary="User page.",
)
async def person(
        username: Annotated[AnyStr, Path(title="Логин пользователя, на чью личную страницу необходимо перейти.")],
        user: Annotated[UserSchema, Depends(validate_access_token)],
        session: Annotated[AsyncSession, Depends(get_session)],
):
    """User's page method.

    If the owner of the token sends a request to this method,
    then a redirect to the personal page is returned.
    In another case, the page of the requested user is returned.

    Parameters
    ----------
    username : AnyStr
        The name of the user whose page is being requested.
    user : UserSchema
        The user is received from dependence on authorization.
    session : AsyncSession
        Request session object.

    Returns
    -------
    user : UserSchema
        User schema without a password.
    """
    if user.username == username:
        return RedirectResponse("/users/me")

    if (result := await user_service.get_user_by_username(session, username)) is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User \"{username}\" not found.",
        )

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Not enough information in request.",
        )

    return result
