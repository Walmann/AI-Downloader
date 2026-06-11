import os
from git import Repo
import sys
import subprocess
import pathlib


from deps.classes import node_info, Settings

def install_nodes(settings: Settings, nodes: list[node_info]):
    # nodes_root = "/workspace/runpod-slim/ComfyUI/custom_nodes/"

    for node in nodes:
        node_dir = settings.loc_custom_nodes / node.dir
        print(f"Node Dir: {node_dir}")
        
        # Get the node with Git
        os.chdir(settings.loc_custom_nodes)
        if pathlib.Path(node_dir).is_dir():
            print(f"{node.dir} already exists. Updating.")
            # Repo(node_dir).remotes.origin.pull()
        else: 
            print(f"{node.dir} does not exists. Downloading now.")
            Repo.clone_from(url=node.url, to_path=node_dir)

        os.chdir(node_dir)
        


        print(f"Installing requirements for {node.dir}")
        pip_exe = os.path.join(settings.loc_venv, "Scripts", "pip.exe")
        try:
            subprocess.run([
                pip_exe,
                "install",
                "-r",
                "requirements.txt"
            ], check=True)


            print("Packages installed successfully.")
        except subprocess.CalledProcessError as e:
            print("Error installing packages:", e)


    pass