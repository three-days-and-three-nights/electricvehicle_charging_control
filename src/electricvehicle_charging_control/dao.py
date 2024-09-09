from typing import Generic, List

from sqlalchemy.orm import Session

from electricvehicle_charging_control.models import Vehicle
from electricvehicle_charging_control.schemas import CreateSchema, ModelType, UpdateSchema ,CreateVehicleSchema,UpdateVehicleSchema

class BaseDAO(Generic[ModelType], CreateSchema,UpdateSchema):
    model: ModelType
    def get(self,session: Session, offset=0, limit=10) -> List[ModelType]:
        result = session.query(self.model).offset(offset).limit(limit).all()
        return result


    def get_by_id(self, session: Session, pk: int) -> ModelType:
        return  session.query(self.model).get(pk)

class VehicleDAO(BaseDAO[Vehicle], CreateVehicleSchema,UpdateVehicleSchema):
    model = Vehicle
