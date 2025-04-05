# from aiogram.filters import CommandStart, Command
# from aiogram import Bot, Dispatcher, types
# from config import TOKEN
# import logging
# import asyncio

# from app.handlers.start import start_command
# from app.handlers.mutojaat.steps import murojaat_router
# from app.handlers.subscribe_handler import subscription_router
# from app.handlers.mutojaat.murojaatlar import murojaatlar_router
# from app.handlers.admin.handlers import admin_router
# from app.hashtags import data_of_db
# from app.handlers.help import help_command
# from app.db.database import init_db
# from app.middlewares.subscription import SubscriptionMiddleware


# async def main():
#     await init_db()
#     await bot.delete_webhook(drop_pending_updates=True)
#     await dp.start_polling(bot)

# if __name__ == "__main__": 
    
#     bot = Bot(token=TOKEN)
#     dp = Dispatcher()
    
#     dp.message.middleware(SubscriptionMiddleware())
#     dp.message.register(start_command, CommandStart())
#     dp.message.register(help_command, Command(commands=["help"]))
#     dp.message.register(data_of_db, types.Message)
#     dp.include_router(subscription_router)
#     dp.include_router(murojaat_router)
#     dp.include_router(murojaatlar_router)
#     dp.include_router(admin_router)

#     logging.basicConfig(level=logging.INFO)
#     try:
#         asyncio.run(main())
#     except (KeyboardInterrupt, SystemExit):
#         print("Bot stopped.")
        



from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types
from config import TOKEN
import logging
import asyncio

from app.handlers.start import start_command
from app.handlers.mutojaat.steps import murojaat_router
from app.handlers.subscribe_handler import subscription_router
from app.handlers.mutojaat.murojaatlar import murojaatlar_router
from app.handlers.admin.handlers import admin_router
from app.handlers.help import help_command
from app.db.database import init_db
from app.middlewares.subscription import SubscriptionMiddleware
from app.handlers.admin.statistics import router_admin


bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():

    await init_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__": 

    dp.message.middleware(SubscriptionMiddleware())
    dp.message.register(start_command, CommandStart())
    dp.message.register(help_command, Command(commands=["help"]))
    dp.include_router(router_admin)
    dp.include_router(subscription_router)
    dp.include_router(murojaat_router)
    dp.include_router(murojaatlar_router)
    dp.include_router(admin_router)
    logging.basicConfig(level=logging.INFO)

    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped.")
