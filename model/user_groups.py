from model.user_group import UserGroup
from typing import Dict
from typing import List


class UserGroups:
    def __init__(self, groups: Dict[str, UserGroup] = {}):
        """
        groups: Dict[str, UserGroup] - alias for key, UserGroup for value
        """
        self.groups: Dict[str, UserGroup] = groups

    def add_group(self, group: UserGroup):
        self.groups[group.alias] = group
        return self

    def add_groups(self, groups_list: List[UserGroup]):
        for group in groups_list:
            self.add_group(group)
        return self

    @classmethod
    def from_json(cls, data):
        groups_dict = data['groups']
        if not groups_dict:
            return None
        group_dict_values = groups_dict.values()
        if len(group_dict_values) < 1:
            return None
        groups = {group.alias: group for group in map(UserGroup.from_json, group_dict_values)}
        return cls(groups)
