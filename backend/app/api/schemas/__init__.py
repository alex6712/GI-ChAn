"""API Genshin Impact Characters Analyzer Schemas

A package with schema descriptions for request body objects.

It contains descriptions of the object schemas needed to pass
data within an application and to cast various objects to a particular structure.

For example, to cast a user record from a database that will
have a password record to a schema without a password.
``Pydantic`` (whose documentation can be found `here`_) is used to create schemas.

.. _`here`:
     https://docs.pydantic.dev/
"""

from .character import (
    CharacterDataSchema,
    CharacterDataWithIdSchema,
    CharacterSchema,
    FullCharacterSchema,
    UserCharacterSchema,
)
from .user import UserWithPasswordSchema
