from functools import lru_cache
from typing import List

from pydantic import (
    EmailStr,
    IPvAnyAddress,
    AnyHttpUrl,
    field_validator,
)
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Config project class.

    Used `pydantic`_ + `python-dotenv`_ to look up application settings described in .env.

    .. _`pydantic`:
        https://docs.pydantic.dev/
    .. _`python-dotenv`:
        https://pypi.org/project/python-dotenv/

    See Also
    --------
    pydantic
    python-dotenv

    Attributes
    ----------
    APP_NAME : str
        The name of the application.
    APP_VERSION : str
        The current version of the application.
    APP_DESCRIPTION : str
        Full description of the application.
    APP_SUMMARY : str
        Brief description of the application.
    ADMIN_NAME : str
        Name of the person responsible.
    ADMIN_EMAIL : EmailStr
        Email address to contact the person in charge.
    DEV_MODE : bool
        Development mode.
    INITIALIZE_DB : bool
        Recreate the DB.
    BACKEND_CORS_ORIGINS : List[AnyHttpUrl]
        List of sources for CORS Middleware.
    DOMAIN : str` | `IPvAnyAddress
        The IP of the domain where the application is located.
    BACKEND_PORT : int
        Application port.
    DATABASE_USER : str
        The database user to connect to.
    DATABASE_PASSWORD : str
        User password to connect to the database.
    DATABASE_PORT : int
        Database port.
    DATABASE_NAME : str
        Database name.
    DATABASE_URL : PostgresDsn
        Connection string (link) to the database.
    JWT_SECRET_KEY : str
        The secret key to encode the JSON Web Token.
    JWT_ALGORITHM : str
        JWT encoding algorithm.
    ACCESS_TOKEN_LIFETIME_MINUTES : int
        Access token lifetime in minutes.
    REFRESH_TOKEN_LIFETIME_DAYS : int
        Refresh token lifetime in days.
    """
    APP_NAME: str
    APP_VERSION: str
    APP_DESCRIPTION: str
    APP_SUMMARY: str

    ADMIN_NAME: str
    ADMIN_EMAIL: EmailStr

    DEV_MODE: bool

    INITIALIZE_DB: bool

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl]

    @classmethod
    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    def assemble_cors_origins(cls, v: List[str] | str) -> List[str] | str:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]

        elif isinstance(v, (list, str)):
            return v

        raise ValueError(v)

    DOMAIN: str | IPvAnyAddress

    BACKEND_PORT: int

    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_NAME: str

    DATABASE_URL: str

    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_LIFETIME_MINUTES: int
    REFRESH_TOKEN_LIFETIME_DAYS: int

    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache
def get_settings() -> Settings:
    return Settings()
