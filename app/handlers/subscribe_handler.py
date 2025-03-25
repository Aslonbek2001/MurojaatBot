from aiogram import Router
from aiogram import types, F
from app.keyboards.inline.menu_btns import menu_btns
from app.keyboards.inline.subscribe_btn import get_channels_keyboard
from app.utils import check_subscription, dict_keys_to_set
from data.malumotlar import CHANNELS, path_to_channel

subscription_router = Router()

@subscription_router.callback_query(F.data == "check_subscription")
async def subscribtion_han(callback: types.CallbackQuery):
    await callback.message.edit_text(
                "Asosiy menu", reply_markup=menu_btns
            )