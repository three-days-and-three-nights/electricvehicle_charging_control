from datetime import datetime
from typing import Optional, TypeVar

from pydantic import BaseModel, constr
from electricvehicle_charging_control.models import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)

class VehicleBase(BaseModel):
    car_name: Optional[constr(max_length=100)] = None
    electromobile_info_id: constr(max_length=50)
    sequence_number: constr(max_length=50)
    equipment_number: constr(max_length=50)
    control_center_id: constr(max_length=50)
    status: constr(max_length=10)
    defense_status: constr(max_length=10)
    mac_address: Optional[constr(max_length=50)] = None
    bluetooth_name: Optional[constr(max_length=50)] = None
    contact_number: constr(max_length=20)
    equipment_version: constr(max_length=20)
    total_distance_meters: float = 0.0
    share_key: bool

class VehicleInDB(VehicleBase):
    vehicle_id: int

    class Config:
        orm_mode = True

class CreateVehicleSchema(VehicleBase):
    pass

class UpdateVehicleSchema(BaseModel):
    car_name: Optional[constr(max_length=100)] = None
    electromobile_info_id: Optional[constr(max_length=50)] = None
    sequence_number: Optional[constr(max_length=50)] = None
    equipment_number: Optional[constr(max_length=50)] = None
    control_center_id: Optional[constr(max_length=50)] = None
    status: Optional[constr(max_length=10)] = None
    defense_status: Optional[constr(max_length=10)] = None
    mac_address: Optional[constr(max_length=50)] = None
    bluetooth_name: Optional[constr(max_length=50)] = None
    contact_number: Optional[constr(max_length=20)] = None
    equipment_version: Optional[constr(max_length=20)] = None
    total_distance_meters: Optional[float] = None
    share_key: Optional[bool] = None
