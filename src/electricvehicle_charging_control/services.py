"""Service"""
from typing import Generic, List

from sqlalchemy.orm import Session

from electricvehicle_charging_control.dao import VehicleDAO, BaseDAO
from electricvehicle_charging_control.models import Vehicle
from electricvehicle_charging_control.schemas import CreateSchema, ModelType, UpdateSchema


class BaseService(Generic[ModelType, CreateSchema, UpdateSchema]):
    dao: BaseDAO

    def get(self, session: Session, offset=0, limit=10) -> List[ModelType]:
        """"""
        return self.dao.get(session, offset=offset, limit=limit)

    def get_by_id(self, session: Session, pk: int) -> ModelType:
        """Get by id"""
        return self.dao.get_by_id(session, pk)


class ArticleService(BaseService[Vehicle, CreateSchema, UpdateSchema]):
    dao = VehicleDAO()
