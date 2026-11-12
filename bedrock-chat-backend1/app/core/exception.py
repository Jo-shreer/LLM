
import logging

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

logger = logging.getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:

    # Request validation errors (HTTP 422)
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError,
    ):
        return JSONResponse(
            status_code=422,
            content={
                "status": "error",
                "message": "Request validation failed.",
                "data": {
                    "errors": [
                        {
                            "field": ".".join(
                                str(part) for part in error["loc"]
                            ),
                            "message": error["msg"],
                            "type": error["type"],
                        }
                        for error in exc.errors()
                    ]
                },
            },
        )

    # HTTP exceptions (400, 401, 403, 404, etc.)
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(
        request: Request,
        exc: StarletteHTTPException,
    ):
        message = (
            exc.detail
            if isinstance(exc.detail, str)
            else "An HTTP error occurred."
        )

        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "message": message,
                "data": None,
            },
            headers=exc.headers,
        )

    # Unexpected application errors (HTTP 500)
    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ):
        logger.exception(
            "Unhandled application exception",
            extra={
                "path": request.url.path,
                "method": request.method,
            },
        )

        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "message": "An internal server error occurred.",
                "data": None,
            },
        )
