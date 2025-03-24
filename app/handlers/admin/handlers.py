from aiogram import Router, types, F
from app.utils import extract_text, get_admin_users_id, get_admin_name
admin_router = Router()

@admin_router.message()
async def reply_to_user(message: types.Message):
    if message.reply_to_message:
        text = message.text
        reply_message = message.reply_to_message.text        
        user_id = extract_text(reply_message)
        admin_id = message.from_user.id
        
        if get_admin_users_id(admin_id):
            
            if user_id is None:
                await message.answer("Foydalanuvchi ma'lumotlari topilmadi.")
            else:
                await message.bot.send_message(chat_id=user_id, text=f"📩{get_admin_name(admin_id=admin_id)}javobi :\n{text}")
                await message.answer("✅ Javob fuydalanuvchiga yuborildi.")
        else:
            await message.answer("Bu bot GFU ning rasmiy Murojaat boti xisoblanadi.\n")

    else:
        await message.answer("Murojaatga javob berish uchun belgilab yozish kerak.")

