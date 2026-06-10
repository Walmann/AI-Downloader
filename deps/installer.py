import model_installer
import node_installer

import os
import sys


# This module is to start the installation of models and nodes. 

class model_info:
    def __init__(self, model_url: str, model_dir: str):
        self.url = model_url
        self.dir = model_dir

class node_info:
    def __init__(self, dir, url):
        self.dir = dir
        self.url = url
        pass

class install_job:
    def __init__(self, models: list[model_info], nodes: list[node_info]):
        self.models = models
        self.nodes = nodes

def install(jobs: install_job):
    # Change dir to ComfyUI
    os.chdir("/workspace/ComfyUI/")


    if sys.prefix == sys.base_prefix:
        print("Script is not running inside virtual enviorment.")
        exit()
    
    # Install nodes and models
    node_installer.install_node(jobs.nodes)
    model_installer.download(jobs.models)

    pass