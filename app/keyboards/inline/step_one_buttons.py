from data.malumotlar import murojatchilar
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def get_murojatchilar():
    keyboard = InlineKeyboardBuilder()
    for key, value in murojatchilar.items():
        keyboard.button(text=value, callback_data=key)
    
    return keyboard.adjust(2).as_markup()




# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

# step_one_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Talaba", callback_data="talaba"),
#             InlineKeyboardButton(text="Abituriyent", callback_data="abituriyent"),
#         ],
#         [
#             InlineKeyboardButton(text="Xodim", callback_data="xodim"),
#             InlineKeyboardButton(text="Ota Ona", callback_data="ota_ona"),
#         ],
#         [
#             InlineKeyboardButton(text="Boshqa", callback_data="boshqa"),
#         ],
#     ], 
# )



