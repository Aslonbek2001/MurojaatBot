from aiogram import types

async def help_command(message: types.Message):
    await message.answer("This is the help section. How can I assist you today?")

