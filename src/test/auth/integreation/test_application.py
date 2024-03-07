import pytest
from auth.domain.entity import Auth
from auth.application.command import AuthCommandUseCase
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.domain.service.log_in import LogInService
from auth.application.query import AuthQueryUseCase
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
def test_application_can_log_in_user(command):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when
    result = command.log_in_user(auth_entity)

    # then
    assert result.id == EMAIL


@pytest.mark.order(5)
def test_clear_database(postgre_session):
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)
    result = AuthRepository().delete(postgre_session, auth_entity)
    assert result.email == EMAIL
