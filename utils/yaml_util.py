import yaml
from pathlib import Path

def load_yaml(file_path):
    with open(file_path, encoding="utf-8") as f:
        return yaml.safe_load(f)
    
def get_project_root():
    return Path(__file__).resolve().parent.parent