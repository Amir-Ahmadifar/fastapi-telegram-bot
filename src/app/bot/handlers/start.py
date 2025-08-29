from aiogram import types
from aiogram.filters import Command
from src.app.services.bot_service import dp

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="گزینه ۱"), types.KeyboardButton(text="گزینه ۲")],
            [types.KeyboardButton(text="گزینه ۳")]
        ],
        resize_keyboard=True
    )
    await message.answer("سلام! من ربات شما هستم. یک گزینه انتخاب کنید:", reply_markup=keyboard)
