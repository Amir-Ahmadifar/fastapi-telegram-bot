from aiogram import types
from app.services.bot_service import dp

@dp.message(lambda m: m.text in ["گزینه ۱", "گزینه ۲", "گزینه ۳"])
async def menu_handler(message: types.Message):
    responses = {
        "گزینه ۱": "شما گزینه ۱ را انتخاب کردید",
        "گزینه ۲": "شما گزینه ۲ را انتخاب کردید",
        "گزینه ۳": "شما گزینه ۳ را انتخاب کردید",
    }
    await message.answer(responses[message.text])
