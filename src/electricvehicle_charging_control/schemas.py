from typing import Optional,TypeVar
from pydantic import BaseModel, constr
from electricvehicle_charging_control.models import BaseModel as DBModel

ModelType = TypeVar('ModelType', bound=DBModel)
CreateSchema = TypeVar('CreateSchema', bound=BaseModel)
UpdateSchema = TypeVar('UpdateSchema', bound=BaseModel)

# 定义主键字段的Mixin
class InDBMixin(BaseModel):
    class Config:
        orm_mode = True

# 车辆基础模型
class BaseVehicle(BaseModel):
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

# 车辆模型，继承InDBMixin并指定主键字段名称
class VehicleSchema(BaseVehicle, InDBMixin):
    vehicle_id: int  # 指定正确的主键字段名称

# 创建车辆时使用的模型
class CreateVehicleSchema(BaseVehicle):
    pass

# 更新车辆时使用的模型
class UpdateVehicleSchema(BaseVehicle):
    pass
