import uvicorn

from app import get_settings


if __name__ == "__main__":
    settings = get_settings()

    uvicorn.run(
        app="app.main:cybersquad_games",
        host=settings.DOMAIN,
        port=settings.BACKEND_PORT,
        reload=settings.DEV_MODE,
    )
