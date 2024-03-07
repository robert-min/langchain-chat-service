from shared.infra.database.mapper import ModelMapperInterface
from auth.domain.entity import Auth as AuthEntity
from auth.infra.database.model import Account as AccountModel


class AuthMapper(ModelMapperInterface):
    def to_entity(self, model: AccountModel) -> AuthEntity:
        return AuthEntity(
            email=model.email,
            password=model.password,
        )

    def to_model(self, entity: AuthEntity) -> AccountModel:
        return AccountModel(
            email=entity.email,
            password=entity.password
        )
