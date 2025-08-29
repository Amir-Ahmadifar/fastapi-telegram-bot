from fastapi import APIRouter, Request
from app.services.bot_service import bot, dp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/telegram/webhook")
async def telegram_webhook(request: Request):
    try:
        data = await request.json()
        logger.info(f"Telegram update: {data}")
        update = dp.bot.parse_update(data)
        await dp.process_update(update)
        return {"ok": True}
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        return {"ok": False}
