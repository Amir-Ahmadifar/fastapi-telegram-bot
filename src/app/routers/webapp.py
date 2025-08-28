from fastapi import APIRouter, Query
from app.services.webapp_auth_service import verify_webapp_init

router = APIRouter(prefix="/webapp", tags=["webapp"])

@router.get("/auth")
async def webapp_auth(init_data: str = Query(..., description="Telegram WebApp init data")):
    verify_webapp_init(init_data)
    return {"ok": True}
