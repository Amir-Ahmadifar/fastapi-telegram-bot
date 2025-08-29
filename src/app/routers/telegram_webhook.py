from fastapi import APIRouter, Request
from app.services.bot_service import bot, dp

router = APIRouter()

@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_update(bot, update)
    print("Received update:", update)
    return {"ok": True}
