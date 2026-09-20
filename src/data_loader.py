import requests
import pandas as pd


def load_crime_data(limit=10000):

    url = "https://data.cityofchicago.org/resource/ijzp-q8t2.json"

    params = {
        "$limit": limit,
        "$order": "date DESC"
    }

    response = requests.get(url, params=params)

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)

    return df
