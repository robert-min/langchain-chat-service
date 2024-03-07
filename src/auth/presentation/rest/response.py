import pydantic
from auth.domain.entity import Auth
from shared.infra.fastapi.util import make_response


class SignUpResponse(pydantic.BaseModel):
    auth_info: Auth

    def build(self):
        return make_response(
            {"email": self.auth_info.email}
        )
