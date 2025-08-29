from aiogram import Router, types
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="🚀 خرید توکن"),
                types.KeyboardButton(text="💰 کیف پول"),
            ],
            [types.KeyboardButton(text="📞 ارتباط با ما")],
        ],
        resize_keyboard=True,
    )
    await message.answer('🤖')
    await message.answer(
        "سلام 🙂! من ربات شما هستم. گزینه مورد نظر خود را انتخاب کنید:", reply_markup=keyboard
    )
