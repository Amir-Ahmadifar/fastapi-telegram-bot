from app.core.security import validate_webapp_init_data, is_fresh
from fastapi import HTTPException, status

def verify_webapp_init(init_data: str):
    if not validate_webapp_init_data(init_data):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid initData")
    from urllib.parse import parse_qs
    auth_date = parse_qs(init_data).get("auth_date", [None])[0]
    if not auth_date or not is_fresh(auth_date):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Stale initData")
