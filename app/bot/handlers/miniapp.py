from aiogram import Router, types

router = Router()

WEBAPP_URL = "https://bot.markaztrade.com"


@router.message(lambda m: m.text is not None and not m.text.startswith("/"))
async def miniapp_handler(message: types.Message):
    text = message.text.strip()
    if text == "🚀 خرید توکن":
        kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="🚀 ورود به مینی اپ",
                        web_app=types.WebAppInfo(url=WEBAPP_URL),
                    )
                ]
            ]
        )
        await message.answer(
            "سلام 👋 برای ورود به مینی اپ روی دکمه زیر بزن:", reply_markup=kb
        )
        return
    
