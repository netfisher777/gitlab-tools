from model.user_project import UserProject
from typing import List


class EditableUserGroup:
    def __init__(self):
        self.name: str = None
        self.alias: str = None
        self.projects_list: List[UserProject] = []

    def add_project(self, user_project: UserProject):
        self.projects_list.append(user_project)
