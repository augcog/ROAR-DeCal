## Agent
This configuration is for Agent.

Here's a selection of them that might come handy:
```
# location of the default waypoint file
"waypoint_file_path": "./data/easy_map_waypoints.txt",

# location of the output data folder, the program will automatcially write into that folder only
# if the folder does not exist, it will be created automatically
"output_data_folder_path": "./data/output/",

# enable autopilot loop on every world click.
# If you want the vehicle to move per autopilot instruction, set use_manual_control=False in runner
"enable_autopilot": true,

# spawn point for this agent
"spawn_point_id": 1,

# true to save sensor data to output_data_folder
"save_sensor_data": false
```

## Carla
This will set the configuration between Carla Client and Carla Server, and how the Carla World spawns.

Here's some useful ones that might come handy:

```
# true to print keyboard control hints
"print_keyboard_hint": false,

# true to not render graphics. You may turn save_sensor_data on to record each frame and do a play back later
"no_rendering_mode": false,

# True to enable syncrhonous mode with the server
"synchronous_mode": false,

# If the simulation is running slow for you, change this variable to some bigger number
"fixed_delta_seconds": 0.05,

# NPC configuration file location
"npc_config_file_path": "./configurations/npc_config.json",

# true to spawn npc
"should_spawn_npcs": false
```

## NPC
Please note that current NPC only implement simple PurePursuit control to follow waypoints.

Please note that NPC is a simpler version of an Agent. 

You may spawn multiple NPCs by putting them in a list. Please see example in `configurations/npc_config.json`
```
# name of the npc
"name": "npc_0",

# the waypoint that this npc is going to follow
"waypoint_file_path": "./data/easy_map_waypoints.txt",

# true to enable autopilot of the npc
"enable_autopilot": true,

# spawn location of the npc. Note that if two agents have the same spawn location, 
# the one that spanwed first will be prreserved
"spawn_point_id": 0,

# target speed in which this NPC is going to go at
"target_speed": 50
```