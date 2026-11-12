
from typing import Any

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


# Request schema
class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="User's chat question",
    )
    conversation_id: str | None = None


# Response schema
class ChatResponse(BaseModel):
    status: str
    message: str
    data: dict[str, Any] | None = None


# Chat endpoint
@router.post(
    "",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
)
async def chat(request: ChatRequest):

    try:
        # TODO: Connect Bedrock Knowledge Base and LLM service.

        answer = "Chat route is working. LLM integration is pending."

        return ChatResponse(
            status="success",
            message="Chat response generated successfully",
            data={
                "answer": answer,
                "conversation_id": request.conversation_id,
            },
        )

    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An internal server error occurred.",
        ) from exc
