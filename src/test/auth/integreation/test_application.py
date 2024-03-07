import pytest
from auth.domain.entity import Auth
from auth.application.command import AuthCommandUseCase
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.domain.service.log_in import LogInService
from auth.application.query import AuthQueryUseCase
from auth.domain.exception import AuthError
from shared.infra.database.connection import get_postgre_session

# Mock data
EMAIL = "test@naver.com"
PASSWORD = "test1234"


@pytest.fixture
def command():
    yield AuthCommandUseCase(
        AuthRepository(),
        SignUpService(),
        LogInService(),
        AuthQueryUseCase(AuthRepository(), get_postgre_session),
        get_postgre_session
    )


@pytest.mark.order(1)
def test_application_can_sign_up_user(command):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when
    result = command.sign_up_user(auth_entity)

    # then
    assert result.email == EMAIL


@pytest.mark.order(2)
def test_application_cannot_sign_up_user_with_already_exist(command):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # then
    with pytest.raises(AuthError):
        # when : 회원가입 요청
        command.sign_up_user(auth_entity)


@pytest.mark.order(2)
def test_application_cannot_sign_up_with_wrong_email_pattern(command):
    # given
    WRONG_EMAIL = "test!naver.com"
    auth_entity: Auth = Auth.new(WRONG_EMAIL, PASSWORD)

    # then
    with pytest.raises(AuthError):
        # when : 회원가입 요청
        command.sign_up_user(auth_entity)


@pytest.mark.order(3)
def test_application_can_log_in_user(command):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when
    result = command.log_in_user(auth_entity)

    # then
    assert result.id == EMAIL


@pytest.mark.order(4)
def test_application_cannot_log_in_user_with_not_existence_user(command):
    # given
    WRONG_EMAIL = "wrong@naver.com"
    auth_entity: Auth = Auth.new(WRONG_EMAIL, PASSWORD)

    # when
    with pytest.raises(AuthError):
        command.log_in_user(auth_entity)


@pytest.mark.order(4)
def test_application_cannot_log_in_user_with_wrong_password(command):
    # given
    WRONG_PASSWORD = "wrong123"
    auth_entity: Auth = Auth.new(EMAIL, WRONG_PASSWORD)

    # when
    with pytest.raises(AuthError):
        command.log_in_user(auth_entity)


@pytest.mark.order(5)
def test_clear_database(postgre_session):
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)
    result = AuthRepository().delete(postgre_session, auth_entity)
    assert result.email == EMAIL
