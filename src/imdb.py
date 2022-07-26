from dataclasses import dataclass
from typing import Any
from src.imdb_api import get_movie_from_id, get_search_movie


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


@dataclass
class Movie():
    title: str
    plot: str
    link: str


class ImdbPort():
    def __init__(self, IMDB_API_KEY: str) -> None:
        self.api_key = IMDB_API_KEY

    def search_movie_by_title(self, title: str) -> str:
        response = get_search_movie(title, self.api_key)
        if not response:
            print(f"Couldn't find movie with title: {title}")
            exit()
        results = response["results"]

        for i, result in enumerate(results):
            print(
                f"{i + 1}. {result['title']} - {result['description']} - {generate_link(result['id'])}"
            )
        index = int(input("Select result by typing leading number: ")) - 1
        return results[index]['id']

    def get_media(self, s: str) -> Movie:
        """
        Accepts a move id, URL or movie title as argument.
        Returns a dictionary containing information about the movie.
        """
        if is_movie_id(s):    # given id
            movie_id = s
        elif is_url(s):    # given url
            movie_id = get_id_from_url(s)
        else:    # given title
            movie_id = self.search_movie_by_title(s)
        movie_dict = get_movie_from_id(movie_id, self.api_key)
        movie = Movie(
            title=movie_dict['fullTitle'],
            plot=movie_dict['plot'],
            link=generate_link(movie_id),
        )
        return movie