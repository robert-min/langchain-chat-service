import pytest
from auth.domain.entity import Auth
from auth.infra.database.repository import AuthRepository

# Mock data
EMAIL = "test@naver.com"
PASSWORD = "test1234"


@pytest.mark.order(1)
@pytest.mark.asyncio
async def test_auth_can_sign_up_user_with_valid(client):
    # given
    mock = {
        "email": EMAIL,
        "password": PASSWORD
    }

    # when
    response = client.post(
        "/auth/signup",
        json=mock
    )

    # then
    assert response.status_code == 200
    assert response.json()["meta"]["message"] == "ok"
    assert response.json()["data"]["email"] == EMAIL


@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_auth_can_log_in_user_with_valid(client):
    # given
    mock = {
        "email": EMAIL,
        "password": PASSWORD
    }

    # when
    response = client.post(
        "/auth/login",
        json=mock
    )

    # then
    assert response.status_code == 200
    assert response.json()["meta"]["message"] == "ok"
    assert response.json()["data"]["id"] == EMAIL


@pytest.mark.order(4)
def test_auth_repository_can_delete_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL)

    # when : 계정 삭제
    result = AuthRepository().delete(postgre_session, auth_entity)

    # then
    assert result.email == EMAIL
