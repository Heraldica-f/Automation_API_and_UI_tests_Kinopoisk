import requests
import os

class KinopoiskAPI:

    def __init__(self, base_url: str, token: str) -> None:
        self.base_url = base_url
        self.token = token

    def search_movie(self, title: str) -> requests.Response:
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params = {
            'page': 1,
            'limit': 10,
            'query': title
        }

        resp = requests.get(f"{self.base_url}/movie/search", headers=headers, params=params)
        return resp
    
    def search_worker(self, name: str) -> requests.Response:
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params = {
            'page': 1,
            'limit': 10,
            'query': name
        }

        resp = requests.get(f"{self.base_url}/person/search", headers=headers, params=params)
        return resp
    
    def searching_collections(self, category: str) -> requests.Response:
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params = {
            'page': 1,
            'limit': 10,
            'query': category
        }
        resp = requests.get(f"{self.base_url}/list", headers=headers, params=params)
        return resp
    
    def emty_searching_collections(self, category: str) -> requests.Response:
        headers = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params = {
            'page': None,
            'limit': None,
            'query': category
        }

        resp = requests.get(f"{self.base_url}/list", headers=headers, params=params)
        return resp