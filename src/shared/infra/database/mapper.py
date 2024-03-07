from typing import TypeVar, List
from shared.domain.entity import EntityType
from shared.infra.database.model import Base

ModelType = TypeVar('ModelType', bound=Base)


class ModelMapperInterface:
    def to_entity(self, model: ModelType) -> EntityType:
        """convert model instance to entity"""
        raise NotImplementedError

    def to_model(self, entity: EntityType) -> ModelType:
        """convert entity to model instance"""
        raise NotImplementedError

    def to_entity_list(self, models: List[ModelType]) -> List[EntityType]:
        return [self.to_entity(model=m) for m in models]
