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


class LogInError(Enum):
    NotFoundData = {
        "code": status.HTTP_404_NOT_FOUND,
        "message": "This account is not registered.",
        "log": "User Error. Request non data on DB."
    }
    WrongPasswordError = {
        "code": status.HTTP_401_UNAUTHORIZED,
        "message": "The password is incorrect. Please check again..",
        "log": "User request fail with wrong password."
    }
