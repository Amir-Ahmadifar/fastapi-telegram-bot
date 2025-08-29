from fastapi import APIRouter, Request
from app.services.bot_service import bot, dp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    await dp.feed_update(bot, update)
    logger.info(f"Received update: {update}") 
    return {"ok": True}
