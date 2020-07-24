import numpy as np
from pydantic import BaseModel, Field
from typing import Union, List, Tuple
from ROAR_simulation.roar_autonomous_system.utilities_module \
    .data_structures_models import (
    Transform,
    Location,
)
import cv2
import logging
import math
from typing import Optional, List


class OccupancyGridMap:
    """
    A 2D Occupancy Grid Map representing the world

    Should be able to handle
        1. Transformation of coordinate from world to grid cord
        2. Transformation of cord from grid cord to world cord
        3. Represent the vehicle size and position, vehicle is represented as 0
            Note that this class does NOT remember the vehicle position,
            in order to visualize vehicle, vehicle position has to be passed in
        4. Represent the obstacles' position once its world coordinate is
           given
        5. Represent free space's position, once its world coordinate is given
        6. visualize itself, including zoom to a certain area so that not
           the entire map is visualized
        7. The range of values should be bewteen 0 - 1
            - 0 = obstacles, 1 = free space
        8 Failure tolerant, if I pass in a wrong world coordinate,
          it will prompt it, but do not fail. Similar with other functions
          in this class
    """

    def __init__(self, min_x: int, min_y: int, max_x: int, max_y: int,
                 map_padding: int = 40, vehicle_width=5, vehicle_height=5):
        """

        Args:
            min_x: minimum x in world cord
            min_y: minimum y in world cord
            max_x: maximum x in world cord
            max_y: maximum y in world cord
            map_padding: additional padding intended to add.
        Note: This method pad to both sides, for example, it create padding
        to the left of min_x, and to the right of max_x
        Note: map_padding is for when when visualizing, we have to take a whole
         block and just in case the route is to the edge of the map,
         it will not error out
        """
        self.logger = logging.getLogger(__name__)
        self.map: Optional[np.ndarray] = None

        self._min_x = math.floor(min_x)
        self._min_y = math.floor(min_y)

        self._max_x = math.ceil(max_x)
        self._max_y = math.ceil(max_y)

        self._map_additiona_padding = map_padding

        self.vehicle_width = vehicle_width
        self.vehicle_height = vehicle_height

        self._initialize_map()

    def _initialize_map(self):
        x_total = self._max_x - self._min_x + 2 * self._map_additiona_padding
        y_total = self._max_y - self._min_y + 2 * self._map_additiona_padding
        self.map = np.zeros([x_total, y_total])
        self.logger.debug(f"Occupancy Grid Map of size {x_total} x {y_total} "
                          f"initialized")

    def location_to_occu_cord(self, location: Location):
        return self.cord_translation_from_world(world_cords_xy=
                                                np.array([[location.x,
                                                           location.y]]))

    def cord_translation_from_world(self,
                                    world_cords_xy: np.ndarray) -> np.ndarray:
        """
        Translate from world coordinate to occupancy coordinate

        If the given world coord is less than min or greater than maximum,
        then do not execute the translation, log error message

        Args:
            world_cords_xy: Numpy array of shape (N, 2) representing
             [[x, y], [x, y], ...]

        Returns:
            occupancy grid map coordinate for this world coordinate of shape
            (N, 2)
            [
             [x, y],
             [a, b]
            ]

        """
        # reshape input into a ndarray that looks like [[X, Y], [X, Y]...]
        # self.logger.debug(f"translating world cords xy: {np.shape(world_cords_xy)}")
        transformed = np.round(world_cords_xy - [self._min_x, self._min_y]).astype(np.int64)
        # self.logger.debug(f"Transformed: {np.shape(transformed)}")
        return transformed

    def update_grid_map(self, world_cords_xy):
        """
        Updates the grid map based on the world coordinates passed in
        Args:
            world_cords_xy: Numpy array of shape (N, 2) representing
             [[x, y], [x, y], ...]

        Returns:

        """
        # find occupancy map cords
        # self.logger.debug(f"Updating Grid Map: {np.shape(world_cords_xy)}")
        occu_cords = self.cord_translation_from_world(
            world_cords_xy=world_cords_xy)
        # self.logger.debug(f"Occupancy Grid Map Cord shape = {np.shape(occu_cords)}")
        self.map[occu_cords[:, 0], occu_cords[:, 1]] = 1

    def visualize(self,
                  vehicle_location: Optional[Location] = None,
                  view_width: int = 20):
        if vehicle_location is None:
            cv2.imshow("Occupancy Grid Map", self.map)
        else:
            occu_cord = self.location_to_occu_cord(
                location=vehicle_location)
            map_copy = self.map.copy()
            x, y = occu_cord[0]
            map_copy[x - self.vehicle_width // 2:x + self.vehicle_width // 2,
                     y - self.vehicle_height // 2: y + self.vehicle_height // 2] = 0
            cv2.imshow("Occupancy Grid Map", map_copy)
        cv2.waitKey(1)
