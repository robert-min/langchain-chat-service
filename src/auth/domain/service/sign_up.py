import re
from typing import List
from auth.domain.entity import Auth
from auth.domain.exception import AuthServiceError
from auth.domain.errorcode import SignUpError
from auth.domain.util.cipher import CipherManager


class SignUpService:
    cipher_manager: CipherManager = CipherManager()

    def encrypt_user(self, auth_entity: Auth, entities: List[Auth]):
        # Validate user's input
        self.__check_user_email_pattern(auth_entity.email)
        self.__check_user_existence(auth_entity.email, entities)

        # Encrypt_password
        encrypt_password = self.cipher_manager.encrypt_password(
            auth_entity.password
        )
        return Auth(
            email=auth_entity.email,
            password=encrypt_password
        )

    @staticmethod
    def __check_user_email_pattern(user_email: str):
        """Check ID is in email pattern."""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, user_email):
            raise AuthServiceError(**SignUpError.NonMatchEmail.value)

    @staticmethod
    def __check_user_existence(user_email: str, entities: List[Auth]):
        for auth_entity in entities:
            if user_email == auth_entity.email:
                raise AuthServiceError(**SignUpError.AlreadyUserError.value)
