from typing import (
    Annotated,
)

from fastapi import (
    APIRouter,
    Depends,
    status,
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.dependencies import validate_access_token
from app.api.schemas import UserSchema
from app.api.schemas.responses import StandardResponse
from app.database.session import get_session

router = APIRouter(
    prefix="/characters",
    tags=["characters"],
)


@router.get(
    "",
    response_model=StandardResponse,
    status_code=status.HTTP_200_OK,
    summary="Returns user's characters."
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
    return {"message": "In development."}
