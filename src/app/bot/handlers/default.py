from aiogram import types
from app.services.bot_service import dp

@dp.message()
async def default_handler(message: types.Message):
    await message.answer("من این پیام را متوجه نشدم، لطفاً یکی از گزینه‌های منو را انتخاب کنید.")
