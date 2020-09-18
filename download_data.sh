mkdir -p data

filename="easy_map_waypoints.txt"
fileid="15X1i1qd3E0k0LLsypoRiFCgDA3HNUw3y"
curl -L -o data/${filename} "https://drive.google.com/uc?export=download&id=${fileid}"
