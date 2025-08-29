from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from aiogram.filters import Command
from app.config.config import settings

dp = Dispatcher()

bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")  # تنظیم parse_mode
)

@dp.message(Command(commands=["start"]))
async def start_handler(message):
    await message.answer("سلام! ربات فعال است ✅")
