import jwt
from datetime import datetime, timedelta
from auth.domain.entity import Auth, Token
from shared.infra.config import settings


class LogInService:
    HOURS: int = 5

    def create_token(self, entity: Auth) -> Token:
        token = jwt.encode({
            "email": entity.email,
            "exp": datetime.utcnow() + timedelta(hours=self.HOURS)
        }, settings.TOKEN_KEY, algorithm="HS256")
        return Token.new(entity.email, token)
