from aiogram import Router, types, F
from app.keyboards.inline import menu_btns



murojaatlar_router = Router()



"""Mening murojaatlarim tugmasi bosilganda"""
@murojaatlar_router.callback_query(F.data == "murojaatlarim")
async def murojaatlarim(callback: types.CallbackQuery):
    await callback.answer("Sizning Murojaatlaringiz")
    await callback.message.answer("Asosiy menu", reply_markup=menu_btns)

