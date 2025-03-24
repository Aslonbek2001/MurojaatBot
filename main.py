from aiogram.filters import CommandStart, Command
import asyncio
import logging
from aiogram import Bot, Dispatcher


from app.handlers.start import start_command
from app.handlers.mutojaat.steps import murojaat_router
from app.handlers.mutojaat.murojaatlar import murojaatlar_router
from app.handlers.admin.handlers import admin_router
from app.handlers.help import help_command
from app.db.database import init_db
from app.middlewares.subscription import SubscriptionMiddleware
from config import TOKEN


async def main():
    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__": 
    
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    dp.message.middleware(SubscriptionMiddleware())
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command(commands=["help"]))
    dp.include_router(murojaat_router)
    dp.include_router(murojaatlar_router)
    dp.include_router(admin_router)

    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped.")
        



