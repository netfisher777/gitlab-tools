from model.gitlab_project import GitlabProject


class UserProject:
    def __init__(self, alias: str = None, gitlab_project: GitlabProject = None):
        self.alias: str = alias
        self.gitlab_project: GitlabProject = gitlab_project

    @classmethod
    def from_json(cls, data):
        alias = data['alias']
        gitlab_project_dict = data['gitlab_project']
        gitlab_project = GitlabProject.from_json(gitlab_project_dict)
        return cls(alias, gitlab_project)
