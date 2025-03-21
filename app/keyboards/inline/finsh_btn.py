from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


finish_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Yuborish", callback_data="send"),
        ],
        [
            InlineKeyboardButton(text="❌ Bekor qilish", callback_data="cancel")
        ],
   
    ], 
)
