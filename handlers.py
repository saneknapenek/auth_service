from fastapi import HTTPException

from main import app
from schemas import AuthenticationData


@app.post("/login")
async def login_user(data: AuthenticationData):
    