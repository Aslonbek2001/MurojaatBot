from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# PostgreSQL uchun asinxron engine yaratamiz
engine = create_async_engine(DATABASE_URL, echo=True)

# Session yaratish uchun factory
async_session_maker = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db():
    async with async_session_maker() as session:
        yield session
