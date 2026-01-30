import pytest
import os
import allure
import requests

from api.KinipoiskAPI import KinopoiskAPI
from dotenv import load_dotenv
load_dotenv()

base_url = 'https://api.kinopoisk.dev/v1.4'
token = os.getenv('Kinopoisk_token')

api = KinopoiskAPI(base_url, token)

def test_searching_film_by_name():
    resp = api.search_movie('Бригада')

    assert resp.status_code == 200

    resp_data = resp.json()
    assert "docs" in resp_data
    assert len(resp_data["docs"]) > 0

    first_film = resp_data["docs"][0]
    assert first_film["name"] == 'Бригада'

def test_searching_film_idustry_worker():
    resp = api.search_worker('Сергей Безруков')

    assert resp.status_code == 200

    resp_data = resp.json()
    assert "docs" in resp_data
    assert len(resp_data["docs"]) > 0

    first_person = resp_data["docs"][0]
    assert first_person["name"] == 'Сергей Безруков'

def test_searching_film_collections():
    category_list = {
        '0': 'Фильмы',
        '1': 'Онлайн-кинотеатр',
        '2': 'Премии',
        '3': 'Сборы',
        '4': 'Сериалы'
    }
    resp = api.searching_collections(category_list['0'])
    assert resp.status_code == 200

    resp_data = resp.json()
    assert "docs" in resp_data
    assert len(resp_data["docs"]) > 0

    first_coll = resp_data["docs"][0]
    assert first_coll["category"] == category_list['0']

def test_searching_collections_without_parameters():
    resp = api.emty_searching_collections('')
    assert resp.status_code == 400

    resp_data = resp.json()
    assert resp_data["error"] == "Bad Request"

def test_searching_film_without_name():
    pass

def test_searching_an_actor_without_name():
    pass

def test_searching_an_actor_with_defunct_name():
    pass