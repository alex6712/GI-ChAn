from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber


class UserSchema(BaseModel):
    """Scheme of the user object.

    Used to represent user information.

    Attributes
    ----------
    id : UUID
        User's UUID.
    username : str
        User login.
    email : EmailStr
        The user's email address.
    phone : PhoneNumber
        The user's mobile phone number.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID = Field(example="7a0fac1b-0ff6-46ab-906b-a4eb173bce21")
    username: str = Field(example="someone")
    email: EmailStr = Field(default=None, example="someone@post.domen")
    phone: PhoneNumber = Field(default=None, example="+7 900 000-00-00")


class UserWithPasswordSchema(UserSchema):
    """Scheme of the user object with password.

    Used as a representation of information about the user, including the password.

    Attributes
    ----------
    password : str
        User password.
    """

    password: str = Field(example="password")
