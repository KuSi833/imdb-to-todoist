import argparse

from src.imdb import ImdbPort
from src import configuration
from src.todoist import TodoistPort
from src.exceptions import MissingAttributeException


def add_task(args):
    config = configuration.load_configuration()
    config.check_if_complete()

    project_name = None
    if args.project:
        project_name = args.project
    elif config.default_project_name:
        project_name = config.default_project_name
    else:
        raise MissingAttributeException(
            "Project Name",
            message="Project name must be passed as an argument or a default must be set.",
        )

    labels = None
    if args.labels:
        if args.labels == "-":
            labels = None
        else:
            labels = args.labels
    elif config.default_label_name:
        if config.default_label_name == "-":
            labels = None
        else:
            labels = config.default_label_name

    imdb = ImdbPort(config.IMDB_API_KEY)
    todoist = TodoistPort(config.TODOIST_API_KEY)
    for media_name in args.media:
        media = imdb.get_media(media_name)
        todoist.make_task(media, labels=labels, project_name=project_name)
        if labels:
            print(
                f"\nAdded {media.title} to project {project_name} with label(s): {' '.join(labels)}\n"
            )
        else:
            print(
                f"\nAdded {media.title} to project {project_name} without labels\n"
            )


def configure(args):
    configuration.configure(args)


def main():
    parser = argparse.ArgumentParser(
        description="Takes a movie/show from IMDB and assigns it as a Todoist task")
    subparsers = parser.add_subparsers()
    # Add task parser
    add_task_parser = subparsers.add_parser("add")
    add_task_parser.add_argument(
        "-m",
        "--media",
        help="media title / id / url",
        type=str,
        required=True,
        nargs="*",
    )
    add_task_parser.add_argument("-p",
                                 "--project",
                                 help="override default project name",
                                 type=str)
    add_task_parser.add_argument("-l",
                                 "--labels",
                                 help="override default label with given labels",
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