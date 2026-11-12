
from fastapi import FastAPI
from app.api.routes.chat import router as chat_router

app = FastAPI(
    title="Enterprise Knowledge Chat API",
    version="1.0.0",
)

register_exception_handlers(app)

app.include_router(chat_router, prefix="/api/v1",)


@app.get("/health")
async def health():
    return {"status": "healthy"}

