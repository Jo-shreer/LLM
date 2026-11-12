
from typing import Any
from pydantic import BaseModel, ConfigDict, Field

class ChatRequest(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    question: str = Field(...,
                          min_length=1,
                          max_length=10000,
                          description="User's message",
    )

    conversation_id: str | None = Field(
                                         default=None,
                                          max_length=100,
                                          description="Conversation identifier",
    )

class ChatData(BaseModel):
    answer: str
    conversation_id: str


class ChatResponse(BaseModel):
    status: str = "success"
    message: str
    data: ChatData
