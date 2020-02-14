from typing import List


class UserGroup:
    def __init__(self, name: str = None, alias: str = None, user_project_aliases: List[str] = []):
        self.name: str = name
        self.alias: str = alias
        self.user_project_aliases: List[str] = user_project_aliases

    @classmethod
    def from_json(cls, data):
        name = data['name']
        alias = data['alias']
        user_project_aliases_list = data['user_project_aliases']
        return cls(name, alias, user_project_aliases_list)
