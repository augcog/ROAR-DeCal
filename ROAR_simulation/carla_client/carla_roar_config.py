from pydantic import BaseModel, Field
from ROAR_simulation.roar_autonomous_system.utilities_module.agent_config import AgentConfig
from ROAR_simulation.carla_client.carla_config import CarlaConfig


class Configuration(BaseModel):
    agent_config: AgentConfig = Field(default=AgentConfig())
    carla_config: CarlaConfig = Field(default=CarlaConfig())
