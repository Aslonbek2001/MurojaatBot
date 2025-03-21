from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from typing import Any, Dict, Tuple
import logging
from data.malumotlar import CHANNELS

from app.utils import check_subscription

class SubscriptionMiddleware(BaseMiddleware):
    
    async def __call__(self, handler, event: Message, data: Dict[str, Any]):
        bot = data["bot"]
        user_id = event.from_user.id

        not_subscribed = await check_subscription(bot, user_id, CHANNELS)
        if not_subscribed:
            await event.answer(
                "Quyidagi kanallarga obuna bo'ling:\n" +
                "\n".join([f"{channel}" for channel in not_subscribed])
            )
            return  # Agar obuna bo'lmasa, hech qanday qo'shimcha harakat qilmaydi

        return await handler(event, data)
