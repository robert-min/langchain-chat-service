import re
from typing import List
from sqlalchemy.orm import Session
from auth.domain.entity import Auth, Token
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.domain.service.log_in import LogInService
from auth.application.query import AuthQueryUseCase
from auth.domain.exception import AuthError
from auth.domain.errorcode import LogInError, SignUpError
from auth.domain.util.cipher import CipherManager


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
        # check user data
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, entity.email):
            raise AuthError(**SignUpError.NonMatchEmail.value)

        entities: List[Auth] = self.auth_query.get_all_auth_info()
        for auth_entity in entities:
            if entity.email == auth_entity.email:
                raise AuthError(**SignUpError.AlreadyUserError.value)

        # encrypt password
        auth: Auth = self.sign_up_service.encrypt_user(entity)
        with self.session() as session:
            return self.auth_repository.create(session, auth)

    def log_in_user(self, entity: Auth) -> Token:
        # check user data
        user_info: Auth | None = self.auth_query.get_auth_info(entity)
        if not user_info:
            raise AuthError(**LogInError.NotFoundData.value)
        # decrypt password
        origin_password: str = CipherManager().decrypt_password(user_info.password)
        if origin_password != entity.password:
            raise AuthError(**LogInError.WrongPasswordError.value)

        # make token
        return self.log_in_service.create_token(entity)
