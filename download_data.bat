mkdir -p data

filename="easy_map_waypoints.txt"
fileid="1QSOqGHWx2DtRvwl0kFwxQYidLVAZUZA7"
curl -L  ${filename} "https://drive.google.com/uc?export=download&id=${fileid}" > data/${filename}