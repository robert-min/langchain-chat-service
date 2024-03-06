from typing import TypeVar
from shared.domain.entity import EntityType
from shared.infra.database.model import Base

ModelType = TypeVar('ModelType', bound=Base)


class ModelMapperInterface:
    def to_entity(self, instance: ModelType) -> EntityType:
        """convert model instance to entity"""
        raise NotImplementedError

    def to_instance(self, entity: EntityType) -> ModelType:
        """convert entity to model instance"""
        raise NotImplementedError
