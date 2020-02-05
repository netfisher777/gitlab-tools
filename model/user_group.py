from typing import List
from model.gitlab_project import GitlabProject


class UserGroup:
    def __init__(self):
        self.name: str = None
        self.alias: str = None
        self.gitlab_projects: List[GitlabProject] = []

    def add_project(self, gitlab_project: GitlabProject):
        self.gitlab_projects.append(gitlab_project)
