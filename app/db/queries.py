from sqlalchemy.future import select
from sqlalchemy import func
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.db.models import User, Murojaat, Javob


####################################################
####################################################
####################################################


async def add_user(name: str, tg_id: int):
    """Foydalanuvchini bazaga qo‘shish"""
    session = await get_db()  
    async with session.begin():  
        user = User(name=name, tg_id=tg_id)
        session.add(user)
    await session.commit()

async def get_user_by_tg_id(tg_id: int):
    """Telegram ID bo‘yicha foydalanuvchini olish"""
    session = await get_db()  
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    return result.scalars().first()

async def get_users():
    """Barchasini olish"""
    session = await get_db()  
    async with session:
        result = await session.execute(select(User))
        return result.scalars().all()


####################################################
####################################################
####################################################

async def add_murojaat(full_name, phone, your_position, department, murojaat_type, description, user_tg_id):
    """Murojaatni qo‘shish"""
    session = await get_db()
    async with session.begin(): 
        murojaat = Murojaat(
                full_name=full_name,
                phone=phone,
                your_position=your_position,
                department=department,
                murojaat_type=murojaat_type,
                description=description,
                user_tg_id=user_tg_id
            )
        session.add(murojaat)
    await session.commit() 

####################################################
####################################################
####################################################


async def get_murojaatlar(user_tg_id):
    """Foydalanuvchiga tegishli murojaatlar ro‘yxatini olish"""
    session = await get_db()
    async with session:
        result = await session.execute(
                select(Murojaat).where(Murojaat.user_tg_id == user_tg_id)
            )
        return result.scalars().all()

async def list_of_murojaatlar():
    """Barcha murojaatlarni olish"""
    session = await get_db()  
    async with session:
        result = await session.execute(select(Murojaat))
        return result.scalars().all()


####################################################
####################################################
####################################################

async def add_javob(murojaat_id: int, javob_text: str):
    """Murojaatga javob qo‘shish"""
    session = await get_db()
    async with session:    
        javob = Javob(murojaat_id=murojaat_id, javob=javob_text)
        session.add(javob)
        await session.commit() 

async def get_javoblar_by_murojaat_id(murojaat_id):
    """Foydalanuvchiga tegishli murojaatlar ro‘yxatini olish"""
    session = await get_db()
    async with session:
        result = await session.execute(
                select(Murojaat).where(Javob.murojaat_id == murojaat_id)
            )
        return result.scalars().all()
    

####################################################
####################################################
####################################################

# async def get_users_count():
#     """Foydalanuvchilar sonini qaytarish"""
#     async with get_db() as session:
#         stmt = select(func.count(User.id))
#         result = await session.execute(stmt)
#         count = result.scalar()
#         return count

# async def get_users_count():
#     """Foydalanuvchilar sonini qaytarish"""
#     session = await get_db()
#     async with session:
#         stmt = select(func.count(User.id))
#         result = await session.execute(stmt)
#         count = result.scalar()
#         return count

####################################################
####################################################
####################################################

async def get_users_count():
    """Foydalanuvchilar sonini qaytarish"""
    session = await get_db()
    async with session:
        stmt = select(func.count(User.id))
        result = await session.execute(stmt)
        count = result.scalar()
        return count


async def get_murojaatlar_count():
    """Murojaatlar sonini qaytarish"""
    session = await get_db()
    async with session:
        result = await session.execute(select(func.count(Murojaat.id)))
        return result.scalar()


async def get_javoblar_count():
    """Javoblar sonini qaytarish"""
    session = await get_db()
    async with session:
        result = await session.execute(select(func.count(Javob.id)))
        return result.scalar()
