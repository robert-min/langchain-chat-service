from typing import List
from sqlalchemy.orm import Session
from auth.domain.entity import Auth
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.domain.service.log_in import LogInService
from auth.application.query import AuthQueryUseCase
from auth.domain.exception import AuthError
from auth.domain.errorcode import LogInError


class AuthCommandUseCase:
    def __init__(
        self,
        auth_repository: AuthRepository,
        sign_up_service: SignUpService,
        log_in_service: LogInService,
        auth_query: AuthQueryUseCase,
        session: Session
    ) -> None:
        self.auth_repository = auth_repository
        self.sign_up_service = sign_up_service
        self.log_in_service = log_in_service
        self.auth_query = auth_query
        self.session = session

    def sign_up_user(self, entity: Auth) -> Auth:
        # sign up user with encrypting user info.
        entities: List[Auth] = self.auth_query.get_all_auth_info()
        auth: Auth = self.sign_up_service.encrypt_user(entity, entities)
        with self.session() as session:
            return self.auth_repository.create(session, auth)

    def log_in_user(self, entity: Auth) -> Auth:
        # check user data
        user_info: Auth | None = self.auth_query.get_auth_info(entity)
        if not user_info:
            raise AuthError(**LogInError.NotFoundData.value)
        if user_info.email != entity.email:
            raise AuthError(**LogInError.WrongPasswordError.value)

        # make token
        return self.log_in_service.create_token(entity)
