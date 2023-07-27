"""Genshin Impact Characters Analyzer API routers

A package with the implementation of API routers.

This package collects implementations of API routers containing a set of
methods (``endpoints``) of the application's server side.
Each of the routers is imported into the root path of the package,
which allows them to be further imported without explicitly specifying the module.

Routers are imported with the identifier replaced so that there are no conflicts,
because for convenience [1]_ each router is called ``router`` in separate modules.

.. [1] For code consistency and readability.
"""

from fastapi import APIRouter

from .auth import router as auth_router
from .characters import router as characters_router
from .root import router as root_router
from .users import router as users_router

api_v1_router = APIRouter(
    prefix="/api/v1",
)
api_v1_router.include_router(auth_router)
api_v1_router.include_router(characters_router)
api_v1_router.include_router(root_router)
api_v1_router.include_router(users_router)
