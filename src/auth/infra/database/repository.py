from typing import List
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from auth.domain.entity import Auth
from auth.infra.database.model import Account
from auth.infra.database.mapper import AuthMapper
from shared.domain.exception import DBError
from shared.domain.errorcode import RepositoryError


class AuthRepository:
    def __init__(self) -> None:
        self.auth_mapper = AuthMapper()

    def create(self, session: Session, entity: Auth) -> Auth:
        try:
            account_model: Account = self.auth_mapper.to_model(entity)
            with session:
                session.add(account_model)
                session.commit()
            return Auth(email=entity.email)
        except Exception as e:
            raise DBError(**RepositoryError.DBProcess.value, err=e)

    def get(self, session: Session, entity: Auth) -> Auth | None:
        try:
            with session:
                query = select(Account).filter(Account.email == entity.email)
                account_model = session.execute(query).scalar_one()
            return self.auth_mapper.to_entity(account_model)
        except NoResultFound:
            return None
        except Exception as e:
            raise DBError(**RepositoryError.DBProcess.value, err=e)

    def get_all(self, session: Session) -> List[Auth]:
        try:
            with session:
                query = select(Account)
                accout_model_list = session.execute(query).scalars()
                return AuthMapper().to_entity_list(accout_model_list)
        except Exception as e:
            raise DBError(**RepositoryError.DBProcess.value, err=e)

    def delete(self, session: Session, entity: Auth) -> Auth:
        try:
            with session:
                query = select(Account).filter(Account.email == entity.email)
                account_model = session.execute(query).scalar_one()
                if account_model:
                    session.delete(account_model)
                session.commit()
            return Auth(email=entity.email)
        except Exception as e:
            raise DBError(**RepositoryError.DBProcess.value, err=e)
