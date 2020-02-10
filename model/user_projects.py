from model.user_project import UserProject
from typing import Dict


class UserProjects:
    def __init__(self, projects: Dict[str, UserProject]):
        """
        projects: Dict[str, UserProject] - path_with_namespace for key, UserProject for value
        """
        self.projects: Dict[str, UserProject] = projects
