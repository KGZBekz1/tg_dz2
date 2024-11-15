import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
from dotenv import load_dotenv
from handlers import start, myinfo, random_name

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Список имен для команды /random
NAMES = ("Алексей", "Мария", "Сергей", "Игорь", "Наталья")

# Подсчет уникальных пользователей
unique_users = set()


@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    # Счетчик уникальных пользователей
    unique_users.add(message.from_user.id)
    user_count = len(unique_users)

    # Клавиатура с кнопками
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton("Наш сайт", url="https://example.com"),
        InlineKeyboardButton("Instagram", url="https://instagram.com/your_profile")
    )

    # Приветственное сообщение
    await message.reply(
        f"Привет, {message.from_user.first_name}! Наш бот уже обслуживает {user_count} пользователей.",
        reply_markup=keyboard
    )

@dp.message_handler(commands=["myinfo"])
async def myinfo_handler(message: types.Message):
    await message.reply(
        f"Ваш id: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш никнейм: {message.from_user.username}"
    )

@dp.message_handler(commands=["random"])
async def random_handler(message: types.Message):
    await message.reply(f"Сегодняшнее имя: {random.choice(NAMES)}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)