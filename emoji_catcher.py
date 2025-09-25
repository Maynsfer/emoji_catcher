import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from dotenv import load_dotenv

# Загружаем токен из .env файла
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Отправь мне премиум-эмодзи, и я покажу его custom_emoji_id 🔑")

@dp.message()
async def catch_custom_emoji(message: Message):
    if message.entities:
        for entity in message.entities:
            if entity.type == "custom_emoji":
                emoji_text = message.text[entity.offset: entity.offset + entity.length]
                await message.answer(
                    f"📌 Поймал премиум-эмодзи: {emoji_text}\n"
                    f"🔑 custom_emoji_id:\n<code>{entity.custom_emoji_id}</code>"
                )

async def main():
    print("🚀 Бот запущен. Жду эмодзи...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
