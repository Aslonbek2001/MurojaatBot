from aiogram import types
from aiogram.filters import CommandStart
from app.keyboards.inline.menu_btns import menu_btns
from data.malumotlar import xodimlar
from app.states import AdminStates
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

async def start_command(message: types.Message, state: FSMContext):
    if any(xodim.tg_id == message.from_user.id for xodim in xodimlar.values()):
        await state.set_state(AdminStates.admin)
        await message.answer("Assalomu alaykum \nBu bot orqali foydalanuvchilardan kelgan murojatlarga javob yozishingiz mumkin!")
    
    else:
        await message.answer("Assalomu alaykum \nGFU murojaat botiga hush kelibsiz!", reply_markup=menu_btns)
    


