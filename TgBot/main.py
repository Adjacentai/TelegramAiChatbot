from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import F

from aibot import send_to_aibot

import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN_TG = os.getenv('TG_API')

if API_TOKEN_TG is None:
    raise ValueError("API_TOKEN_TG не найден.")

# Создание объектов бота и диспетчера
bot = Bot(token=API_TOKEN_TG)
dp = Dispatcher()

# Хранение контекста диалога для каждого пользователя
user_contexts = {}

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    # Инициализация контекста для нового пользователя
    user_contexts.setdefault(user_id, [])
    await message.reply("Hi!\nWhat do you want to ask?")

@dp.message(F.text)
async def message_handler(message: types.Message):
    user_id = message.from_user.id
    # Инициализация контекста для пользователя, если его еще нет
    user_contexts.setdefault(user_id, [])

    user_contexts[user_id].append({"role": "user", "content": message.text})

    # Получаем ответ от AI через функцию send_to_aibot
    response_text = send_to_aibot(user_contexts[user_id])

    # Сохраняем ответ в контексте
    user_contexts[user_id].append({"role": "assistant", "content": response_text})

    # Создаем инлайн-кнопку для сброса диалога
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="СБРОСИТЬ", callback_data="reset")]
    ])

    # Отправляем ответ пользователю
    await message.answer(response_text, reply_markup=kb)

@dp.callback_query(F.data == "reset")
async def reset_handler(query: types.CallbackQuery):
    user_id = query.from_user.id
    # Очищаем контекст диалога
    user_contexts[user_id] = []
    await query.answer("Контекст диалога сброшен.")
    await query.message.edit_reply_markup()

# Запуск бота
if __name__ == '__main__':
    dp.run_polling(bot)
