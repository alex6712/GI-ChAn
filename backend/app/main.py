from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import get_settings
from app.api.routers import (
    auth_router,
    root_router,
    users_router,
)

settings = get_settings()

tags_metadata = [
    {
        "name": "root",
        "description": "Getting information about **application**.",
    },
    {
        "name": "authorization",
        "description": "**Registration** and **authentication** operations.",
    },
    {
        "name": "users",
        "description": "Operations with **users**. Getting _information_ about them.",
    },
]

cybersquad_games = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.APP_DESCRIPTION,
    summary=settings.APP_SUMMARY,
    contact={
        "name": settings.ADMIN_NAME,
        "email": settings.ADMIN_EMAIL,
    },
    openapi_tags=tags_metadata,
)

cybersquad_games.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cybersquad_games.include_router(auth_router)
cybersquad_games.include_router(root_router)
cybersquad_games.include_router(users_router)
