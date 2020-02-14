from model.user_project import UserProject
from typing import Dict
from typing import List


class UserProjects:
    def __init__(self, projects: Dict[str, UserProject] = None):
        """
        projects: Dict[str, UserProject] - path_with_namespace for key, UserProject for value
        """
        self.projects: Dict[str, UserProject] = projects if projects is not None else {}

    def add_project(self, user_project: UserProject):
        self.projects[user_project.alias] = user_project
        return self

    def add_projects(self, user_projects: List[UserProject]):
        for user_project in user_projects:
            self.add_project(user_project)
        return self

    @classmethod
    def from_json(cls, data):
        projects_dict = data['projects']
        if not projects_dict:
            return None
        project_dict_values = projects_dict.values()
        if len(project_dict_values) < 1:
            return None
        projects = {project.alias: project for project in map(UserProject.from_json, project_dict_values)}
        return cls(projects)
