from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

unique_users = set()

async def start_handler(message: types.Message):
    unique_users.add(message.from_user.id)
    user_count = len(unique_users)

    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Наш сайт", url="https://example.com"),
        InlineKeyboardButton("Instagram", url="https://instagram.com/your_profile")
    )

    await message.reply(
        f"Привет, {message.from_user.first_name}! Наш бот уже обслуживает {user_count} пользователей.",
        reply_markup=keyboard
    )

def register_start(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=["start"])
