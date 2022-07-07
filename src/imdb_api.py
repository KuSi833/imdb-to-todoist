import requests
from typing import Any
from config import API_KEY


def get_search_movie(title: str) -> Any:
    return requests.get(
        f"https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{title}").json()


def get_movie_from_id(id: str) -> Any:
    return requests.get(f"https://imdb-api.com/en/API/Title/{API_KEY}/{id}").json()