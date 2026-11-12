
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.schemas.response import ErrorResponse, ErrorDetail

logger = logging.getLogger(__name__)


def get_request_id(request: Request) -> str | None:
    return getattr(request.state, "request_id", None)


def register_exception_handlers(app: FastAPI) -> None:

    # Validation errors: HTTP 422
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:

        errors = [
            ErrorDetail(
                field=".".join(str(part) for part in error["loc"]),
                message=error["msg"],
                type=error["type"],
            )
            for error in exc.errors()
        ]

        response = ErrorResponse(
            message="Request validation failed.",
            data=errors,
            request_id=get_request_id(request),
        )

        return JSONResponse(
            status_code=422,
            content=response.model_dump(mode="json"),
        )

    # HTTP errors: 400, 401, 403, 404, etc.
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request,
        exc: StarletteHTTPException,
    ) -> JSONResponse:

        message = (
            exc.detail
            if isinstance(exc.detail, str)
            else "An HTTP error occurred."
        )

        response = ErrorResponse(
            message=message,
            request_id=get_request_id(request),
        )

        return JSONResponse(
            status_code=exc.status_code,
            content=response.model_dump(mode="json"),
            headers=exc.headers,
        )

    # Unexpected errors: HTTP 500
    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:

        request_id = get_request_id(request)

        logger.exception(
            "Unhandled application exception",
            extra={
                "request_id": request_id,
                "path": request.url.path,
                "method": request.method,
            },
        )

        response = ErrorResponse(
            message="An internal server error occurred.",
            request_id=request_id,
        )

        return JSONResponse(
            status_code=500,
            content=response.model_dump(mode="json"),
        )
