from ROAR_simulation.roar_autonomous_system.planning_module.mission_planner.mission_planner import (
    MissionPlanner,
)
from pathlib import Path
import logging
from typing import List, Optional
from ROAR_simulation.roar_autonomous_system.utilities_module.data_structures_models import (
    Transform,
    Location,
    Rotation,
)
from ROAR_simulation.roar_autonomous_system.utilities_module.vehicle_models import (
    Vehicle,
)
from collections import deque


class WaypointFollowingMissionPlanner(MissionPlanner):
    """
    A mission planner that takes in a file that contains x,y,z coordinates, formulate into carla.Transform
    """

    def run_step(self, vehicle: Vehicle) -> deque:
        """
        Regenerate waypoints from file
        Find the waypoint that is closest to the current vehicle location.
        return a mission plan starting from that waypoint

        Args:
            vehicle: current state of the vehicle

        Returns:
            mission plan that start from the current vehicle location
        """
        super(WaypointFollowingMissionPlanner, self).run_step(vehicle=vehicle)
        self.logger.debug("TO BE IMPLEMENTED")
        return self.produce_mission_plan()

    def __init__(self, vehicle: Vehicle, file_path: Path):
        super().__init__(vehicle=vehicle)
        self.logger = logging.getLogger(__name__)
        self.file_path = file_path
        self.mission_plan = self.produce_mission_plan()
        self.logger.debug("Path Following Mission Planner Initiated.")

    def produce_mission_plan(self) -> deque:
        """
        Generates a list of waypoints based on the input file path
        :return a list of waypoint
        """
        mission_plan = deque()
        raw_path: List[List[float]] = self._read_data_file()
        for coord in raw_path:
            if len(coord) == 3 or len(coord) == 6:
                mission_plan.append(self._raw_coord_to_transform(coord))
        self.logger.debug(f"Computed Mission path of length {len(mission_plan)}")
        return mission_plan

    def _read_data_file(self) -> List[List[float]]:
        """
        Read data file and generate a list of (x, y, z) where each of x, y, z is of type float
        Returns:
            List of waypoints informat of [x, y, z]
        """
        result = []
        with open(self.file_path.as_posix(), "r") as f:
            for line in f:
                result.append(self._read_line(line=line))
        return result

    def _raw_coord_to_transform(self, raw: List[float]) -> Optional[Transform]:
        """
        transform coordinate to Transform instance

        Args:
            raw: coordinate in form of [x, y, z, pitch, yaw, roll]

        Returns:
            Transform instance
        """
        if len(raw) == 3:
            return Transform(
                location=Location(x=raw[0], y=raw[1], z=raw[2]),
                rotation=Rotation(pitch=0, yaw=0, roll=0),
            )
        elif len(raw) == 6:
            return Transform(
                location=Location(x=raw[0], y=raw[1], z=raw[2]),
                rotation=Rotation(pitch=raw[4], yaw=raw[5], roll=raw[6]),
            )
        else:
            self.logger.error(f"Point {raw} is invalid, skipping")
            return None

    def _read_line(self, line: str) -> List[float]:
        """
        parse a line of string of "x,y,z" into [x,y,z]
        Args:
            line: comma delimetered line

        Returns:
            [x, y, z]
        """
        x, y, z = line.split(",")
        x, y, z = float(x), float(y), float(z)
        return [x, y, z]
