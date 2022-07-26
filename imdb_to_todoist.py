from src.imdb import ImdbPort
from src.configure import load_configuration
from src.todoist import TodoistPort


def main():
    # Set path
    config = load_configuration()
    imdb = ImdbPort(config.IMDB_API_KEY)
    todoist = TodoistPort(config.TODOIST_API_KEY, config.default_project_id)
    movie = imdb.get_movie(input("Enter the movie title / id / url: "))
    todoist.make_task(movie)


if __name__ == "__main__":
    main()