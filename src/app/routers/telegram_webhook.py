from fastapi import APIRouter, Request
from app.services.bot_service import bot, dp

router = APIRouter()

@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    payload = await request.json()
    update = dp.update_types.get("update")(**payload)  # parse update
    chat_id = update['message']['chat']['id']
    await bot.send_message(chat_id, "پیام شما دریافت شد ✅")
    await dp.feed_update(update)
    print("Received update:", update)
    return {"ok": True}
