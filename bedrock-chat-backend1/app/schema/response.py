from pydantic import BaseModel, ConfigDict, Field
from typing import Any


class APIResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    status: str
    message: str
    data: dict[str, Any] | None = None
    request_id: str | None = None


class ErrorDetail(BaseModel):
    field: str
    message: str
    type: str


class ErrorResponse(BaseModel):
    status: str = "error"
    message: str
    data: list[ErrorDetail] = Field(default_factory=list)
    request_id: str | None = None
