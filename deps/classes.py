
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