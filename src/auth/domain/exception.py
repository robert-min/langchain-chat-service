from shared.domain.exception import BaseHttpException


class AuthServiceError(BaseHttpException):
    def __init__(
            self, code: int, message: str, log: str, err: Exception = None
            ) -> None:
        super().__init__(code, message, log)
