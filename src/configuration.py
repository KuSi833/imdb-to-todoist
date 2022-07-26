from pathlib import Path
import pickle
from dataclasses import dataclass
from src import todoist
from src import imdb_api
from typing import List, Optional
from src.util import get_project_root
from todoist_api_python.models import Project
from todoist_api_python.api import TodoistAPI
from src.exceptions import MissingAttributeException


@dataclass
class Config:
    IMDB_API_KEY: Optional[str] = None
    TODOIST_API_KEY: Optional[str] = None
    default_project_name: Optional[str] = None
    default_label_name: Optional[str] = None

    def check_if_complete(self) -> None:
        if self.IMDB_API_KEY is None:
            raise MissingAttributeException("IMDB Api Key")
        if self.TODOIST_API_KEY is None:
            raise MissingAttributeException("Todoist Api Key")

    def __str__(self) -> str:
        s = []
        for key, value in self.__dict__.items():
            s.append(f"{key}: {value}\n")
        return "".join(s)


# def configure_imdb_api_key() -> str:
#     while True:
#         IMDB_API_KEY = input("Enter the IMDB API key: ")
#         if imdb_api.is_valid_api_key(IMDB_API_KEY):
#             return IMDB_API_KEY
#         else:
#             print("Invalid key, try again.")

# def configure_todoist_api_key() -> str:
#     while True:
#         TODOIST_API_KEY = input("Enter the Todoist API key: ")
#         if todoist.is_valid_api_key(TODOIST_API_KEY):
#             return TODOIST_API_KEY
#         else:
#             print("Invalid key, try again.")

# def select_project(projects: List[Project]) -> Project:
#     print("Pick the default project where to place all tasks.")
#     for i, project in enumerate(projects):
#         print(f"{i + 1}. {project.name}")
#     project_index = int(input("Select the project by typing leading number: ")) - 1
#     return projects[project_index]


def configure(args):
    config = load_configuration()
    if args.imdb:
        if imdb_api.is_valid_api_key(args.imdb):
            config.IMDB_API_KEY = args.imdb
            print("valid IMDB API key entered and saved")
        else:
            print("invalid IMDB API key entered, skipped")
    if args.todoist:
        if todoist.is_valid_api_key(args.todoist):
            config.TODOIST_API_KEY = args.todoist
            print("valid Todoist API key entered and saved")
        else:
            print("invalid Todoist API key entered, skipped")
    elif args.project:
        config.default_project_name = args.project
        print(f"Default project name assigned to: {config.default_project_name}")
    elif args.label:
        config.default_label_name = args.label
        print(f"Default label name assigned to: {config.default_label_name}")


def load_configuration_from_file(file_path: Path) -> Config:
    return pickle.load(open(file_path, "rb"))


def load_configuration() -> Config:
    config_file_name = "data.p"
    config_path = get_project_root() / config_file_name
    if not config_path.exists():
        config = Config()
    else:
        config = load_configuration_from_file(config_path)
    return config
