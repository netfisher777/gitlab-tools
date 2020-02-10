from model.user_group import UserGroup
from typing import Dict


class UserGroups:
    def __init__(self, groups: Dict[str, UserGroup]):
        """
        groups: Dict[str, UserGroup] - alias for key, UserGroup for value
        """
        self.groups: Dict[str, UserGroup] = groups
