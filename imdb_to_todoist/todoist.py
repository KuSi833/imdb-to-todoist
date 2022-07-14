from todoist_api_python.api import TodoistAPI
from todoist_api_python.models import Project
from typing import List

from imdb_to_todoist.imdb import Movie


def is_valid_api_key(TODOIST_API_KEY: str) -> bool:
    "Checks if the given API KEY is valid."
    todoist = TodoistAPI(TODOIST_API_KEY)
    try:
        todoist.get_projects()
        return True
    except:
        return False


class TodoistPort():
    def __init__(self, TODOIST_API_KEY: str, default_project_id: str) -> None:
        self.todoist = TodoistAPI(TODOIST_API_KEY)
        self.default_project_id = default_project_id

    def get_projects(self) -> Project:
        projects = self.todoist.get_projects()

        print("Pick the default project where to place all tasks.")
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project.name}")
        project_index = int(input("Select the project by typing leading number: ")) - 1
        return projects[project_index]

    def make_task(self, movie: Movie) -> None:
        content = f"[{movie.title}]({movie.link})"
        description = movie.plot
        self.todoist.add_task(
            content=content,
            description=description,
            project_id=self.default_project_id,
        )