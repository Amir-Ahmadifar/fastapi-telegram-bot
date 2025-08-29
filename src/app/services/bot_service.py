from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from app.config.config import settings
from app.bot.handlers import start

bot = Bot(
    token=settings.TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="HTML")
)

dp = Dispatcher()
dp.include_router(start.router)


async def set_bot_commands():
    commands = [
        BotCommand(command="start", description="شروع ربات"),
        BotCommand(command="help", description="راهنما"),
        BotCommand(command="menu", description="نمایش منو"),
    ]
    await bot.set_my_commands(commands)
