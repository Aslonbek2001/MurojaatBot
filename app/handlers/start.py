from aiogram import types
from app.keyboards.inline.menu_btns import menu_btns
from data.malumotlar import xodimlar
from app.states import AdminStates
from aiogram.fsm.context import FSMContext
from app.db.queries import add_user, get_user_by_tg_id

async def start_command(message: types.Message, state: FSMContext):
    user = await get_user_by_tg_id(message.from_user.id)
    
    # Check if the user exists in the database
    if not user:
        await add_user(name=message.from_user.full_name, tg_id=message.from_user.id)
    
    # Check if the user is a staff member (xodim)
    if message.from_user.id in [xodim.tg_id for xodim in xodimlar.values()]:
        await state.set_state(AdminStates.admin)
        await message.answer("Assalomu alaykum \nBu bot orqali foydalanuvchilardan kelgan murojatlarga javob yozishingiz mumkin!")
    else:
        await message.answer("Assalomu alaykum \nGFU murojaat botiga hush kelibsiz!", reply_markup=menu_btns)