
from fastapi import FastAPI
from app.api.routes.chat import router as chat_router
from app.middleware.request_logging import RequestLoggingMiddleware

app = FastAPI(
    title="Enterprise Knowledge Chat API",
    version="1.0.0",
)

register_exception_handlers(app)

app.add_middleware(RequestIDMiddleware)
app.add_middleware(RequestLoggingMiddleware)

app.include_router(chat_router, prefix="/api/v1",)

@app.get("/health")
async def health():
    return {"status": "healthy"}

