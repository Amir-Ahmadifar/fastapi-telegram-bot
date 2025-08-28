from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from app.config.config import settings
from app.core.logging import logger
from app.core.rate_limit import limiter
from slowapi.middleware import SlowAPIMiddleware
from app.routers import health, telegram_webhook, webapp

class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request.state.correlation_id = request.headers.get("X-Request-ID")
        response = await call_next(request)
        if request.state.correlation_id:
            response.headers["X-Request-ID"] = request.state.correlation_id
        return response

app = FastAPI(title=settings.APP_NAME)

origins = settings.ALLOWED_ORIGINS if settings.ALLOWED_ORIGINS else []
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

app.add_middleware(SessionMiddleware, secret_key=settings.JWT_SECRET.get_secret_value())
app.add_middleware(CorrelationIdMiddleware)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(health.router)
app.include_router(telegram_webhook.router)
app.include_router(webapp.router)

@app.get("/")
async def root():
    return {"name": settings.APP_NAME, "env": settings.ENV}
