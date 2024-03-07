import pydantic


class SignUpUserRequest(pydantic.BaseModel):
    email: str
    password: str
