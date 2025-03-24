from app.db.models import User, Murojaat
from app.db.database import async_session
from sqlalchemy.future import select



async def add_user(name: str, tg_id: int):
    async with async_session() as session:
        async with session.begin():
            user = User(name=name, tg_id=tg_id)
            session.add(user)


async def get_user_by_tg_id(tg_id: int):
    async with async_session() as session:
        result = await session.execute(
            User.__table__.select().where(User.tg_id == tg_id)
        )
        user = result.fetchone()
        return User(**user._mapping) if user else None
    

async def add_murojaat(full_name, phone, your_position, department, murojaat_type, description, user_id):
    async with async_session() as session:
        async with session.begin():
            murojaat = Murojaat(
                full_name=full_name,
                phone=phone,
                your_position=your_position,
                department=department,
                murojaat_type=murojaat_type,
                description=description,
                user_id=user_id
            )
            session.add(murojaat)

async def get_murojaatlar(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(Murojaat).where(Murojaat.user_id == user_id))
        murojaatlar = result.scalars().all()  # Barcha natijalarni olish
        return murojaatlar
