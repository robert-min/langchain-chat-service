import pytest
import base64
from auth.domain.entity import Auth
from shared.domain.exception import DBError
from auth.infra.database.repository import AuthRepository


# Mock data
EMAIL = "test@naver.com"
PASSWORD = base64.b64encode(bytes("test1234", 'utf-8'))


@pytest.mark.order(0)
def test_auth_repository_can_create_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when : 계정 등록
    result = AuthRepository().create(postgre_session, auth_entity)

    # then
    assert result.email == EMAIL


@pytest.mark.order(1)
def test_auth_repository_can_get_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL)

    # when : 계정 조회
    result = AuthRepository().get(postgre_session, auth_entity)

    # then
    assert result.email == EMAIL
    assert result.password == PASSWORD


@pytest.mark.order(1)
def test_auth_repository_cannot_get_user_account_with_no_user(postgre_session):
    # given : 없는 계정 정보 요청
    WRONG_EMAIL: str = "wrong@naver.com"
    auth_entity: Auth = Auth.new(WRONG_EMAIL)

    # when : 계정 조회
    result = AuthRepository().get(postgre_session, auth_entity)

    # then
    assert not result


@pytest.mark.order(2)
def test_auth_repository_can_get_all_user_account(postgre_session):
    # given

    # when : 계정 전체 조회
    auth_entity_list = AuthRepository().get_all(postgre_session)

    # then
    assert len(auth_entity_list) > 0


@pytest.mark.order(4)
def test_auth_repository_can_delete_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL)

    # when : 계정 삭제
    result = AuthRepository().delete(postgre_session, auth_entity)

    # then
    assert result.email == EMAIL
