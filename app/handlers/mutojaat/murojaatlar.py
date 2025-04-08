from aiogram import Router, types, F
from app.keyboards.inline.menu_btns import menu_btns

from app.db.queries import get_murojaatlar


murojaatlar_router = Router()

@murojaatlar_router.callback_query(F.data == "murojaatlarim")
async def murojaatlarim(callback: types.CallbackQuery):
    murojaatlar = await get_murojaatlar(callback.from_user.id)
    if murojaatlar:
        await callback.answer("Sizning Murojaatlaringiz")
        
        for murojaat in murojaatlar:
            murojaat_text = (
                f"🆕 <b>Murojaat: {murojaat.created_at.strftime('%d.%m.%Y')}</b>\n"
                f"👤 Foydalanuvchi ID: ({murojaat.user_tg_id}) \n"
                f"📌 Foydalanuvchi turi: {murojaat.your_position}\n"
                f"🎯 Murojaat maqsadi: {murojaat.murojaat_type}\n"
                f"📩 Murojaat kimga: {murojaat.department}\n"
                f"👤 Ism Familiya: {murojaat.full_name}\n"
                f"📞 Telefon raqami: {murojaat.phone}\n"
                f"📝 Murojaat matni: {murojaat.description}\n"
                
            )
            await callback.message.answer(
                text=murojaat_text, parse_mode="HTML",
            )
    else:
        await callback.message.answer("Sizning hech qanday\nmurojaatingiz yo‘q.", reply_markup=menu_btns)
    
    await callback.message.answer("Asosiy menu", reply_markup=menu_btns)



# @murojaatlar_router.callback_query(F.data == "murojaatlarim")
# async def murojaatlarim(callback: types.CallbackQuery):
#     await callback.answer("Sizning Murojaatlaringiz")
    
#     murojaatlar = await get_murojaatlar(callback.from_user.id)

#     if murojaatlar:
#         for murojaat in murojaatlar:
#             murojaat_text = (
#                 "**********************************************\n"
#                 f"🆕 <b>Murojaat: {murojaat.created_at}</b>\n"
#                 f"👤 Foydalanuvchi ID: ({murojaat.user_id}) \n"
#                 f"📌 Foydalanuvchi turi: {murojaat.your_position}\n"
#                 f"🎯 Murojaat maqsadi: {murojaat.murojaat_type}\n"
#                 f"📩 Murojaat kimga: {murojaat.department}\n"
#                 f"👤 Ism Familiya: {murojaat.full_name}\n"
#                 f"📞 Telefon raqami: {murojaat.phone}\n"
#                 f"📝 Murojaat matni: {murojaat.description}\n"
#                 "**********************************************\n"
#             )
#             await callback.message.answer(text=murojaat_text, parse_mode="HTML", reply_markup=menu_btns)
#     else:
#         await callback.message.answer("Sizning hech qanday murojaatingiz yo‘q.", reply_markup=menu_btns)
#         await callback.message.answer("Asosiy menu", reply_markup=menu_btns)
