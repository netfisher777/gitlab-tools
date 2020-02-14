from typing import List


class UserGroup:
    def __init__(self):
        self.name: str = None
        self.alias: str = None
        self.user_project_aliases: List[str] = []

    def add_project(self, user_project_alias: str):
        self.user_project_aliases.append(user_project_alias)
