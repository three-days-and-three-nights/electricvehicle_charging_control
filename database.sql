-- 创建数据库
CREATE DATABASE IF NOT EXISTS golden_arrow
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- 选择数据库
USE golden_arrow;

DROP TABLE IF EXISTS `vehicles`;
-- 车辆信息表
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,         -- 车辆的唯一标识符
    car_name VARCHAR(100) DEFAULT NULL,                -- 车辆名称（可为空）
    electromobile_info_id VARCHAR(50) NOT NULL,        -- 电动汽车信息ID
    sequence_number VARCHAR(50) NOT NULL,              -- 车辆序列号
    equipment_number VARCHAR(50) NOT NULL,             -- 设备号
    control_center_id VARCHAR(50) NOT NULL,            -- 中心控制ID
    status VARCHAR(10) NOT NULL,                       -- 车辆状态，例如 '0' 表示正常
    defense_status VARCHAR(10) NOT NULL,               -- 防御状态，例如 '0' 表示未启用
    mac_address VARCHAR(50) DEFAULT NULL,              -- MAC 地址（可为空）
    bluetooth_name VARCHAR(50),                        -- 蓝牙名称
    contact_number VARCHAR(20) NOT NULL,               -- 联系电话号码
    equipment_version VARCHAR(20) NOT NULL,            -- 设备版本
    total_distance_meters DECIMAL(10, 1) DEFAULT 0.0,  -- 总行驶距离（单位：米）
    share_key BOOLEAN NOT NULL                         -- 是否共享密钥，布尔值（true 或 false）
);

