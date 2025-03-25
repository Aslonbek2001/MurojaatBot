from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import Any, Dict
from data.malumotlar import CHANNELS
from app.keyboards.inline.subscribe_btn import get_channels_keyboard
from app.utils import check_subscription

class SubscriptionMiddleware(BaseMiddleware):    
    async def __call__(self, handler, event: Message, data: Dict[str, Any]):
        bot = data["bot"]
        user_id = event.from_user.id
        channels = set(CHANNELS.keys())  # Faqat channel nomlarini olish

        # 👇 Obuna bo'lmagan kanallarni olish
        not_subscribed = await check_subscription(bot, user_id, channels)

        # 🔹 Agar foydalanuvchi barcha kanallarga obuna bo‘lmagan bo‘lsa
        if not_subscribed:
            # ❗ Faqat obuna bo‘lmagan kanallarni olish va inline button yaratish
            not_sub_channels = {channel: CHANNELS[channel] for channel in not_subscribed}
            keyboard = await get_channels_keyboard(not_sub_channels)

            # 🔹 Foydalanuvchiga xabar yuborish
            await event.answer(
                "🚀 Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:",
                reply_markup=keyboard
            )
            return  # ❌ Keyingi handlerga o'tkazmaymiz

        # ✅ Agar foydalanuvchi barcha kanallarga obuna bo‘lsa, davom etamiz
        return await handler(event, data)
