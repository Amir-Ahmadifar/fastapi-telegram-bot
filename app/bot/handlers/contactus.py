from aiogram import Router, types

router = Router()

WEBAPP_URL = "https://www.keraseh.com/contactus/"


@router.message(lambda m: m.text is not None and not m.text.startswith("/"))
async def miniapp_handler(message: types.Message):
    text = message.text.strip()
    if text == "📞 ارتباط با ما":
        kb = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(
                        text="📞  راه های ارتباط با ما",
                        web_app=types.WebAppInfo(url=WEBAPP_URL),
                    )
                ]
            ]
        )
        await message.answer(
            "👋 پشتیبانی مجموعه ما :", reply_markup=kb
        )
        return
    
    await message.answer(
        "من این گزینه را نمی‌شناسم. لطفاً از منوی ربات انتخاب کن."
    )
