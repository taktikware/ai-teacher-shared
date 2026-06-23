import os
import yaml

_MAP_DIR = os.path.join(os.path.dirname(__file__), "map")


def _load_map(filename: str) -> dict:
    path = os.path.join(_MAP_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_timit_to_mfa_map() -> dict:
    return _load_map("timit_mfa_mapping.yaml")


def get_mfa_to_timit_map() -> dict:
    return _load_map("mfa_timit_mapping.yaml")
