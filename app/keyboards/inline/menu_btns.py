from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

menu_btns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Murojaat yo'llash", callback_data="murojaat"),
        ],
        [
            InlineKeyboardButton(text="Mening murojaatlarim", callback_data="murojaatlarim"),
        ],
    ]
)
