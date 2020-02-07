from model.gitlab_project import GitlabProject


class UserProject:
    def __init__(self):
        self.alias: str = None
        self.gitlab_project: GitlabProject = None
