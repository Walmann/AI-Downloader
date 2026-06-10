import os
from git import Repo
import sys


from installer import node_info

def install_nodes(nodes: list[node_info]):
    nodes_root = "/workspace/ComfyUI/custom_nodes/"

    for node in nodes:
        Repo.clone_from(url=node.url, to_path=node.url)

        os.chdir(nodes_root + node.dir)
        
        print(f"Installing requirements for {node.dir}")
        sys.executable("pip", "install", "-r", "requirements.txt")


    pass