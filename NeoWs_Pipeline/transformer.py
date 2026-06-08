import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

def transform_data(raw_data, date):
    print("Start data transforming and cleaning...")

    #load data in the list
    asteroid_list = raw_data['near_earth_objects'][date]

    ready_data = []

    for asteroid in asteroid_list:
        info = {
            "id": asteroid["id"],
            "name": asteroid["name"],
            "absolute_magnitude": asteroid["absolute_magnitude_h"],
            "min_estimated_diameter_m": asteroid["estimated_diameter"]["meters"]["estimated_diameter_min"],
            "max_estimated_diameter_m": asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"],
            "is_potentially_hazardous_asteroid": asteroid["is_potentially_hazardous_asteroid"],
            "close_approach_data": asteroid["close_approach_data"][0]["close_approach_date_full"],
            "speed_km/h": float(asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]),
            "earth_distance_km": float(asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]),
        }

        ready_data = ready_data + [info]

    #convert dictionary into DataFrame
    df = pd.DataFrame(ready_data)
    return df