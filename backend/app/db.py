import json, os
BASE = os.path.dirname(__file__)
def _read(path, default):
    try:
        with open(os.path.join(BASE, path), "r", encoding="utf-8") as f: return json.load(f)
    except Exception: return default
VENDORS = _read("seed/vendors.json", {})
PROJECTS = {p["id"]: p for p in _read("seed/projects.json", [])}