-- 车辆历史位置表
CREATE TABLE IF NOT EXISTS vehicle_location_history (
    location_id INT AUTO_INCREMENT PRIMARY KEY,       -- 位置记录的唯一标识符
    sequence_number VARCHAR(50) NOT NULL,             -- 外键，关联车辆信息表的ID
    latitude DECIMAL(10, 7) NOT NULL,                 -- 纬度
    longitude DECIMAL(10, 7) NOT NULL,                -- 经度
    recorded_at DATETIME NOT NULL,                    -- 记录时间
    FOREIGN KEY (sequence_number) REFERENCES vehicles(sequence_number) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 骑行记录表
CREATE TABLE IF NOT EXISTS cycling_records (
    cycling_record_id INT AUTO_INCREMENT PRIMARY KEY,  -- 自增主键，用于唯一标识每条骑行记录
    cycling_report_id VARCHAR(50) NOT NULL,            -- 报告ID，用于关联骑行报告详情
    sequence_number VARCHAR(50) NOT NULL,              -- 车辆序列号
    start_latitude DECIMAL(10, 7) NOT NULL,            -- 起始纬度
    start_longitude DECIMAL(10, 7) NOT NULL,           -- 起始经度
    start_address VARCHAR(255) NOT NULL,               -- 起始地址
    end_latitude DECIMAL(10, 7) NOT NULL,              -- 结束纬度
    end_longitude DECIMAL(10, 7) NOT NULL,             -- 结束经度
    end_address VARCHAR(255) NOT NULL,                 -- 结束地址
    start_time DATETIME NOT NULL,                      -- 起始时间
    end_time DATETIME NOT NULL,                        -- 结束时间
    duration_hours DECIMAL(5, 2) NOT NULL,             -- 持续时间（单位：小时）
    duration_seconds DECIMAL(10, 2) NOT NULL,          -- 持续时间（单位：秒）
    distance_km DECIMAL(10, 2) NOT NULL,               -- 距离（单位：公里）
    gaode_travel_id VARCHAR(50) DEFAULT NULL,          -- 高德地图旅行ID（可为空）
    gaode_distance_km DECIMAL(10, 2) DEFAULT NULL,     -- 高德地图骑行距离（单位：公里）
    trip_id INT NOT NULL,                              -- 旅行ID
    created_by VARCHAR(50) DEFAULT NULL,               -- 创建者（可为空）
    created_at DATETIME NOT NULL,                      -- 创建时间
    updated_by VARCHAR(50) DEFAULT NULL,               -- 更新者（可为空）
    updated_at DATETIME DEFAULT NULL,                  -- 更新时间
    FOREIGN KEY (sequence_number) REFERENCES vehicles(sequence_number) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4

-- 骑行报告详情表
CREATE TABLE IF NOT EXISTS cycling_report_details (
    cycling_report_id VARCHAR(50) PRIMARY KEY,       -- 报告ID
    device_time DATETIME NOT NULL,                   -- 设备记录时间
    equipment_number VARCHAR(50) NOT NULL,           -- 设备号
    north_or_south VARCHAR(1) DEFAULT NULL,          -- 北纬或南纬标记（可为空）
    latitude DECIMAL(10, 7) NOT NULL,                -- 纬度
    east_or_west VARCHAR(1) DEFAULT NULL,            -- 东经或西经标记（可为空）
    longitude DECIMAL(10, 7) NOT NULL,               -- 经度
    height DECIMAL(10, 2) DEFAULT NULL,              -- 高度（可为空）
    gps_speed DECIMAL(10, 2) DEFAULT NULL,           -- GPS速度（可为空）
    angle DECIMAL(5, 2) DEFAULT NULL,               -- 角度（可为空）
    trip_id INT DEFAULT NULL,                       -- 旅行ID
    mileage_meters DECIMAL(10, 2) NOT NULL,         -- 行驶里程（单位：米）
    signal_status VARCHAR(50) DEFAULT NULL,         -- 信号状态（可为空）
    charge_level DECIMAL(5, 2) DEFAULT NULL,        -- 电量状态（可为空）
    endurance DECIMAL(5, 2) DEFAULT NULL,           -- 耐力（可为空）
    voltage DECIMAL(5, 2) DEFAULT NULL,             -- 电压（可为空）
    temperature DECIMAL(5, 2) DEFAULT NULL,         -- 温度（可为空）
    FOREIGN KEY (cycling_report_id) REFERENCES cycling_records(cycling_report_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 车辆电量表
CREATE TABLE IF NOT EXISTS vehicle_battery (
    vehicle_battery_id INT AUTO_INCREMENT PRIMARY KEY, -- 电量记录的唯一标识符
    equipment_number VARCHAR(50) NOT NULL,             -- 外键，关联车辆信息表的设备id
    battery_level DECIMAL(5, 2) NOT NULL,              -- 电量水平（单位：%）
    recorded_at DATETIME NOT NULL,                     -- 记录时间
    FOREIGN KEY (equipment_number) REFERENCES vehicles(equipment_number) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 定时任务表
CREATE TABLE IF NOT EXISTS scheduled_tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,         -- 任务的唯一标识符
    task_name VARCHAR(100) NOT NULL,                -- 任务名称
    task_type VARCHAR(50) NOT NULL,                 -- 任务类型
    schedule_expression VARCHAR(50) NOT NULL,       -- 定时调度表达式
    last_run_at DATETIME DEFAULT NULL,              -- 上次运行时间
    status VARCHAR(50) DEFAULT 'pending'            -- 任务状态（默认为 'pending'）
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 充电控制表
CREATE TABLE IF NOT EXISTS charging_control (
    control_id INT AUTO_INCREMENT PRIMARY KEY,     -- 充电控制记录的唯一标识符
    vehicle_id INT NOT NULL,                       -- 外键，关联车辆信息表的ID
    command VARCHAR(50) NOT NULL,                  -- 控制命令
    status VARCHAR(50) DEFAULT 'pending',          -- 控制状态（默认为 'pending'）
    issued_at DATETIME NOT NULL,                   -- 命令发出时间
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


-- 推送消息表
CREATE TABLE IF NOT EXISTS push_notifications (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,  -- 推送消息的唯一标识符
    vehicle_id INT NOT NULL,                         -- 外键，关联车辆信息表的ID
    message TEXT NOT NULL,                           -- 推送消息内容
    notification_type VARCHAR(50) NOT NULL,          -- 推送消息类型
    sent_at DATETIME NOT NULL,                       -- 消息发送时间
    status VARCHAR(50) DEFAULT 'pending',            -- 消息状态（默认为 'pending'）
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
