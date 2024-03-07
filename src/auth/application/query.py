from typing import List
from sqlalchemy.orm import Session
from auth.domain.entity import Auth
from auth.infra.database.repository import AuthRepository


class AuthQueryUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
        session: Session
    ) -> None:
        self.auth_repository = auth_repository
        self.session = session()

    def get_all_auth_info(self) -> List[Auth]:
        return self.auth_repository.get_all(self.session)
