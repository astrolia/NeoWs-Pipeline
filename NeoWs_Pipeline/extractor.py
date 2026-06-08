import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

def load_data(API_KEY, date):
    print("Loading data...")

    #url from NeoWs api
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={date}&end_date={date}&api_key={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error loading data: {response.status_code}")