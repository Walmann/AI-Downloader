import os
from git import Repo
import sys


from deps.classes import node_info

def install_nodes(nodes: list[node_info]):
    nodes_root = "/workspace/ComfyUI/custom_nodes/"

    for node in nodes:
        Repo.clone_from(url=node.url, to_path=node.dir)

        node_dir = nodes_root + node.dir
        print(node_dir)
        os.chdir(node_dir)
        
        print(f"Installing requirements for {node.dir}")
        sys.executable("pip", "install", "-r", "requirements.txt")


    pass