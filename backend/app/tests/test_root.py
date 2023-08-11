import pytest
from httpx import AsyncClient

from app import get_settings
from app.config import Settings
from app.main import characters_analyzer

settings: Settings = get_settings()

api_url = f"http://{settings.DOMAIN}:{settings.BACKEND_PORT}/{settings.CURRENT_API_URL}"


@pytest.mark.anyio
async def test_root():
    async with AsyncClient(app=characters_analyzer, base_url=api_url) as ac:
        response = await ac.get("/")

    assert response.status_code == 200
    assert response.json() == {"code": 200, "message": "API works!"}
