import yaml

def load_config(path: str) -> dict:
    """
    Load YAML configuration from the given file path.
    """
    with open(path, "r") as f:
        return yaml.safe_load(f)

def get_pipeline(config: dict) -> list:
    """
    Extract the 'pipeline' list from the loaded config.
    """
    return config.get("pipeline", [])
