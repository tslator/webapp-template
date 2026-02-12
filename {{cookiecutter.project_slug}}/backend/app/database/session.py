"""SQLAlchemy database session factory and connection management."""

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings

# Create async engine
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,  # Log SQL queries in debug mode
    future=True,
    pool_pre_ping=True,  # Test connections before providing them
    pool_recycle=3600,  # Recycle connections after 1 hour
    connect_args={
        "timeout": 30,
        "server_settings": {
            "application_name": settings.APP_NAME,
        },
    } if "asyncpg" in settings.DATABASE_URL else {},
)

# Create async session factory
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency for getting database session.
    Used with FastAPI dependency injection.
    """
    async with async_session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


async def init_db() -> None:
    """Initialize database (create tables)."""
    async with engine.begin() as conn:
        from app.models.base import Base
        await conn.run_sync(Base.metadata.create_all)


async def drop_db() -> None:
    """Drop all tables (use with caution)."""
    async with engine.begin() as conn:
        from app.models.base import Base
        await conn.run_sync(Base.metadata.drop_all)


async def close_db() -> None:
    """Close database connection pool."""
    await engine.dispose()
