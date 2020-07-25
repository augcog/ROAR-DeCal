from pydantic import Field, BaseModel
from pathlib import Path
from typing import Optional
from ROAR_simulation.roar_autonomous_system.utilities_module.camera_models \
    import \
    Camera
from ROAR_simulation.roar_autonomous_system.utilities_module. \
    data_structures_models import Location, Rotation, Transform
import os


class AgentConfig(BaseModel):
    # ROAR sensors settings
    front_depth_cam: Camera = Field(default=Camera(fov=70,
                                                   transform=Transform(
                                                       location=Location(x=1.6,
                                                                         y=0,
                                                                         z=1.7
                                                                         ),
                                                       rotation=Rotation(
                                                           pitch=0,
                                                           yaw=0,
                                                           roll=0)),

                                                   image_size_x=800,
                                                   image_size_y=600),
                                    title="Front Depth Camera")
    front_rgb_cam: Camera = Field(default=Camera(fov=70,
                                                 transform=Transform(
                                                     location=Location(x=1.6,
                                                                       y=0,
                                                                       z=1.7),
                                                     rotation=Rotation(pitch=0,
                                                                       yaw=0,
                                                                       roll=0)
                                                 ),
                                                 image_size_x=800,
                                                 image_size_y=600),
                                  title="Front RGB Camera")
    rear_rgb_cam: Camera = Field(default=Camera(fov=145,
                                                transform=Transform(
                                                    location=Location(x=-1.5,
                                                                      y=0.0,
                                                                      z=1.4),
                                                    rotation=Rotation(
                                                        pitch=0.0, yaw=180,
                                                        roll=0.0)),

                                                image_size_x=800,
                                                image_size_y=600),
                                 title="Rear RGB Camera")
    # data path
    waypoint_file_path: str = Field(default=(Path(
        os.getcwd()) / "data" / "easy_map_waypoints.txt").as_posix())
    output_data_folder_path: str = Field(
        default=(Path(os.getcwd()) / "data" / "output"))

    # miscellaneous settings
    enable_autopilot: bool = Field(default=True, title="Enable Antopilot",
                                   description="Enable Antopilot")
    spawn_point_id: int = Field(default=1, title="Spaning Location ID",
                                description="Spanning Location ID")
    show_sensors_data: bool = Field(default=False)
    graph_post_modem_data: bool = Field(default=False)
    save_sensor_data: bool = Field(default=False)

