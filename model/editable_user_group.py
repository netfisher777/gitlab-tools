from model.user_project import UserProject
from typing import List


class EditableUserGroup:
    def __init__(self):
        self.name: str = None
        self.alias: str = None
        self.user_projects: List[UserProject] = []

    def add_project(self, user_project: UserProject):
        self.user_projects.append(user_project)
