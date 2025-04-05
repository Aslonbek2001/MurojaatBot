from aiogram import types, Router, F
from app.db.models import User, Murojaat, Javob
# from app.db.queryies import get_count, get_javob_count, get_muroojat_count, get_users_count
from app.db.queries import get_murojaatlar_count, get_users_count, get_javoblar_count
import re

router_admin = Router()

@router_admin.message(F.text == "data")
async def data_of_db(message: types.Message):
  
    print("\n\n\n\n Data of db \n\n\n\n")
    users_count = await get_users_count()
    await message.answer(
        f"📊 Ma'lumotlar:\n"
        f"Foydalanuvchilar soni: {users_count}\n"
        # f"Murojaatlar soni: {murojaatlar_count}\n"
        # f"Javoblar soni: {javoblar_count}\n"
        # f"Javob berilgan murojaatlar soni: {murojaatlar_count - javoblar_count}\n"
        # f"Javob berilmagan murojaatlar soni: {javoblar_count}\n"
    )