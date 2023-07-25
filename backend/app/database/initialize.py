from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
)

from app import get_settings
from app.config import Settings
from .models import BaseModel


async def initialize():
    """Initializing a database.

    Drops all tables, then recreates all the ones.
    This will delete all the info from existing tables, so
    this is a very unsafe operation.

    That's why this function requires confirmation of superuser.
    """
    settings: Settings = get_settings()

    database_user: str = input("Please, enter the superuser login:\n")
    database_password: str = input("Please, enter the superuser password:\n")

    engine: AsyncEngine = create_async_engine(
        url=f"postgresql+asyncpg://{database_user}:{database_password}@{settings.DOMAIN}"
            f":{settings.DATABASE_PORT}/{settings.DATABASE_NAME}",
        echo=False,
    )

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)
