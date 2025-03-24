from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)

menu_btns = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="GfuChanel", ),
        ],
        [
            InlineKeyboardButton(text="Mening murojaatlarim", callback_data="murojaatlarim"),
        ],
    ]
)
