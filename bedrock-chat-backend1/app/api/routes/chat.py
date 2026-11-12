
from fastapi import APIRouter, status

from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
    ChatData,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
)
async def chat(request: ChatRequest) -> ChatResponse:

    # Temporary response until ChatService is connected.
    answer = "Chat service integration is pending."

    return ChatResponse(
        status="success",
        message="Chat response generated successfully",
        data=ChatData(
            answer=answer,
            conversation_id=request.conversation_id or "pending",
        ),
    )
