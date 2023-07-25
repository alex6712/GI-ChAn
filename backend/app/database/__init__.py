"""Database Genshin Impact Characters Analyzer

Database package.

The SQLAlchemy framework is used, the documentation of which
can be found `here`_.

This package contains a description of the dependency on getting
asynchronous session for executing SQL queries and record model
entities in the database (see database.models).

.. _`here`:
     https://www.sqlalchemy.org
"""

from .initialize import initialize
