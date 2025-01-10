import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def extract(
    endpoint: str,
    base_url: str = 'https://api.rawg.io',
    api_key: str = API_KEY,
) -> dict:
    response = requests.get(url=base_url + endpoint, params={'key': api_key})

    return response


def extract_test(
    endpoint: str,
    base_url: str = 'https://api.rawg.io',
    api_key: str = API_KEY,
) -> dict:
    response = requests.get(url=base_url + endpoint, params={'key': api_key})

    data = response.json()['results'][0]

    return data


if __name__ == '__main__':
    data = extract(endpoint='/api/games')

    with open('rawg_games.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
