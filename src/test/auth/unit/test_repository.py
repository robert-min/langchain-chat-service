import pytest
import base64
from sqlalchemy import select
from auth.domain.entity import Auth
from auth.infra.database.model import Account
from auth.infra.database.mapper import AuthMapper
from sqlalchemy.exc import NoResultFound

# Mock data
EMAIL = "test@naver.com"
PASSWORD = base64.b64encode(bytes("test1234", 'utf-8'))


@pytest.mark.order(0)
def test_auth_repository_can_insert_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL, PASSWORD)

    # when : 계정 등록
    account_model: Account = AuthMapper().to_model(auth_entity)
    with postgre_session as session:
        session.add(account_model)
        session.commit()

    # then
    assert auth_entity.email == EMAIL
    assert auth_entity.password == PASSWORD


@pytest.mark.order(1)
def test_auth_repository_can_get_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL)

    # when : 계정 조회
    with postgre_session as session:
        query = select(Account).filter(Account.email == auth_entity.email)
        account_model = session.execute(query).scalar_one()

        auth_entity = AuthMapper().to_entity(account_model)

    # then
    assert auth_entity.email == EMAIL
    assert auth_entity.password == PASSWORD


@pytest.mark.order(1)
def test_auth_repository_cannot_get_user_account_with_no_user(postgre_session):
    # given : 없는 계정 정보 요청
    WRONG_EMAIL: str = "wrong@naver.com"
    auth_entity: Auth = Auth.new(WRONG_EMAIL)

    # then : NoResultFound
    with pytest.raises(NoResultFound):
        # when : 계정 조회
        with postgre_session as session:
            query = select(Account).filter(Account.email == auth_entity.email)
            account_model = session.execute(query).scalar_one()

            auth_entity = AuthMapper().to_entity(account_model)


@pytest.mark.order(2)
def test_auth_repository_can_get_all_user_account(postgre_session):
    # given

    # when : 계정 전체 조회
    with postgre_session as session:
        query = select(Account)
        accout_model_list = session.execute(query).scalars()
        auth_entity_list = AuthMapper().to_entity_list(accout_model_list)

    # then
    assert len(auth_entity_list) > 0


@pytest.mark.order(4)
def test_auth_repository_can_delete_user_account(postgre_session):
    # given
    auth_entity: Auth = Auth.new(EMAIL)

    # when : 계정 삭제
    with postgre_session as session:
        query = select(Account).filter(Account.email == auth_entity.email)
        account_model = session.execute(query).scalar_one()
        if account_model:
            session.delete(account_model)
        session.commit()

    # then
    assert auth_entity.email == EMAIL
