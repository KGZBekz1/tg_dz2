# обрабочик для команды /myinfo
from aiogram import types, Dispatcher

async def myinfo_handler(message: types.Message):
    await message.reply(
        f"Ваш id: {message.from_user.id}\n"
        f"Ваше имя: {message.from_user.first_name}\n"
        f"Ваш никнейм: {message.from_user.username}"
    )

def register_myinfo(dp: Dispatcher):
    dp.register_message_handler(myinfo_handler, commands=["myinfo"])
