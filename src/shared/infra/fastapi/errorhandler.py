from starlette import status
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from shared.domain.exception import BaseHttpException


def error_handlers(app) -> JSONResponse:
    @app.exception_handler(BaseHttpException)
    async def http_custom_exception_handler(
        request: Request,
        exc: BaseHttpException
    ):
        content = {
            "meta": {
                "code": exc.code,
                "error": str(exc.error),
                "message": exc.message
            },
            "data": None
        }
        return JSONResponse(
            status_code=exc.code,
            content=content
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request,
        exc: RequestValidationError
    ):
        content = {
            "meta": {
                "code": status.HTTP_422_UNPROCESSABLE_ENTITY,
                "error": str(exc.errors),
                "message": "A required value is missing. Please check."
            },
            "data": None
        }
        return JSONResponse(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            content=content
        )
