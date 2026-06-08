import pandas as pd
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

import extractor
import transformer
import loader

if __name__ == "__main__":

    load_dotenv()
    API_KEY = os.getenv("NASA_API_KEY")
    date = datetime.today().strftime('%Y-%m-%d')
    file_name = f"asteroids/near_asteroids_{date}.csv"

    try:

        raw_data = extractor.load_data(API_KEY, date)
        trans_data = transformer.transform_data(raw_data, date)
        loader.load_csv_file(trans_data, file_name)

    except Exception as e:
        print(e)
