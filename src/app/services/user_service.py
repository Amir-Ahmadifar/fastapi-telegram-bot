from sqlalchemy.orm import Session
from app.models.user import User

class UserService:
    def __init__(self, db: Session):
        self.db = db

    def upsert_from_telegram(self, tg_id: int, username: str | None, language_code: str | None, is_bot: bool):
        user = self.db.query(User).filter(User.telegram_id == tg_id).one_or_none()
        if user:
            user.username = username
            user.language_code = language_code
            user.is_bot = is_bot
            return user
        user = User(telegram_id=tg_id, username=username, language_code=language_code, is_bot=is_bot)
        self.db.add(user)
        return user
