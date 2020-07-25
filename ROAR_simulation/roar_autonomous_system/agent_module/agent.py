from abc import ABC, abstractmethod
import logging
from ROAR_simulation.roar_autonomous_system.utilities_module.vehicle_models \
    import (
    Vehicle,
)
from ROAR_simulation.roar_autonomous_system.utilities_module \
    .data_structures_models import (
    SensorsData,
    IMUData,
    Transform,
)
from ROAR_simulation.roar_autonomous_system.utilities_module.vehicle_models \
    import (
    VehicleControl,
)
from typing import Optional, List
from pathlib import Path
import cv2
import numpy as np

from ROAR_simulation.roar_autonomous_system.configurations.agent_settings \
    import \
    AgentConfig


class Agent(ABC):
    """
    Abstract Agent class that define the minimum of a ROAR agent.

    Inherited agent can perform different duties.

    """

    def __init__(self,
                 vehicle: Vehicle,
                 agent_settings: AgentConfig,
                 imu: Optional[IMUData] = None):
        """
        Initialize cameras, output folder, and logging utilities

        Args:
            vehicle: Vehicle instance
            agent_settings: User specified settings for Agent
            imu: IMU data (will be deprecated to be passed in like this)
        """
        self.logger = logging.getLogger(__name__)

        self.vehicle = vehicle
        self.agent_settings = agent_settings
        self.front_rgb_camera = agent_settings.front_rgb_cam
        self.front_depth_camera = agent_settings.front_depth_cam
        self.rear_rgb_camera = agent_settings.rear_rgb_cam
        self.imu = imu

        self.output_folder_path = \
            Path(self.agent_settings.output_data_folder_path)
        self.front_depth_camera_output_folder_path = \
            self.output_folder_path / "front_depth"
        self.front_rgb_camera_output_folder_path = \
            self.output_folder_path / "front_rgb"
        self.rear_rgb_camera_output_folder_path = \
            self.output_folder_path / "rear_rgb"
        self.should_save_sensor_data = self.agent_settings.save_sensor_data

        self.time_counter = 0

        self.transform_history: List[Transform] = []

        self.init_cam()

    def init_cam(self) -> None:
        """
        Initialize the cameras by calculating the camera intrinsics and
        ensuring that the output folder path exists

        Returns:
            None
        """

        if self.front_rgb_camera is not None:
            self.front_rgb_camera.intrinsics_matrix = (
                self.front_rgb_camera.calculate_intrinsic_matrix()
            )
        if self.front_depth_camera is not None:
            self.front_depth_camera.intrinsics_matrix = (
                self.front_depth_camera.calculate_intrinsic_matrix()
            )
        if self.rear_rgb_camera is not None:
            self.rear_rgb_camera.intrinsics_matrix = (
                self.rear_rgb_camera.calculate_intrinsic_matrix()
            )

        if self.should_save_sensor_data:
            self.front_depth_camera_output_folder_path.mkdir(parents=True,
                                                             exist_ok=True)
            self.front_rgb_camera_output_folder_path.mkdir(parents=True,
                                                           exist_ok=True)
            self.rear_rgb_camera_output_folder_path.mkdir(parents=True,
                                                          exist_ok=True)

    @abstractmethod
    def run_step(self, sensors_data: SensorsData,
                 vehicle: Vehicle) -> VehicleControl:
        """
        Receive Sensor Data and vehicle state information on every step and
        return a control

        Args:
            sensors_data: sensor data on this frame
            vehicle: vehicle state on this frame

        Returns:
            Vehicle Control

        """
        self.time_counter += 1
        self.sync_data(sensors_data=sensors_data, vehicle=vehicle)
        if self.should_save_sensor_data:
            self.save_sensor_data()
        return VehicleControl()

    def sync_data(self, sensors_data: SensorsData, vehicle: Vehicle) -> None:
        """
        Sync agent's state by updating Sensor Data and vehicle information

        Args:
            sensors_data: the new frame's sensor data
            vehicle: the new frame's vehicle state

        Returns:
            None
        """

        self.vehicle = vehicle

        if self.front_rgb_camera is not None:
            self.front_rgb_camera.data = (
                sensors_data.front_rgb.data
                if sensors_data.front_rgb is not None
                else None
            )

        if self.front_depth_camera is not None:
            self.front_depth_camera.data = (
                sensors_data.front_depth.data
                if sensors_data.front_depth is not None
                else None
            )

        if self.rear_rgb_camera is not None:
            self.rear_rgb_camera.data = (
                sensors_data.rear_rgb.data
                if sensors_data.rear_rgb is not None
                else None
            )

        if self.imu is not None:
            self.imu = sensors_data.imu_data

    def save_sensor_data(self) -> None:
        """
        Failure-safe saving function that saves all the sensor data of the
        current frame

        Returns:
            None
        """
        try:
            cv2.imwrite((self.front_rgb_camera_output_folder_path /
                         f"frame_{self.time_counter}.png").as_posix(),
                        self.front_rgb_camera.data)

            np.save((self.front_depth_camera_output_folder_path /
                     f"frame_{self.time_counter}").as_posix(),
                    self.front_depth_camera.data)

            cv2.imwrite((self.rear_rgb_camera_output_folder_path /
                         f"frame_{self.time_counter}.png").as_posix(),
                        self.rear_rgb_camera.data)
        except Exception as e:
            self.logger.error(
                f"Failed to save at Frame {self.time_counter}. Error: {e}")
