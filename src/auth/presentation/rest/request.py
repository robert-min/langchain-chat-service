import pydantic


class SignUpUserRequest(pydantic.BaseModel):
    email: str
    password: str


class LogInUserRequest(pydantic.BaseModel):
    email: str
    password: str
