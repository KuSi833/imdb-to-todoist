from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Project
from typing import List

from src.imdb import Movie
from src.parse_input import parse_bool


def is_valid_api_key(TODOIST_API_KEY: str) -> bool:
    "Checks if the given API KEY is valid."
    todoist = TodoistAPI(TODOIST_API_KEY)
    try:
        todoist.get_projects()
        return True
    except:
        return False


class TodoistPort():
    def __init__(self, TODOIST_API_KEY: str) -> None:
        self.todoist = TodoistAPI(TODOIST_API_KEY)

    def get_projects(self) -> Project:
        projects = self.todoist.get_projects()

        print("Pick the default project where to place all tasks.")
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project.name}")
        project_index = int(input("Select the project by typing leading number: ")) - 1
        return projects[project_index]

    def get_label_id(self, label_name: str) -> str:
        "TODO: Use some kind of cache"
        labels = self.todoist.get_labels()
        for label in labels:
            if label.name == label_name:
                return label.id
        print(f"Couldn't find label with name: {label_name}.")
        ans = parse_bool("Would you like to create it?", default_value=False)
        if not ans:
            print("Exiting script.")
            quit()
        label = self.todoist.add_label(label_name)
        return label.id

    def get_project_id(self, project_name: str) -> str:
        "TODO: Use some kind of cache"
        projects = self.todoist.get_projects()
        for project in projects:
            if project.name == project_name:
                return project.id
        print(f"Couldn't find project with name: {project_name}.")
        ans = parse_bool("Would you like to create it?", default_value=False)
        if not ans:
            print("Exiting script.")
            quit()
        project = self.todoist.add_project(project_name)
        return project.id

    def make_task(self, movie: Movie, labels: List[str], project_name: str) -> None:
        content = f"[{movie.title}]({movie.link})"
        description = movie.plot
        project_id = self.get_project_id(project_name)
        if labels:
            self.todoist.add_task(content=content,
                                  description=description,
                                  project_id=project_id,
                                  labels=labels)
        else:
            self.todoist.add_task(content=content,
                                  description=description,
                                  project_id=project_id)
