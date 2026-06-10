from deps import model_installer
from deps import node_installer
from deps.classes import install_job

import os
import sys


# This module is to start the installation of models and nodes. 


def install(jobs: install_job):
    # Change dir to ComfyUI
    ComfyInstallLocations = ["/workspace/ComfyUI/", "/workspace/runpod-slim/ComfyUI/"]
    os.chdir("../ComfyUI")


    if sys.prefix == sys.base_prefix:
        print("Script is not running inside virtual enviorment.")
        exit()

    # Install nodes and models
    node_installer.install_node(jobs.nodes)
    model_installer.download(jobs.models)

    pass