# ROAR Carla Simlulation

### QuickStart


#### Windows:
1. Clone this repo
    - `git clone https://github.com/augcog/ROAR-Sim.git`
2. Download Carla Server package
    - [Windows](https://drive.google.com/file/d/1TguaqwO9rPxCcOZ4DacJ_YQ5EoY1NJwz/view?usp=sharing)
    - put it OUTSIDE of the `ROAR-DeCal` folder, doesn't matter where
3. Check your file directory, it should be:
    - `ROAR-DeCal`
        - `data`
            - `easy_map_waypoints.txt`
        - `ROAR_simulation`
        - `runner.py`
        - ... other files and folders
4. Create virtual environment and install dependencies
    - `conda create -n ROAR python=3.7`
    - `conda activate ROAR`
    - `pip install -r requirements.txt`
5. Enjoy
    - Double click the `CarlaUE4.exe` file in the Carla Server package to launch the server
    - `python runner.py`
        
#### Linux:
Same as Windows except

In Step 2, download this file instead: [Linux](https://drive.google.com/file/d/1wU2mk5htapTEtyhsK4THIf1hp-OzvuN3/view?usp=sharing)

In step 5, just type in `./CarlaUE4.sh` to start the server
    
