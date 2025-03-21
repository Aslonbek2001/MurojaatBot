import re
from data.malumotlar import CHANNELS
from aiogram.exceptions import TelegramBadRequest
from typing import Tuple
import logging

def dict_keys_to_set(dictionary):
    return set(dictionary.keys())


def extract_text(text):
    start = text.find("(")
    end = text.find(")", start)

    if start != -1 and end != -1:
        return text[start+1:end]  # Qavslarni o‘chirib, faqat ichidagi matnni olish
    return None



pattern = r"^\+998\d{9}$|^\d{9}$"

def phone_reg(number):
    if re.match(pattern, number):
        return True
    return False

def format_phone_number(phone: str) -> str:
    # Faqat raqamlarni olish
    digits = re.sub(r"\D", "", phone)

    # Telefon raqami uzunligini tekshiramiz
    if len(digits) == 9:  # 9 xonali raqam
        return f"+998 {digits[:2]} {digits[2:5]} {digits[5:7]} {digits[7:9]}"
    elif len(digits) == 12 and digits.startswith("998"):  # To‘liq +998 bilan kelgan raqam
        return f"+{digits[:3]} {digits[3:5]} {digits[5:8]} {digits[8:10]} {digits[10:12]}"
    else:
        return "❌ Noto‘g‘ri raqam"
    

async def check_subscription(bot, user_id: int, channels: Tuple[str]):
        """Foydalanuvchining barcha kanallarga obuna bo'lganligini tekshiradi."""
        not_subscribed = []
        for channel in channels:
            try:
                member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
                if member.status in ["left", "kicked"]:
                    not_subscribed.append(channel)
            except TelegramBadRequest as e:
                logging.error(f"Kanalni tekshirishda xatolik: {e}")
                not_subscribed.append(channel)
        return not_subscribed