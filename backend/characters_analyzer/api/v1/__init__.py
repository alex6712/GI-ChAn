"""Genshin Impact Characters Analyzer API V1

Here are the Version 1 API files.

This file describes the router for API methods of the first version.
"""

from fastapi import APIRouter

from characters_analyzer.api.v1.endpoints import (
    artifacts_router,
    auth_router,
    characters_router,
    root_router,
    users_router,
)

api_v1_router = APIRouter(
    prefix="/api/v1",
)
api_v1_router.include_router(artifacts_router)
api_v1_router.include_router(auth_router)
api_v1_router.include_router(characters_router)
api_v1_router.include_router(root_router)
api_v1_router.include_router(users_router)
