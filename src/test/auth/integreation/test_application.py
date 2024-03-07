import pytest
from auth.domain.entity import Auth
from auth.application.command import AuthCommandUseCase
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.application.query import AuthQueryUseCase


# Mock data
EMAIL = "test@naver.com"
PASSWORD = "test1234"


@pytest.fixture
def command(postgre_session):
    yield AuthCommandUseCase(
        AuthRepository(),
        SignUpService(),
        AuthQueryUseCase(AuthRepository(), postgre_session),
        postgre_session
    )


def test_application_can_sign_up_user(postgre_session, command):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when
    result = command.sign_up_user(auth_entity)

    # then
    assert result.email == EMAIL

    # clear
    result = AuthRepository().delete(postgre_session, auth_entity)
    assert result.email == EMAIL
