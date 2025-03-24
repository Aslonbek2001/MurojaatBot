from aiogram import types
from aiogram.filters import CommandStart
from app.keyboards.inline.menu_btns import menu_btns
from data.malumotlar import xodimlar
from app.states import AdminStates
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import init_db
from app.db.queryies import add_user, get_user_by_tg_id
from app.utils import beauty_print


async def start_command(message: types.Message, state: FSMContext):

    user = await get_user_by_tg_id(message.from_user.id)
    if not user:
        await add_user(name=message.from_user.full_name, tg_id=message.from_user.id)
        
    if not user:
        user = await add_user(name=message.from_user.full_name, tg_id=message.from_user.id)
        
    
    if any(xodim.tg_id == message.from_user.id for xodim in xodimlar.values()):
        await state.set_state(AdminStates.admin)
        await message.answer("Assalomu alaykum \nBu bot orqali foydalanuvchilardan kelgan murojatlarga javob yozishingiz mumkin!")
    else:
        await message.answer("Assalomu alaykum \nGFU murojaat botiga hush kelibsiz!", reply_markup=menu_btns)
    


