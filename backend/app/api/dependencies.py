from typing import Annotated, AnyStr

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    OAuth2PasswordBearer,
)
from jose import ExpiredSignatureError, JWTError
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.jwt import jwt_decode
from app.api.services import user_service
from app.database.session import get_session
from app.database.tables import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/sign_in")

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials.",
    headers={"WWW-Authenticate": "Bearer"},
)


async def validate_access_token(
    token: Annotated[AnyStr, Depends(oauth2_scheme)],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> User:
    """Dependency authorization.

    Receives a JSON Web Token as input, decodes it, and checks if the user exists in the database.
    Returns the user record model.

    Parameters
    ----------
    token : AnyStr
        JSON Web Token, access token.
    session : AsyncSession
        Request session object.

    Returns
    -------
    user : User
        User's ORM.
    """
    return await _get_user_from_token(token, session)


async def validate_refresh_token(
    credentials: Annotated[HTTPAuthorizationCredentials, Security(HTTPBearer())],
    session: Annotated[AsyncSession, Depends(get_session)],
) -> User:
    """Dependency of automatic authentication.

    Gets the user's refresh_token in the request header, decodes it,
    checks for a match in the database.

    Parameters
    ----------
    credentials : HTTPAuthorizationCredentials
        Automatic authentication data (refresh token).
    session : AsyncSession
        Request session object.

    Returns
    -------
    user : User
        User's ORM.
    """
    user = await _get_user_from_token(refresh_token := credentials.credentials, session)

    if user.refresh_token != refresh_token:
        raise credentials_exception

    return user


async def _get_user_from_token(token: AnyStr, session: AsyncSession) -> User:
    """Function to get user record from a database by data from JWT.

    Receives a JSON Web Token as input, decodes it, and checks if the user exists in the database.
    Returns the user record model from the database.

    Parameters
    ----------
    token : AnyStr
        JSON Web Token, access token.
    session : AsyncSession
        Request session object.

    Returns
    -------
    user : User
        Model of the user record from the database.
    """
    try:
        if (username := jwt_decode(token).get("sub")) is None:
            raise credentials_exception
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Signature has expired.",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except JWTError:
        raise credentials_exception

    if (user := await user_service.get_user_by_username(session, username)) is None:
        raise credentials_exception

    try:
        await session.commit()
    except IntegrityError:
        await session.rollback()

        raise credentials_exception

    return user
