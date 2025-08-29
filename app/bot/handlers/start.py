from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="خرید توکن 🪙"),
                types.KeyboardButton(text="گزینه ۲"),
            ],
            [types.KeyboardButton(text="گزینه ۳")],
        ],
        resize_keyboard=True,
    )
    await message.answer(
        "سلام! من ربات شما هستم. یک گزینه انتخاب کنید:", reply_markup=keyboard
    )
