import pytest
from auth.domain.entity import Auth
from auth.domain.service.sign_up import SignUpService
from auth.domain.util.cipher import CipherManager
from auth.domain.exception import AuthServiceError

# Mock data
EMAIL = "test@naver.com"
PASSWORD = "test1234"


def test_can_sign_up_user_with_valid_user():
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when : 회원가입 요청
    result = SignUpService().encrypt_user(auth_entity, [])

    # then
    assert result.email == EMAIL
    assert CipherManager().decrypt_password(result.password) == PASSWORD


def test_cannot_sign_up_user_with_already_exist():
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # then
    with pytest.raises(AuthServiceError):
        # when : 회원가입 요청
        SignUpService().encrypt_user(auth_entity, [auth_entity])


def test_cannot_sign_up_user_with_with_wrong_email_pattern():
    # given
    WRONG_EMAIL = "test!naver.com"
    auth_entity: Auth = Auth.new(WRONG_EMAIL, PASSWORD)

    # then
    with pytest.raises(AuthServiceError):
        # when : 회원가입 요청
        SignUpService().encrypt_user(auth_entity, [])
