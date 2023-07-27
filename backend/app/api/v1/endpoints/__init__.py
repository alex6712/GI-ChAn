"""Genshin Impact Characters Analyzer API V1 routers

A package with the implementation of API V1 routers.

This package collects implementations of API routers containing a set of
methods (``endpoints``) of the application's server side.
Each of the routers is imported into the root path of the package,
which allows them to be further imported without explicitly specifying the module.

Routers are imported with the identifier replaced so that there are no conflicts,
because for convenience [1]_ each router is called ``router`` in separate modules.

.. [1] For code consistency and readability.
"""

from .auth import router as auth_router
from .characters import router as characters_router
from .root import router as root_router
from .users import router as users_router
