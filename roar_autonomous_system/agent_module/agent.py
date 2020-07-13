from abc import ABC, abstractmethod
import logging
from roar_autonomous_system.utilities_module.vehicle_models import Vehicle
from roar_autonomous_system.utilities_module.camera_models import Camera
from roar_autonomous_system.utilities_module.data_structures_models import SensorsData, IMUData, Transform
from roar_autonomous_system.utilities_module.vehicle_models import VehicleControl
from typing import Optional, List


class Agent(ABC):
    """
    Abstract Agent class that define the minimum of a ROAR agent.

    Inherited agent can perform different duties.

    """

    def __init__(self,
                 vehicle: Vehicle,
                 front_rgb_camera: Optional[Camera] = None,
                 front_depth_camera: Optional[Camera] = None,
                 rear_rgb_camera: Optional[Camera] = None,
                 imu: Optional[IMUData] = None):
        self.vehicle = vehicle
        self.front_rgb_camera = front_rgb_camera
        self.front_depth_camera = front_depth_camera
        self.rear_rgb_camera = rear_rgb_camera
        self.imu = imu
        self.logger = logging.getLogger(__name__)
        self.transform_history: List[Transform] = []

    @abstractmethod
    def run_step(self, sensors_data: SensorsData, vehicle: Vehicle) -> VehicleControl:
        """
        Receive Sensor Data and vehicle state information on every step and return a control

        Args:
            sensors_data: sensor data on this frame
            vehicle: vehicle state on this frame

        Returns:
            Vehicle Control

        """
        self.sync_data(sensors_data=sensors_data, vehicle=vehicle)
        return VehicleControl()

    def sync_data(self, sensors_data: SensorsData, vehicle: Vehicle):
        self.vehicle = vehicle
        if self.front_rgb_camera is not None:
            self.front_rgb_camera.data = sensors_data.front_rgb.data
        if self.front_depth_camera is not None:
            self.front_depth_camera.data = sensors_data.front_depth.data
        if self.rear_rgb_camera is not None:
            self.rear_rgb_camera.data = sensors_data.rear_rgb.data
        if self.imu is not None:
            self.imu = sensors_data.imu_data