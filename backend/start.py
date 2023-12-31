import asyncio

import uvicorn

from characters_analyzer.core.config import get_settings
from characters_analyzer.database import initialize

if __name__ == "__main__":
    settings = get_settings()

    if settings.INITIALIZE_DB:
        asyncio.run(initialize())

    uvicorn.run(
        app="characters_analyzer.main:characters_analyzer",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEV_MODE,
    )
