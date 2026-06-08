import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

def load_csv_file(asteroid_data, file_name):
    print("Transfering to file")

    try:
        asteroid_data.to_csv(file_name, index=False)
        print(f"Data saved in {file_name}")
    except Exception as e:
        print(e);
        