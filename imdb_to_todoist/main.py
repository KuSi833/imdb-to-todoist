from imdb_to_todoist.imdb import ImdbPort
from configure import load_configuration
from imdb_to_todoist.todoist import TodoistPort

if __name__ == "__main__":
    # Set path
    config = load_configuration()
    imdb = ImdbPort(config.IMDB_API_KEY)
    todoist = TodoistPort(config.TODOIST_API_KEY, config.default_project_id)
    movie = imdb.get_movie(input("Enter the movie title / id / url: "))
    todoist.make_task(movie)