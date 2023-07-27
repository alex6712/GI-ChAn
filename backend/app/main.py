from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import get_settings
from app.api.routers import api_v1_router

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
    {
        "name": "characters",
        "description": "Operations with **characters**. _Adding_, _deleting_, _updating_.",
    },
]

characters_analyzer = FastAPI(
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

characters_analyzer.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

characters_analyzer.include_router(api_v1_router)
