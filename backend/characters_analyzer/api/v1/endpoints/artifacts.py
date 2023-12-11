import re
from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from characters_analyzer.api.dependencies import get_session, validate_access_token
from characters_analyzer.api.services import artifact_service
from characters_analyzer.database.tables.entities import User
from characters_analyzer.schemas import ArtifactData
from characters_analyzer.schemas.responses import StandardResponse

router = APIRouter(
    prefix="/artifacts",
    tags=["artifacts"],
)


@router.post(
    "/append",
    response_model=StandardResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Appends an artifact to the user's account.",
)
async def append_artifact(
    artifact_data: Annotated[ArtifactData, Body()],
    user: Annotated[User, Depends(validate_access_token)],
    session: Annotated[AsyncSession, Depends(get_session)],
):
    try:
        await artifact_service.add_artifact(session, user.id, artifact_data)
    except IntegrityError as integrity_error:
        await session.rollback()

        error_class = re.search(
            r"<class '[\w.]*\.(.*)'>", str(integrity_error.orig)
        ).group(1)

        match error_class:
            case "ForeignKeyViolationError":
                # if a user isn't found, then 401 Error is raised by ``validate_access_token``
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User with uuid={artifact_data} not found.",
                )
            case _:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Incorrect request.",
                )

    return {
        "code": status.HTTP_201_CREATED,
        "message": "Artifact appended successfully.",
    }
