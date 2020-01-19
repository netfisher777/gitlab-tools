import gitlab
from gitlab_api.gitlab_group import GitlabGroup


class GitlabAdapter:
    def __init__(self, connection_url, access_token):
        self.__connection_url = connection_url
        self.__access_token = access_token
        self.__gitlab_api = gitlab.Gitlab(url=self.__connection_url, private_token=self.__access_token)

    def connect(self):
        self.__gitlab_api.auth()

    def get_available_groups(self):
        groups_from_api = self.__gitlab_api.groups.list()
        groups = [GitlabGroup(group_from_api.id, group_from_api.web_url, group_from_api.name)
                  for group_from_api in groups_from_api]
        return groups
