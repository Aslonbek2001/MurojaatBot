from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.db.models import Base
from config import DATABASE_URL

# Async Engine va Session yaratamiz
engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Ma’lumotlar bazasini yaratish
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

