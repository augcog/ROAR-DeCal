from pydantic import BaseModel, Field
from typing import Union
import math
from ROAR_simulation.roar_autonomous_system.utilities_module.data_structures_models import (
    Transform,
    Vector3D,
)


class VehicleControl(BaseModel):
    throttle: float = Field(default=0)
    steering: float = Field(default=0)

    @staticmethod
    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)

    def get_throttle(self) -> float:
        """
        Cap it between -1  and 1
        :return:
        """
        return self.clamp(self.throttle, -1, 1)

    def get_steering(self) -> float:
        return self.clamp(self.steering, -1, 1)


class Vehicle(BaseModel):
    """
    Encodes the Vehicle's state at the last tick
    """

    velocity: Vector3D
    transform: Union[Transform, None] = Field(default=None)
    control: VehicleControl  # ?
    wheel_base: float = Field(
        default=2.875,
        title="Wheel Base length of the vehilce in meters",
        description="Default to tesla model 3's wheel base",
    )

    @staticmethod
    def get_speed(vehicle):
        """
        Compute speed of a vehicle in Km/h.

            :param vehicle: the vehicle for which speed is calculated
            :return: speed as a float in Km/h
        """
        vel = vehicle.velocity
        return 3.6 * math.sqrt(vel.x ** 2 + vel.y ** 2 + vel.z ** 2)
