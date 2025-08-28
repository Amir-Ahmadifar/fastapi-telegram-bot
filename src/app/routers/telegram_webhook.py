from fastapi import APIRouter, Request, Depends, HTTPException, status
from aiogram import types
from app.services.bot_service import dp, bot
from app.core.security import validate_webhook_secret
from app.db.session import SessionLocal
from app.core.logging import logger
from app.models.webhook_event import WebhookEvent

router = APIRouter(prefix="/telegram", tags=["telegram"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhook")
async def telegram_webhook(request: Request, db=Depends(get_db)):
    if not validate_webhook_secret(request.headers):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid secret token")
    data = await request.json()
    try:
        update = types.Update.model_validate(data)
        # persist webhook event lightly
        try:
            ev = WebhookEvent(update_id=getattr(update, "update_id", None), headers=dict(request.headers), payload=data)
            db.add(ev)
            db.commit()
        except Exception:
            logger.warning("failed to persist webhook event")
        await dp.feed_webhook_update(bot, update)
    except Exception as e:
        logger.error(f"webhook processing error: {e}")
        raise HTTPException(status_code=500, detail="processing error")
    return {"ok": True}
