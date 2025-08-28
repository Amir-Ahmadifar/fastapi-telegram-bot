# fastapi-telegram-pro

Production-ready scaffold for a FastAPI + Aiogram (webhook) Telegram bot with Mini App support.

**What is included**
- Clean folder structure
- SQLAlchemy models + Alembic migrations
- Webhook router with secret token validation
- WebApp initData validation helper
- Docker + docker-compose (Postgres + Redis + Nginx)
- Basic rate limiting, logging, and security patterns

Follow the `.env.example` and fill required fields, then run `docker compose up --build -d`.
