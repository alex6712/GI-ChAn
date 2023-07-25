"""Genshin Impact Characters Analyzer

Source directory of the application's server side.

Tools used:
     *`FastAPI`_
     * `SQLAlchemy`_
     *`uvicorn`_
     * `asyncpg`_

Genshin Impact Characters Analyzer app offers users
user-friendly interface for analyzing character builds.

.. _`FastAPI`:
     https://fastapi.tiangolo.com/
.. _`SQLAlchemy`:
     https://www.sqlalchemy.org
.. _`uvicorn`:
     https://www.uvicorn.org
.. _`asyncpg`:
     https://magicstack.github.io/asyncpg/current/
"""

from .config import get_settings

settings = get_settings()

__title__ = settings.APP_NAME
__summary__ = settings.APP_SUMMARY

__version__ = settings.APP_VERSION

__author__ = settings.ADMIN_NAME
__email__ = settings.ADMIN_EMAIL
