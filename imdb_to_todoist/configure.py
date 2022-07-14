from dataclasses import dataclass
import os
import json
from imdb_to_todoist import todoist
from imdb_to_todoist import imdb_api
from typing import List
from todoist_api_python.models import Project
from todoist_api_python.api import TodoistAPI


@dataclass
class Config:
    IMDB_API_KEY: str
    TODOIST_API_KEY: str
    default_project_id: str
    

def configure_imdb_api_key() -> str:
    while True:
        IMDB_API_KEY = input("Enter the IMDB API key: ")
        if imdb_api.is_valid_api_key(IMDB_API_KEY):
            return IMDB_API_KEY
        else:
            print("Invalid key, try again.")


def configure_todoist_api_key() -> str:
    while True:
        TODOIST_API_KEY = input("Enter the Todoist API key: ")
        if todoist.is_valid_api_key(TODOIST_API_KEY):
            return TODOIST_API_KEY
        else:
            print("Invalid key, try again.")


def select_project(projects: List[Project]) -> Project:
    print("Pick the default project where to place all tasks.")
    for i, project in enumerate(projects):
        print(f"{i + 1}. {project.name}")
    project_index = int(input("Select the project by typing leading number: ")) - 1
    return projects[project_index]


def configure() -> Config:
    with open('data.json', 'w') as file:
        # Get required fields
        IMDB_API_KEY = configure_imdb_api_key()
        TODOIST_API_KEY = configure_todoist_api_key()

        todoistAPI = TodoistAPI(TODOIST_API_KEY)
        project = select_project(todoistAPI.get_projects())
        default_project_id = project.id
        data = {
            "IMDB_API_KEY": IMDB_API_KEY,
            "TODOIST_API_KEY": TODOIST_API_KEY,
            "default_project_id": default_project_id,
        }
        json.dump(data, file)
        config = Config(IMDB_API_KEY, TODOIST_API_KEY, default_project_id)
        return config


def load_configuration_json() -> Config:
    with open('data.json', 'r') as file:
        config_json = json.load(file)
        config = Config(
            config_json["IMDB_API_KEY"],
            config_json["TODOIST_API_KEY"],
            config_json["default_project_id"],
        )
        return config


def load_configuration():
    if not os.path.exists("data.json"):
        return configure()
    else:
        return load_configuration_json()