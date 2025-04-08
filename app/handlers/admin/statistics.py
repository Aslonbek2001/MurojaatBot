from aiogram import types, Router, F
from app.db.queries import get_murojaatlar_count, get_users_count, get_javoblar_count
import re

router_admin = Router()

@router_admin.message(F.text == "data")
async def data_of_db(message: types.Message):
    """ Umumiy statistikani ko'rsatish """
    users_count = await get_users_count()
    murojaatlar_count = await get_murojaatlar_count()
    javoblar_count = await get_javoblar_count()
    await message.answer(
        f"📊 Ma'lumotlar:\n"
        f"Foydalanuvchilar soni: {users_count}\n"
        f"Murojaatlar soni: {murojaatlar_count}\n"
        f"Javoblar soni: {javoblar_count}\n"
    )


@router_admin.message(F.text == "users")
async def list_of_users(message: types.Message):
    """ Umumiy statistikani ko'rsatish """
    users_count = await get_users_count()
    

    await message.answer(
        f"📊 Ma'lumotlar:\n"
        f"Foydalanuvchilar soni: {users_count}\n"
        f"Foydalanuvchilar ro'yxati:\n"

    )