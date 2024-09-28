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

# Creating bot and dispatcher objects
bot = Bot(token=API_TOKEN_TG)
dp = Dispatcher()

# Storing dialog context for each user
user_contexts = {}

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    # Initializing context for a new user
    user_contexts.setdefault(user_id, [])
    await message.reply("Hi!\nWhat do you want to ask?")

@dp.message(F.text)
async def message_handler(message: types.Message):
    user_id = message.from_user.id
    # Initializing context for the user if it doesn't already exist
    user_contexts.setdefault(user_id, [])

    if len(message.text) < 10:
        await message.reply("Messege need to be longer than 10 symbols")
        return

    user_contexts[user_id].append({"role": "user", "content": message.text})

    # Getting a response from AI via the send_to_aibot function
    response_text = send_to_aibot(user_contexts[user_id])

    # Saving the response in the context
    user_contexts[user_id].append({"role": "assistant", "content": response_text})

    # Creating an inline button to reset the dialog
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="RESET", callback_data="reset")]
    ])

    # Sending the response to the user
    await message.answer(response_text, reply_markup=kb)

@dp.callback_query(F.data == "reset")
async def reset_handler(query: types.CallbackQuery):
    user_id = query.from_user.id
    # Clearing the dialog context
    user_contexts[user_id] = []
    await query.answer("Dialog context reset.")
    await query.message.edit_reply_markup()

# Running the bot
if __name__ == '__main__':
    dp.run_polling(bot)