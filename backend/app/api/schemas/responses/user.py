from app.api.schemas import UserSchema
from .standard import StandardResponse


class UserResponse(StandardResponse, UserSchema):
    """A response model with user data.

    Used as a response from the server to a query about a user.

    See Also
    --------
    schemas.responses.standard.StandardResponse
    schemas.user.UserSchema
    """
    pass
