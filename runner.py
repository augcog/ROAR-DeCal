import logging
from ROAR_simulation.roar_autonomous_system.agent_module.pid_agent import PIDAgent
from pathlib import Path

import numpy as np
import os
import warnings
from ROAR_simulation.carla_client.carla_roar_config import Configuration
from ROAR_simulation.carla_client.carla_runner import CarlaRunner


def main():
    config = Configuration.parse_file(
        Path(os.getcwd()) / "configurations" / "config.json"
    )

    carla_runner = CarlaRunner(carla_settings=config.carla_config,
                               agent_settings=config.agent_config)
    try:
        my_vehicle = carla_runner.set_carla_world()
        # agent = PurePursuitAgent(vehicle=my_vehicle, agent_settings=config.agent_config)
        agent = PIDAgent(vehicle=my_vehicle, agent_settings=config.agent_config)
        # agent = MPCAgent(vehicle=my_vehicle, agent_settings=config.agent_config)
        carla_runner.start_game_loop(agent=agent, use_manual_control=False)
    except Exception as e:
        carla_runner.on_finish()
        logging.error(f"{e}. Might be a good idea to restart Server")


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(name)s '
                               '- %(levelname)s - %(message)s',
                        level=logging.DEBUG)
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    warnings.simplefilter("ignore")
    np.set_printoptions(suppress=True)

    main()



