#основной файл
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from dotenv import load_dotenv
from handlers.start import start_router
from handlers.myinfo import myinfo_router
from handlers.random_recipe import random_recipe_router

load_dotenv()
TOKEN = os.getenv("T_ELEGRAMTOKEN")
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher()

# Регистрируем роутеры
dp.include_router(start_router)
dp.include_router(myinfo_router)
dp.include_router(random_recipe_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "main":
    import asyncio
    asyncio.run(main())