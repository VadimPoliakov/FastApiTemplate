from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.config import env


SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{env("POSTGRES_USER")}:'
    f'{env("POSTGRES_PASSWORD")}@'
    f'{env("POSTGRES_HOST")}:'
    f'{env("POSTGRES_PORT")}/'
    f'{env("POSTGRES_DB")}'
)


class Base(DeclarativeBase):
    pass


engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
