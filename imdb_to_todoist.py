import argparse

from src.imdb import ImdbPort
from src.configure import load_configuration
from src.todoist import TodoistPort


def add_task(args):
    config = load_configuration()
    config.check_if_complete()
    imdb = ImdbPort(config.IMDB_API_KEY)
    todoist = TodoistPort(config.TODOIST_API_KEY, config.default_project_id)
    movie = imdb.get_movie(args.movie)
    todoist.make_task(movie, labels=args.labels)


def configure(args):
    print("CONFIG")
    print(args)


def main():
    parser = argparse.ArgumentParser(
        description="Takes a movie from IMDB and assigns it as a Todoist task")
    subparsers = parser.add_subparsers()
    # Add task parser
    add_task_parser = subparsers.add_parser("add")
    add_task_parser.add_argument("movie", help="movie title / id / url", type=str)
    add_task_parser.add_argument("-p",
                                 "--project",
                                 help="override default project name",
                                 type=str)
    add_task_parser.add_argument("-l",
                                 "--labels",
                                 help="override default labels",
                                 type=str,
                                 nargs="*")
    add_task_parser.set_defaults(func=add_task)

    # Config parser
    config_parser = subparsers.add_parser("config")
    config_parser.add_argument("-i", "--imdb", help="Assign IMDB Api Key", type=str)
    config_parser.add_argument("-t", "--todoist", help="Assign Todoist Api Key", type=str)
    config_parser.add_argument("-p",
                               "--project",
                               help="Assign default project name",
                               type=str)
    config_parser.add_argument("-l",
                               "--label",
                               help="Assign default label name",
                               type=str)
    config_parser.set_defaults(func=configure)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()