from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """Scheme of the user object.

    Used to represent user information.

    Attributes
    ----------
    username : str
        User login.
    email : EmailStr
        The user's email address.
    phone : str
        The user's mobile phone number.
    """
    username: str = Field(example="someone")
    email: EmailStr = Field(default=None, example="someone@post.domen")
    phone: str = Field(default=None, example="+7 900 000-00-00")


class UserWithPasswordSchema(UserSchema):
    """Scheme of the user object with password.

    Used as a representation of information about the user, including the password.

    Attributes
    ----------
    password : str
        User password.
    """
    password: str = Field(example="password")
