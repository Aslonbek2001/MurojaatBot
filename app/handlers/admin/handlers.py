from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.states import AdminStates
from app.utils import extract_text

admin_router = Router()

@admin_router.message(AdminStates.admin)
async def reply_to_user(message: types.Message):
    if message.reply_to_message:
        text = message.text
        reply_message = message.reply_to_message.text        
        user_id = extract_text(reply_message)

        if user_id is None:
            await message.answer("Foydalanuvchi ma'lumotlari topilmadi.")

        else:
            await message.bot.send_message(chat_id=user_id, text=f"📩 Mutaxasis javobi:\n{text}")
            await message.answer("✅ Javob fuydalanuvchiga yuborildi.")
    
    else:
        await message.answer("Murojaatga javob berish uchun belgilab yozish kerak.")

