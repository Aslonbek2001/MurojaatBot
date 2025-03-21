from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
import re


from app.keyboards.inline.step_one_buttons import get_murojatchilar     #step_one_buttons
from app.keyboards.inline.step_two_buttons import get_murojat_turlari   #step_two_buttons
from app.keyboards.inline.step_three_buttons import get_xodimlar        # step_three_buttons
from app.keyboards.inline.phone_btn import phone_btn
from app.keyboards.inline.finsh_btn import finish_buttons
from app.states import MurojaatStates
from app.utils import dict_keys_to_set, phone_reg, format_phone_number
from app.keyboards.inline.menu_btns import menu_btns
from data.malumotlar import xodimlar, murojatchilar, murojat_turlari

murojaat_router = Router()

"""Murojaat tugmasi bosilganda"""
@murojaat_router.callback_query(F.data == "murojaat")
async def step_one(callback: types.CallbackQuery, state: FSMContext):
    
    await state.update_data(user_id=callback.from_user.id)
    
    await state.set_state(MurojaatStates.step_one)
    await callback.message.edit_text(
        "Kim murojaat qilmoqda?", reply_markup=await get_murojatchilar()
    )


"""Murojaat qiluvchi kimligini tanlash tugmasi bosilganda"""
@murojaat_router.callback_query(F.data.in_(dict_keys_to_set(murojatchilar)), MurojaatStates.step_one)
async def step_two(callback: types.CallbackQuery, state: FSMContext):

    await state.update_data(user_type=callback.data)
    await state.set_state(MurojaatStates.step_two)
   
    await callback.message.edit_text(
        "Murojaat maqsadi?", reply_markup=await get_murojat_turlari()
    )



"""Murojaat maqsadi tugmasi bosilganda"""
@murojaat_router.callback_query(F.data.in_(dict_keys_to_set(murojat_turlari)), MurojaatStates.step_two)
async def step_three(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'orqaga':
        await state.set_state(MurojaatStates.step_one)
        await callback.message.edit_text(
            "📌 Kim murojaat qilmoqda?", reply_markup=await get_murojatchilar()
        )
    else:

        await state.update_data(murojaat_type=callback.data)
        await state.set_state(MurojaatStates.step_three)
        await callback.message.edit_text(
            "Murojaat kimga yuborilishi kerak?", reply_markup=await get_xodimlar()
        )


"""Murojaat kimga yuborilishi kerak tugmasi bosilganda"""
@murojaat_router.callback_query(F.data.in_(dict_keys_to_set(xodimlar)), MurojaatStates.step_three)
async def step_four(callback: types.CallbackQuery, state: FSMContext):

    if callback.data == 'orqaga':
        await state.set_state(MurojaatStates.step_two)
        await callback.message.edit_text(
            "🎯 Murojaat maqsadi?", reply_markup=await get_murojat_turlari()
        )

    else:
        await state.update_data(murojaat_to=callback.data)
        await state.set_state(MurojaatStates.step_four)
        await callback.message.edit_text(
            "👤 Ism Familiyangizni kiriting:", reply_markup=None
        )
    

"""Ism Familiya kiritilganda"""
@murojaat_router.message(MurojaatStates.step_four)
async def step_five(message: types.Message, state: FSMContext):
    if 6 < len(message.text) < 30:
        await state.update_data(full_name=message.text)
        await state.set_state(MurojaatStates.step_five)
        
        await message.answer(
            "📞 Telefon raqamingizni kiriting:", reply_markup=phone_btn
        )
    else:
        await message.answer(
            "👤 Ism Familiyangizni to'g'ri kiriting!", reply_markup=types.ReplyKeyboardRemove()
        )



"""Telefon raqami kiritilganda"""
@murojaat_router.message(MurojaatStates.step_five)
async def step_six(message: types.Message, state: FSMContext):

    phone_number = message.text if message.text else f"+{message.contact.phone_number}"
    if phone_reg(phone_number.replace(" ", "")):
        await state.update_data(phone_number=format_phone_number(phone_number))
        await state.set_state(MurojaatStates.step_six)
        await message.answer(
            "📝 Murojaat matnini kiriting:", reply_markup=types.ReplyKeyboardRemove()
        )
    else:
        await message.answer("Telefon raqamini \n+998 94 503 18 17 yoki 94 503 18 17 \nko'rinishida raqamni kiriting!")


"""Murojaat matni kiritilganda"""
@murojaat_router.message(MurojaatStates.step_six)
async def step_seven(message: types.Message, state: FSMContext):
    
    await state.update_data(murojaat_text=message.text)
    await state.set_state(MurojaatStates.step_seven)
    data = await state.get_data()

    await message.answer(
        f"🆕 <b>Yangi murojaat</b>\n"
        f"👤 Foydalanuvchi ID: ({data['user_id']}) \n"
        f"📌 Foydalanuvchi turi: {murojatchilar.get(data['user_type'])}\n"
        f"🎯 Murojaat maqsadi: {murojat_turlari.get(data['murojaat_type'])}\n"
        f"📩 Murojaat kimga: {xodimlar.get(data['murojaat_to']).name}\n"
        f"👤 Ism Familiya: {data['full_name']}\n"
        f"📞 Telefon raqami: {data['phone_number']}\n"
        f"📝 Murojaat matni: {data['murojaat_text']}\n", 
        parse_mode="HTML", reply_markup=finish_buttons
    )


"""Murojaat yuborilganda"""
@murojaat_router.callback_query(F.data.in_({"send", "cancel"}), MurojaatStates.step_seven)
async def step_eight(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.edit_reply_markup(reply_markup=None)  # Inline tugmalarni o‘chirish
    data = await state.get_data()
    murojaat_text = (
            f"🆕 <b>Yangi murojaat</b>\n"
            f"👤 Foydalanuvchi ID: ({data['user_id']}) \n"
            f"📌 Foydalanuvchi turi: {murojatchilar.get(data['user_type'])}\n"
            f"🎯 Murojaat maqsadi: {murojat_turlari.get(data['murojaat_type'])}\n"
            f"📩 Murojaat kimga: {xodimlar.get(data['murojaat_to']).name}\n"
            f"👤 Ism Familiya: {data['full_name']}\n"
            f"📞 Telefon raqami: {data['phone_number']}\n"
            f"📝 Murojaat matni: {data['murojaat_text']}\n"
        )
    
    if callback.data == 'send':
        await callback.bot.send_message(chat_id=xodimlar.get(data['murojaat_to']).tg_id, text=murojaat_text, parse_mode="HTML")
        await state.clear()
        await callback.message.answer("✅ Murojaatingiz yuborildi.")
        await callback.message.answer("Asosiy menu", reply_markup=menu_btns)
        
    else:
        await state.clear()
        await callback.message.answer("❌ Murojaat bekor qilindi.")
        await callback.message.answer("Asosiy menu", reply_markup=menu_btns)

