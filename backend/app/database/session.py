from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_sessionmaker,
)

from app import get_settings

engine: AsyncEngine = create_async_engine(
    url=get_settings().DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)
AsyncSessionMaker: async_sessionmaker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncSession:
    """Creates a unique request asynchronous session object.

    Used to add a database session to the request route using the FastAPI dependency system.

    Returns
    -------
    session : AsyncSession
        The asynchronous session object for the unique request.
    """
    async with AsyncSessionMaker() as session:
        yield session
