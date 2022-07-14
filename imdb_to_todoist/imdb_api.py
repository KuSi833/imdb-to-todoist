import requests
from typing import Any


def get_top_250_movies(IMDB_API_KEY: str):
    return requests.get(f"https://imdb-api.com/en/API/Top250TVs/{IMDB_API_KEY}").json()


def is_valid_api_key(IMDB_API_KEY: str) -> bool:
    "Checks if the given API KEY is valid."
    response = get_top_250_movies(IMDB_API_KEY)
    return not response['errorMessage']


def get_search_movie(title: str, IMDB_API_KEY: str) -> Any:
    return requests.get(
        f"https://imdb-api.com/en/API/SearchMovie/{IMDB_API_KEY}/{title}").json()


def get_movie_from_id(id: str, IMDB_API_KEY: str) -> Any:
    return requests.get(f"https://imdb-api.com/en/API/Title/{IMDB_API_KEY}/{id}").json()