"""Models"""

from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Boolean, DECIMAL, ForeignKey,Text
from sqlalchemy.ext.declarative import declarative_base


class CustomBase:
    """https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html"""

    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_collate': 'utf8mb4_general_ci'
    }

# Base model
BaseModel = declarative_base(cls=CustomBase)

# 车辆信息表
class Vehicle(BaseModel):
    __tablename__ = 'vehicles'
    """Vehicles table"""
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)  # 车辆的唯一标识符
    car_name = Column(String(100), nullable=True, default=None)  # 车辆名称（可为空）
    electromobile_id = Column(String(50), nullable=False)  # 电动汽车信息ID
    serial_number = Column(String(50), nullable=False)  # 车辆序列号
    equipment_id = Column(String(50), nullable=False)  # 设备号
    control_center_id = Column(String(50), nullable=False)  # 中心控制ID
    status = Column(String(10), nullable=False)  # 车辆状态
    defense_status = Column(String(10), nullable=False)  # 防御状态
    mac_address = Column(String(50), nullable=True)  # MAC 地址（可为空）
    bluetooth_name = Column(String(50), nullable=False)  # 蓝牙名称
    contact_number = Column(String(20), nullable=False)  # 联系电话号码
    equipment_version = Column(String(20), nullable=False)  # 设备版本
    total_distance_meters = Column(DECIMAL(10, 1), default=0.0)  # 总行驶距离（单位：米）
    share_key = Column(Boolean, nullable=False)  # 是否共享密钥（布尔值）


# 车辆历史位置表
class VehicleLocationHistory(BaseModel):
    __tablename__ = 'vehicle_location_history'
    """Vehicle_location_history table"""
    location_id = Column(Integer, primary_key=True, autoincrement=True) # 位置记录的唯一标识符
    sequence_number = Column(String(50), ForeignKey('vehicles.sequence_number', ondelete='CASCADE'), nullable=False)  # 外键，关联车辆表
    latitude = Column(DECIMAL(10, 7), nullable=False)      # 纬度
    longitude = Column(DECIMAL(10, 7), nullable=False)     # 经度
    recorded_at = Column(DateTime, default=datetime.now, nullable=False) # 记录时间


class CyclingRecord(BaseModel):
    __tablename__ = 'cycling_records'
    """Cycling records table"""

    cycling_record_id = Column(Integer, primary_key=True, autoincrement=True)  # 自增主键
    cycling_report_id = Column(String(50), nullable=False)  # 报告ID
    sequence_number = Column(String(50), ForeignKey('vehicles.serial_number', ondelete='CASCADE'),
                             nullable=False)  # 车辆序列号
    start_latitude = Column(DECIMAL(10, 7), nullable=False)  # 起始纬度
    start_longitude = Column(DECIMAL(10, 7), nullable=False)  # 起始经度
    start_address = Column(String(255), nullable=False)  # 起始地址
    end_latitude = Column(DECIMAL(10, 7), nullable=False)  # 结束纬度
    end_longitude = Column(DECIMAL(10, 7), nullable=False)  # 结束经度
    end_address = Column(String(255), nullable=False)  # 结束地址
    start_time = Column(DateTime, nullable=False)  # 起始时间
    end_time = Column(DateTime, nullable=False)  # 结束时间
    duration_hours = Column(DECIMAL(5, 2), nullable=False)  # 持续时间（小时）
    duration_seconds = Column(DECIMAL(10, 2), nullable=False)  # 持续时间（秒）
    distance_km = Column(DECIMAL(10, 2), nullable=False)  # 距离（公里）
    gaode_travel_id = Column(String(50), default=None)  # 高德地图旅行ID
    gaode_distance_km = Column(DECIMAL(10, 2), default=None)  # 高德地图骑行距离（公里）
    trip_id = Column(Integer, nullable=False)  # 旅行ID
    created_by = Column(String(50), default=None)  # 创建者
    created_at = Column(DateTime, nullable=False)  # 创建时间
    updated_by = Column(String(50), default=None)  # 更新者
    updated_at = Column(DateTime, default=None)  # 更新时间


