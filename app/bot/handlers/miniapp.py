# bot.py
from aiogram import Router, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()

WEBAPP_URL = "https://bot.markaztrade.com"

@router.message(commands=["Mini App"])
async def start_handler(message: types.Message):
    kb = InlineKeyboardBuilder()
    kb.button(text="🚀 ورود به مینی اپ", web_app=types.WebAppInfo(url=WEBAPP_URL))
    await message.answer("سلام 👋 روی دکمه زیر بزن تا وارد مینی اپ بشی:", reply_markup=kb.as_markup())
