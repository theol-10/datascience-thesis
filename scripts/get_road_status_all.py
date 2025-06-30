import requests
import pandas as pd
import json
import os
from datetime import datetime

APP_KEY = "045e9ab8f6164cb8bc07cd27bcff2109"

# Loading road list
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_dir = os.path.join(project_root, "data")
with open(os.path.join(data_dir, "available_roads.json")) as f:
    roads = json.load(f)

# there may have too many roads for one request so splitting into chunks
def chunk(lst, size):
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

records = []
for road_chunk in chunk(roads, 30):  # 30 at a time first testing
    url = f"https://api.tfl.gov.uk/Road/{','.join(road_chunk)}"
    params = {"app_key": APP_KEY}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        timestamp = datetime.now().isoformat()
        for road in data:
            records.append({
                "road": road["displayName"],
                "status": road["statusSeverity"],
                "description": road["statusSeverityDescription"],
                "timestamp": timestamp
            })
    else:
        print("Error for chunk:", response.status_code)
        print(response.text)

# Saving results
df = pd.DataFrame(records)
os.makedirs(data_dir, exist_ok=True)
file_path = os.path.join(data_dir, "tfl_road_status.csv")
df.to_csv(file_path, index=False, mode='a', header=not os.path.exists(file_path))

print(f"Saved {len(df)} records to {file_path}")
