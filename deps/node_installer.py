import os
from git import Repo
import sys


from deps.classes import node_info

def install_nodes(nodes: list[node_info]):
    nodes_root = "/workspace/runpod-slim/ComfyUI/custom_nodes/"

    for node in nodes:
        node_dir = nodes_root + node.dir
        print(f"Node Dir: {node_dir}")
        
        
        os.chdir = nodes_root
        Repo.clone_from(url=node.url, to_path=node.dir)

        os.chdir(node_dir)
        
        print(f"Installing requirements for {node.dir}")
        sys.executable("pip", "install", "-r", "requirements.txt")


    pass