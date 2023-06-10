from httpx import AsyncClient



async def get_client():
    with AsyncClient as client:
        yield client
