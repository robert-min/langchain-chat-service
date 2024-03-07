from auth.domain.entity import Auth
from auth.domain.util.cipher import CipherManager


class SignUpService:
    cipher_manager: CipherManager = CipherManager()

    def encrypt_user(self, auth_entity: Auth):
        # Encrypt_password
        encrypt_password = self.cipher_manager.encrypt_password(
            auth_entity.password
        )
        return Auth(
            email=auth_entity.email,
            password=encrypt_password
        )
        
