import pydantic
from dataclasses import asdict
from auth.domain.entity import Auth, Token
from shared.infra.fastapi.util import make_response


class SignUpResponse(pydantic.BaseModel):
    auth_info: Auth

    def build(self):
        return make_response(
            {"email": self.auth_info.email}
        )


class LogInResponse(pydantic.BaseModel):
    token_info: Token

    def build(self):
        return make_response(
            asdict(self.token_info)
        )
