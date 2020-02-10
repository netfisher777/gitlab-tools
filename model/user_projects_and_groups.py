from model.user_project import UserProject
from model.user_group import UserGroup
from typing import Dict


class UserProjectsAndGroups:
    def __init__(self, projects: Dict[str, UserProject], groups: Dict[str, UserGroup]):
        """
        projects: Dict[str, UserProject] - path_with_namespace for key, UserProject for value,
        groups: Dict[str, UserGroup] - alias for key, UserGroup for value
        """
        self.projects: Dict[str, UserProject] = projects
        self.groups: Dict[str, UserGroup] = groups
