from httpx import AsyncClient



async def get_client():
    with AsyncClient as client:
        yield client


async def get_tocken(client: AsyncClient):
    resp = client.post()