import requests
import json
import os

APP_KEY = "045e9ab8f6164cb8bc07cd27bcff2109"
url = "https://api.tfl.gov.uk/Road"
params = {"app_key": APP_KEY}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    road_ids = [road["id"] for road in data]

    # Saving to ../data/
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(project_root, "data")
    os.makedirs(data_dir, exist_ok=True)
    save_path = os.path.join(data_dir, "available_roads.json")

    with open(save_path, "w") as f:
        json.dump(road_ids, f)

    print(f"saved {len(road_ids)} road IDs to {save_path}")
else:
    print("failed to fetch road list:", response.status_code)
    print(response.text)
