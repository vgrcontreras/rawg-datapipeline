import os
from http import HTTPStatus

from dotenv import load_dotenv

from rawg_datapipeline.etl.main import extract

load_dotenv

API_KEY = os.getenv('API_KEY')


def test_getrequest_validation():
    endpoint = '/api/games'

    response = extract(endpoint=endpoint, api_key=API_KEY)

    assert response.status_code == HTTPStatus.OK
