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
async def test_auth_cannot_sign_up_user_with_already_exist(client):
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
    assert response.status_code == 400
    assert response.json()["meta"]["message"] == "The user email is already created. Please sign up another email."


@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_auth_cannot_sign_up_user_with_wrong_email_pattern(client):
    # given
    mock = {
        "email": "wrong!naver.com",
        "password": PASSWORD
    }

    # when
    response = client.post(
        "/auth/signup",
        json=mock
    )

    # then
    assert response.status_code == 400
    assert response.json()["meta"]["message"] == "The ID is not in email format. Please enter again."


@pytest.mark.order(2)
@pytest.mark.asyncio
async def test_auth_cannot_sign_up_user_with_wrong_body(client):
    # given
    mock = {
        "email": "wrong!naver.com"
    }

    # when
    response = client.post(
        "/auth/signup",
        json=mock
    )

    # then
    assert response.status_code == 422
    assert response.json()["meta"]["message"] == "A required value is missing. Please check."


@pytest.mark.order(3)
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
@pytest.mark.asyncio
async def test_auth_cannot_log_in_user_with_not_existence_user(client):
    # given
    mock = {
        "email": "wrnog@naver.com",
        "password": PASSWORD
    }

    # when
    response = client.post(
        "/auth/login",
        json=mock
    )

    # then
    assert response.status_code == 404
    assert response.json()["meta"]["message"] == "This account is not registered."
    

@pytest.mark.order(4)
@pytest.mark.asyncio
async def test_auth_cannot_log_in_user_with_wrong_password(client):
    # given
    mock = {
        "email": EMAIL,
        "password": "wrnog1234"
    }

    # when
    response = client.post(
        "/auth/login",
        json=mock
    )

    # then
    assert response.status_code == 401
    assert response.json()["meta"]["message"] == "The password is incorrect. Please check again.."


@pytest.mark.order(5)
def test_auth_repository_can_delete_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL)

    # when : 계정 삭제
    result = AuthRepository().delete(postgre_session, auth_entity)

    # then
    assert result.email == EMAIL
