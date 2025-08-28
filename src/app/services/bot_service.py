from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode
from app.config.config import settings

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN.get_secret_value(), parse_mode=ParseMode.HTML)
dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer("سلام! من یک ربات FastAPI + Aiogram هستم. /help را بزنید.")

@router.message()
async def echo(message: types.Message):
    if message.text:
        await message.answer(f"پیام شما: {message.text}")

dp.include_router(router)
