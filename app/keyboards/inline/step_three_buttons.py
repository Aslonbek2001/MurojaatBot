from data.malumotlar import xodimlar
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def get_xodimlar():
    keyboard = InlineKeyboardBuilder()
    for key, value in xodimlar.items():
        keyboard.button(text=value.name, callback_data=key)
    
    return keyboard.adjust(2,1,2,2,2,2,2,2,2,2).as_markup()

# from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# step_three_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text="Rektor", callback_data="rektor"),
#             InlineKeyboardButton(text="Korupsiyaga qarshi kurash", callback_data="korupsiyaga"),
#         ],
#         [
#             InlineKeyboardButton(text="Qabul komissiyasi", callback_data="qabul"),
#             InlineKeyboardButton(text="Buxgalteriya", callback_data="buxgalteriya"),
#         ],
#         [
#             InlineKeyboardButton(text="Registrator ofis", callback_data="registrator"),
#         ],
#         [
#             InlineKeyboardButton(text="Hemis", callback_data="hemis"),
#         ],
#         [
#             InlineKeyboardButton(text="Orqaga", callback_data="orqaga"),
#         ],
#     ], 
# )

