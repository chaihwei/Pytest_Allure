import requests
from utils.yaml_util import load_yaml, get_project_root
import os

class ApiClient:
    def __init__(self):
        config = load_yaml(os.path.join(get_project_root(), "config", "config.yaml"))
        self.base_url = config["base_url"]
        self.session = requests.Session()
        self.token = None

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.base_url}{endpoint}"
        resp = self.session.post(url, json=data, headers=headers)
        return resp
    
    def get(self, endpoint, headers=None):
        url = f"{self.base_url}{endpoint}"
        resp = self.session.get(url, headers=headers)
        return resp