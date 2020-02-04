import gitlab
from gitlab_api.gitlab_group import GitlabGroup
from gitlab_api.gitlab_project import GitlabProject
from store.connection_settings_store import ConnectionSettingsStore


class GitlabAdapter:
    def __init__(self, connection_url, access_token):
        self.__connection_url = connection_url
        self.__access_token = access_token
        self.__gitlab_api = gitlab.Gitlab(url=self.__connection_url, private_token=self.__access_token)

    def connect(self):
        self.__gitlab_api.auth()

    def get_available_groups(self):
        groups_from_api = self.__gitlab_api.groups.list(all=True)
        groups = [GitlabGroup(group_from_api.id, group_from_api.web_url, group_from_api.name)
                  for group_from_api in groups_from_api]
        return groups

    def get_available_projects_for_group(self, group_id):
        group = self.__gitlab_api.groups.get(group_id)
        projects_from_api = group.projects.list(all=True)
        projects = [GitlabProject(project_from_api.id, project_from_api.ssh_url_to_repo, project_from_api.http_url_to_repo,
                                  project_from_api.web_url, project_from_api.name, project_from_api.description,
                                  project_from_api.path_with_namespace) for project_from_api in projects_from_api]
        return projects

    # TODO: throw exception when settings don't exist
    @staticmethod
    def from_connection_settings():
        if ConnectionSettingsStore.is_settings_exist():
            settings = ConnectionSettingsStore.load_saved_settings()
            adapter_instance = GitlabAdapter(settings.gitlab_url, settings.access_token)
            return adapter_instance
        else:
            return None
