from deps.model_installer import download_models
from deps.node_installer import install_nodes
from deps.classes import install_job, Settings

import os
import sys
import pathlib

# This module is to start the installation of models and nodes. 


def install_models(jobs: install_job):
    # Create settings file
    settings = Settings(Folder_ComfyUI=pathlib.Path("../ComfyUI").resolve())
    
    # Change dir to ComfyUI
    # ComfyInstallLocations = ["/workspace/ComfyUI/", "/workspace/runpod-slim/ComfyUI/"]
    os.chdir(settings.loc_ComfyUI)


    if sys.prefix == sys.base_prefix:
        print("Script is not running inside virtual enviorment.")
        exit()

    # Install nodes and models
    install_nodes(settings = settings, nodes= jobs.nodes)
    download_models(settings = settings, models = jobs.models)

    pass