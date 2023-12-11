"""API response Genshin Impact Characters Analyzer Schemas

Packet with descriptions of server response schemes.

This contains schema descriptions for the JSON objects returned by
server to a client.
Schemas are generated using ``pydantic`` (whose documentation
can be found `here`_), which allows you to give different
JSON-like objects (e.g. ``dict`` dictionaries) to the described schema
with a specific set of parameters: JSON key-value pairs.

Also, ``pydantic`` supports type casting, which allows you to accurately
specify the return type of the server [1]_.

.. _`here`:
     https://docs.pydantic.dev/
.. [1] FastAPI has ``pydantic`` support "out of the box," which
     allows you to implement automatic verification at the method setup level
     and type casting. FastAPI also automatically generates OpenAPI documentation,
     which will automatically include a schema description.
"""

from .characters import FullCharacterResponse, FullCharactersResponse
from .info import AppInfoResponse
from .jwt import TokenResponse
from .standard import StandardResponse
from .user import UserResponse
