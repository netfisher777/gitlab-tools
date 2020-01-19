from cli_flows.flow_base import FlowBase
from gitlab_api.gitlab_adapter import GitlabAdapter


class GroupCreateFlow(FlowBase):
    def __init__(self):
        super().__init__()
        self.__group_name = None
        self.__group_alias = None
        self.__available_repositories = None
        self.__gitlab_adapter: GitlabAdapter = None

    def start(self):
        super().start()
        print('Executing create new group command')
        self.__load_initial_data()
        self.__group_name = input('Enter new group name: ')
        self.__group_alias = input('Enter new group alias: ')
        print('Choose repositories to add in new group:')
        self.__print_available_repositories()

    def __load_initial_data(self):
        self.__init_gitlab_adapter()
        self.__init_available_repositories()

    def __init_gitlab_adapter(self):
        self.__gitlab_adapter = GitlabAdapter.from_connection_settings()
        self.__gitlab_adapter.connect()

    def __init_available_repositories(self):
        self.__gitlab_adapter.get_available_groups()

    def __print_available_repositories(self):
        pass
