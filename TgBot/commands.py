from aiogram import types, Router, F
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aibot import send_to_aibot

router = Router()

# Storing dialog context for each user
user_contexts = {}

@router.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    # Initializing context for a new user
    user_contexts.setdefault(user_id, [])
    await message.reply("Hi!\nWhat do you want to ask?")

@router.message(F.text)
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

@router.callback_query(F.data == "reset")
async def reset_handler(query: types.CallbackQuery):
    user_id = query.from_user.id
    # Clearing the dialog context
    user_contexts[user_id] = []
    await query.answer("Dialog context reset.")
    await query.message.edit_reply_markup()