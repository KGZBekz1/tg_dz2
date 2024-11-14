# обрабочик для команды /myinfo
from aiogram import types, Router

myinfo_router = Router()


@myinfo_router.message(commands=["myinfo"])
async def myinfo_command(message: types.Message):
    user_info = (
        f"Ваш id: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш никнейм: {message.from_user.username}"
    )
    await message.answer(user_info)
