from typing import List

from pydantic import Field

from schemas import FullCharacterSchema
from .standard import StandardResponse


class FullCharacterResponse(StandardResponse, FullCharacterSchema):
    """A response model with full character data.

    Used as a response from the server to a query about a user's character.

    See Also
    --------
    schemas.responses.standard.StandardResponse
    schemas.user.FullCharacterSchema
    """


class FullCharactersResponse(StandardResponse):
    """A response model with several full characters' data.

    Used as a response from the server to a query about user's several characters.

    See Also
    --------
    schemas.responses.standard.StandardResponse
    schemas.user.FullCharacterSchema
    """

    characters: List[FullCharacterSchema] = Field()
