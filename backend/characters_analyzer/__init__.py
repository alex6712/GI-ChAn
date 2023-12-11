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

from characters_analyzer.core.config import get_settings as _get_settings

_settings = _get_settings()

__title__ = _settings.APP_NAME
__summary__ = _settings.APP_SUMMARY

__version__ = _settings.APP_VERSION

__author__ = _settings.ADMIN_NAME
__email__ = _settings.ADMIN_EMAIL
