from enum import Enum
from starlette import status


class SignUpError(Enum):
    NonMatchEmail = {
        "code": status.HTTP_400_BAD_REQUEST,
        "message": "The ID is not in email format. Please enter again.",
        "log": "User service sign up fail with wrong email."
    }
    AlreadyUserError = {
        "code": status.HTTP_400_BAD_REQUEST,
        "message": "The user email is already created. Please sign up another email.",
        "log": "User service sign up fail with already existence email."
    }
