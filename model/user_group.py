from typing import List


class UserGroup:
    def __init__(self):
        self.name: str = None
        self.alias: str = None
        self.user_project_keys: List[str] = []

    def add_project(self, user_project_key: str):
        self.user_project_keys.append(user_project_key)
