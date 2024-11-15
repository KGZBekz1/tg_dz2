# обрабочик команды /random
from aiogram import types, Router
import random
from aiogram.types import InputFile

random_recipe_router = Router()

recipes = [
    {"name": "Паста Карбонара", "image": "images/recipe1.jpg", "caption": "Рецепт пасты Карбонара"},
    # Добавьте сюда другие рецепты
]


@random_recipe_router.message(commands=["random"])
async def random_recipe_command(message: types.Message):
    recipe = random.choice(recipes)
    photo = InputFile(recipe["image"])
    await message.answer_photo(photo, caption=recipe["caption"])
