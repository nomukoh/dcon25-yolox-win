# bash run_docker_container_notrm.sh

#!/bin/bash
#docker --name mpgd run --rm --ipc=host --gpus all  -it -v "$(pwd):/workspace" mpgd
docker run --name yolox_s --ipc=host --gpus all  -it -v "$(pwd):/workspace" yolox_s