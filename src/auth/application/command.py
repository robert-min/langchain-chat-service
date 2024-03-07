from typing import List
from sqlalchemy.orm import Session
from auth.domain.entity import Auth
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.application.query import AuthQueryUseCase


class AuthCommandUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
        sign_up_service: SignUpService,
        auth_query: AuthQueryUseCase,
        session: Session
    ) -> None:
        self.auth_repository = auth_repository
        self.sign_up_service = sign_up_service
        self.auth_query = auth_query
        self.session = session

    def sign_up_user(self, entity: Auth) -> Auth:
        # sign up user with encrypting user info.
        entities: List[Auth] = self.auth_query.get_all_auth_info()
        auth: Auth = self.sign_up_service.encrypt_user(entity, entities)
        return self.auth_repository.create(self.session, auth)
