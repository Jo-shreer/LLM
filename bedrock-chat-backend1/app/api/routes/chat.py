
from fastapi import APIRouter, Request, status

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
    summary="Send a chat message",
    description="Processes a user message and returns an AI-generated response.",
)
async def chat(
    request: Request,
    payload: ChatRequest,
) -> ChatResponse:

    request_id = request.state.request_id

    # TODO: Call ChatService after service integration.

    answer = "Chat service integration is pending."

    return ChatResponse(
        status="success",
        message="Chat response generated successfully",
        data=ChatData(
            answer=answer,
            conversation_id=payload.conversation_id or "pending",
        ),
        request_id=request_id,
    )
