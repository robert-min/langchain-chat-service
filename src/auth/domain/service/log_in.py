import jwt
from datetime import datetime, timedelta
from auth.domain.entity import Auth
from shared.infra.config import settings


class LogInService:
    HOURS: int = 5

    def create_token(self, entity: Auth) -> str:
        return jwt.encode({
            "email": entity.email,
            "exp": datetime.utcnow() + timedelta(hours=self.HOURS)
        }, settings.TOKEN_KEY, algorithm="HS256")
