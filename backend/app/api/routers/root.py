from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Depends,
)

from app import get_settings
from app.api.schemas.responses import (
    StandardResponse,
    AppInfoResponse,
)
from app.config import Settings

router = APIRouter(
    tags=["root"],
)


@router.get("/", response_model=StandardResponse, status_code=status.HTTP_200_OK, summary="Functionality check.")
async def root():
    """Root path for API health check.

    Does nothing but give positive feedback to the request.

    Returns
    -------
    response : StandardResponse
        Answer about the correct operation of the server.
    """
    return {"message": "API works!"}


@router.get(
    "/app_info",
    response_model=AppInfoResponse,
    status_code=status.HTTP_200_OK,
    summary="Application information.",
)
async def app_info(settings: Annotated[Settings, Depends(get_settings)]):
    """Path to get information about the server side of the application.

    Information received:
        * app_name : str, application name;
        * app_version : str, app version;
        * app_description : str, full description of the application;
        * app_summary : str, a short description of the application;
        * admin_name : str, full name of the person in charge;
        * admin_email : str, email address to contact the person in charge.

    Parameters
    ----------
    settings : Settings
        Application settings.

    Returns
    -------
    response : AppInfoResponse
        A response containing information about the server side of the application.
    """
    return {
        "app_name": settings.APP_NAME,
        "app_version": settings.APP_VERSION,
        "app_description": settings.APP_DESCRIPTION,
        "app_summary": settings.APP_SUMMARY,
        "admin_name": settings.ADMIN_NAME,
        "admin_email": settings.ADMIN_EMAIL,
    }
