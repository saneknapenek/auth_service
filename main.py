from fastapi import FastAPI
from sqlalchemy import Engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from environs import Env



env = Env()
env.read_env()


app = FastAPI(
    title="auth_service"
)

DATABASE_URL = env("DATABASE_URL")
engine_db = Engine(url=DATABASE_URL)
async_session_maker = sessionmaker(bind=engine_db, class_=AsyncSession)

async def get_session_db():
    try:
        session: AsyncSession = async_session_maker()
        yield session
    finally:
        session.close()


# commit 22.06.2023