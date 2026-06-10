from deps.model_installer import download_models
from deps.node_installer import install_nodes
from deps.classes import install_job

import os
import sys


# This module is to start the installation of models and nodes. 


def install_models(jobs: install_job):
    # Change dir to ComfyUI
    # ComfyInstallLocations = ["/workspace/ComfyUI/", "/workspace/runpod-slim/ComfyUI/"]
    os.chdir("../ComfyUI")


    if sys.prefix == sys.base_prefix:
        print("Script is not running inside virtual enviorment.")
        exit()

    # Install nodes and models
    install_nodes(jobs.nodes)
    download_models(jobs.models)

    pass