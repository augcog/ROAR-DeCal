
**Platforms Tested:** Ubuntu 18.04, Windows 10, MacOS Catalina
    
**Approximate Time:** ~10 minutes    

#### Windows
1. Clone the repo
    - `git clone https://github.com/augcog/ROAR-DeCal.git && cd ROAR-Decal`
2. Download Carla Server package
    - [https://drive.google.com/drive/folders/1FlkNCNENaC3qrTub7mqra7EH7iSbRNiI](https://drive.google.com/drive/folders/1FlkNCNENaC3qrTub7mqra7EH7iSbRNiI)
    - put it OUTSIDE of the `ROAR-DeCal` folder, doesn't matter where
3. Download data
    - `./download_data.bat`
4. Check your file directory, it should be:
    - `ROAR-Sim`
        - `data`
            - `easy_map_waypoints.txt`
            - `... other data files`
        - `ROAR_simulation`
        - `runner.py`
        - ... other files and folders
5. Create virtual environment and install dependencies
    - `conda create -n ROAR python=3.7`
    - `conda activate ROAR`
    - `pip install -r requirements.txt`
6. Enjoy
    - `.CarlaUE4.exe` file in the Carla Server package to launch the server
    - `python runner.py`
        
#### Linux
1. Clone the repo
    - `git clone https://github.com/augcog/ROAR-DeCal.git && cd ROAR-Decal`
2. Download Carla Server package
    - [https://drive.google.com/drive/folders/1FlkNCNENaC3qrTub7mqra7EH7iSbRNiI](https://drive.google.com/drive/folders/1FlkNCNENaC3qrTub7mqra7EH7iSbRNiI)
    - put it OUTSIDE of the `ROAR-Sim` folder, doesn't matter where
3. Download data
    - `./download_data.sh`
4. Check your file directory, it should be:
    - `ROAR-Sim`
        - `data`
            - `easy_map_waypoints.txt`
            - `... other data files`
        - `ROAR_simulation`
        - `runner.py`
        - ... other files and folders
5. Create virtual environment and install dependencies
    - `conda create -n ROAR python=3.7`
    - `conda activate ROAR`
    - `pip install -r requirements.txt`
6. Enjoy
    - `./CarlaUE4.sh` file in the Carla Server package to launch the server
    - `python runner.py`
    
    
#### Mac
@Sunny, please fill in here

### Common Errors
1. Conda not found 
    - You should download miniconda3 Linux/Windows 64-bit [miniconda3](https://docs.conda.io/en/latest/miniconda.html)
    - Follow the below instructions to install miniconda successfully 
    ![](../images/miniconda3.png)
    - If still cannot call conda, try (directory may vary):
        - `sudo chown -R /home/username/miniconda3/'`
        - `sudo chmod -R +x /home/username/miniconda3/`