class CyclingReportDetail(BaseModel):
    __tablename__ = 'cycling_report_details'
    """Cycling report details table"""

    cycling_report_id = Column(String(50), ForeignKey('cycling_records.cycling_report_id', ondelete='CASCADE'),
                               primary_key=True)  # 报告ID
    device_time = Column(DateTime, nullable=False)  # 设备记录时间
    equipment_number = Column(String(50), nullable=False)  # 设备号
    north_or_south = Column(String(1), default=None)  # 北纬或南纬标记
    latitude = Column(DECIMAL(10, 7), nullable=False)  # 纬度
    east_or_west = Column(String(1), default=None)  # 东经或西经标记
    longitude = Column(DECIMAL(10, 7), nullable=False)  # 经度
    height = Column(DECIMAL(10, 2), default=None)  # 高度
    gps_speed = Column(DECIMAL(10, 2), default=None)  # GPS速度
    angle = Column(DECIMAL(5, 2), default=None)  # 角度
    trip_id = Column(Integer, default=None)  # 旅行ID
    mileage_meters = Column(DECIMAL(10, 2), nullable=False)  # 行驶里程（米）
    signal_status = Column(String(50), default=None)  # 信号状态
    charge_level = Column(DECIMAL(5, 2), default=None)  # 电量状态
    endurance = Column(DECIMAL(5, 2), default=None)  # 耐力
    voltage = Column(DECIMAL(5, 2), default=None)  # 电压
    temperature = Column(DECIMAL(5, 2), default=None) # 温度


class VehicleBattery(BaseModel):
    __tablename__ = 'vehicle_battery'
    """Vehicle battery table"""

    vehicle_battery_id = Column(Integer, primary_key=True, autoincrement=True)  # 电量记录的唯一标识符
    equipment_number = Column(String(50), ForeignKey('vehicles.equipment_number', ondelete='CASCADE'),
                              nullable=False)  # 外键，关联车辆信息表的设备号
    battery_level = Column(DECIMAL(5, 2), nullable=False)  # 电量水平（单位：%）
    recorded_at = Column(DateTime, default=datetime.now, nullable=False) # 记录时间


class ScheduledTask(BaseModel):
    __tablename__ = 'scheduled_tasks'
    """Scheduled tasks table"""

    task_id = Column(Integer, primary_key=True, autoincrement=True)  # 任务的唯一标识符
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id', ondelete='CASCADE'), nullable=False)  # 外键，关联车辆信息表的ID
    task_name = Column(String(100), nullable=False)  # 任务名称
    task_type = Column(String(50), nullable=False)  # 任务类型
    schedule_expression = Column(String(50), nullable=False)  # 定时调度表达式
    last_run_at = Column(DateTime, default=None)  # 上次运行时间
    status = Column(String(50), default='pending')  # 任务状态（默认为 'pending'）


class ChargingControl(BaseModel):
    __tablename__ = 'charging_control'
    """Charging control table"""

    control_id = Column(Integer, primary_key=True, autoincrement=True)  # 充电控制记录的唯一标识符
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id', ondelete='CASCADE'), nullable=False)  # 外键，关联车辆信息表的ID
    status = Column(String(50), default='pending')  # 控制状态（默认为 'pending'）
    issued_at = Column(DateTime, nullable=False)  # 命令发出时间


class PushNotification(BaseModel):
    __tablename__ = 'push_notifications'
    """Push notifications table"""

    notification_id = Column(Integer, primary_key=True, autoincrement=True)  # 推送消息的唯一标识符
    vehicle_id = Column(Integer, ForeignKey('vehicles.vehicle_id', ondelete='CASCADE'), nullable=False)  # 外键，关联车辆信息表的ID
    message = Column(Text, nullable=False)  # 推送消息内容
    notification_type = Column(String(50), nullable=False)  # 推送消息类型
    sent_at = Column(DateTime, nullable=False)  # 消息发送时间
    status = Column(String(50), default='pending')  # 消息状态（默认为 'pending'）
