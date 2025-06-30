import requests
import pandas as pd
import os
from datetime import datetime

APP_KEY = "045e9ab8f6164cb8bc07cd27bcff2109"
roads = ["A2", "A406", "A13"]
url = f"https://api.tfl.gov.uk/Road/{','.join(roads)}"

params = {
    "app_key": APP_KEY
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame([{
        "road": road["displayName"],
        "status": road["statusSeverity"],
        "description": road["statusSeverityDescription"],
        "timestamp": datetime.now().isoformat()
    } for road in data])

    # Building absolute path to data folder outside scripts/.
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))
    data_dir = os.path.join(project_root, "data")
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, "tfl_road_status.csv")

    # Save to CSV
    df.to_csv(file_path, index=False, mode='a', header=not os.path.exists(file_path))

    print("Data saved to:", file_path)
else:
    print("Error:", response.status_code)
    print(response.text)
