from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F

from commands import router

from aibot import send_to_aibot

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN_TG = os.getenv('TG_API')

if API_TOKEN_TG is None:
    raise ValueError("API_TOKEN_TG не найден.")

# Creating bot and dispatcher objects
bot = Bot(token=API_TOKEN_TG)
dp = Dispatcher()
dp.include_router(router)


# Running the bot
if __name__ == '__main__':
    dp.run_polling(bot)