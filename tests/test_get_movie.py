from src.imdb import (get_id_from_url, is_url, is_movie_id, generate_link)


def test_generate_link():
    assert (generate_link("tt0295297") == "https://www.imdb.com/title/tt0295297")


def test_is_movie_id() -> None:
    assert (is_movie_id("tt0295297"))

    assert not (is_movie_id("harry potter"))
    assert not (is_movie_id("https://www.imdb.com/title/tt0295297/"))
    assert not (is_movie_id("https://www.imdb.com/title/tt0295297"))


def test_is_url() -> None:
    assert (is_url("https://www.imdb.com/title/tt0295297/"))
    assert (is_url("https://www.imdb.com/title/tt0295297"))
    assert (is_url("www.imdb.com/title/tt0295297/"))

    assert not (is_url("harry potter"))
    assert not (is_url("tt0295297"))


def test_get_id_from_url() -> None:
    assert (get_id_from_url("https://www.imdb.com/title/tt0295297/") == "tt0295297")
    assert (get_id_from_url("https://www.imdb.com/title/tt0295297") == "tt0295297")
    assert (get_id_from_url("www.imdb.com/title/tt0295297") == "tt0295297")
