#щбрабочик для команды /start
from aiogram import types, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os

load_dotenv()
start_router = Router()
unique_users = set()

def create_welcome_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("Наш сайт", url="https://ваш-сайт.com")],
        [InlineKeyboardButton("Instagram", url="https://instagram.com/ваш-профиль")]
    ])
    return keyboard

@start_router.message(commands=["start"])
async def start_command(message: types.Message):
    user_id = message.from_user.id
    unique_users.add(user_id)
    user_count = len(unique_users)
    name = message.from_user.first_name
    keyboard = create_welcome_keyboard()
    await message.answer(f"Привет, {name}! Наш бот обслуживает уже {user_count} пользователя(ей).", reply_markup=keyboard)
