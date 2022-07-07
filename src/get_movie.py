from typing import Any
import requests
from config import API_KEY


def is_movie_id(s: str) -> bool:
    """
    Returns true if the given string s is an IMDB id
    Every id starts with tt as per IMDB API documentation
    """
    return s[:2] == "tt"


def is_url(s: str) -> bool:
    """
    Returns true if given string s is an URL.
    """
    return bool(s.find("imdb.com") != -1)


def get_id_from_url(s: str) -> str:
    """
    Extracts id from URL.
    """
    return s.strip("/").split("/")[-1]


def generate_link(id: str) -> str:
    return f"https://www.imdb.com/title/{id}"


def get_search_movie(title: str) -> Any:
    response = requests.get(f"https://imdb-api.com/en/API/SearchMovie/{API_KEY}/{title}")
    return response.json()


def get_movie_from_id(id: str) -> Any:
    return requests.get(f"https://imdb-api.com/en/API/Title/{API_KEY}/{id}").json()


def search_movie_by_title(title: str) -> str:
    response = get_search_movie(title)
    results = response["results"]

    for i, result in enumerate(results):
        print(
            f"{i + 1}. {result['title']} - {result['description']} - {generate_link(result['id'])}"
        )
    index = int(input("Select result by typing leading number: ")) - 1
    return results[index]['id']


def get_movie(s: str):
    if is_movie_id(s):    # given id
        movie_id = s
    elif is_url(s):    # given url
        movie_id = get_id_from_url(s)
    else:    # given title
        movie_id = search_movie_by_title(s)
    movie = get_movie_from_id(movie_id)
    print(movie)


if __name__ == "__main__":
    # search_movie("Fantastic Mr. Fox")
    get_movie("harry potter")