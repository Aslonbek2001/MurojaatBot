from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# Asinxron PostgreSQL engine yaratish
async_engine = create_async_engine(DATABASE_URL, echo=False)

# Asinxron session yaratish
AsyncSessionLocal = sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


# ORM uchun bazaviy klass
Base = declarative_base()

# Ma'lumotlar bazasini yaratish
async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    """Yangi asinxron sessiya yaratish"""
    async with AsyncSessionLocal() as session:
        return session

# Ba'zan botni to'xtatishda aloqalarni yopish
async def close_db():
    await async_engine.dispose()