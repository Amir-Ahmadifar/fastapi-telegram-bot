from aiogram import Router, types

router = Router()

WEBAPP_URL = "https://bot.markaztrade.com/wallet"


@router.message(lambda m: m.text is not None and not m.text.startswith("/"))
async def miniapp_handler(message: types.Message):
    text = message.text.strip()
    if text == "💰 کیف پول":
        kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="💰 ورود به کیف پول",
                        web_app=types.WebAppInfo(url=WEBAPP_URL),
                    )
                ]
            ]
        )
        await message.answer(
            "👋 برای ورود به کیف پول روی دکمه زیر بزن:", reply_markup=kb
        )
        return
    
    await message.answer(
        "من این گزینه را نمی‌شناسم. لطفاً از منوی ربات انتخاب کن."
    )
