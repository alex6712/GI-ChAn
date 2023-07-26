import asyncio

import uvicorn

from app import get_settings
from app.database import initialize

if __name__ == "__main__":
    settings = get_settings()

    if settings.INITIALIZE_DB:
        asyncio.run(initialize())

    uvicorn.run(
        app="app.main:characters_analyzer",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEV_MODE,
    )
