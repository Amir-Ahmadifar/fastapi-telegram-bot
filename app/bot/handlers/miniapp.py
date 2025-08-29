# bot.py
from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()

WEBAPP_URL = "https://bot.markaztrade.com"

@router.message(Command("miniapp"))
async def miniapp_handler(message: types.Message):
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text="🚀 ورود به مینی اپ",
                web_app=types.WebAppInfo(url=WEBAPP_URL)
            )]
        ]
    )
    await message.answer("سلام 👋 برای ورود به مینی اپ روی دکمه زیر بزن:", reply_markup=kb)
