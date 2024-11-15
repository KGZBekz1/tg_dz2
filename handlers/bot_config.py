import os
from dotenv import load_dotenv

load_dotenv()

class BotConfig:
    TOKEN = os.getenv("BOT_TOKEN")
    # Добавьте любые другие настройки здесь, если нужно

config = BotConfig()
