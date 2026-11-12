
from fastapi import APIRouter, HTTPException

from pydantic import BaseModel, Field

router = APIRouter(prefix="/chat", tags=["Chat"])


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=10000)
    conversation_id: str | None = None


class ChatResponse(BaseModel):
    answer: str
    conversation_id: str | None = None


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:
        # Service integration will be added next.
        return ChatResponse(
            answer="Chat route is working. LLM integration is pending.",
            conversation_id=request.conversation_id,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail="An internal server error occurred.",
        ) from exc
