from cli_flows.flow_base import FlowBase
from gitlab_api.gitlab_adapter import GitlabAdapter
from gitlab_api.gitlab_group import GitlabGroup
from typing import Dict


class GroupCreateFlow(FlowBase):
    def __init__(self):
        super().__init__()
        self.__group_name = None
        self.__group_alias = None
        self.__available_groups_dict: Dict[int, GitlabGroup] = None
        self.__current_repositories_dict = None
        self.__gitlab_adapter: GitlabAdapter = None

    def start(self):
        super().start()
        print('Executing create new group command')
        self.__init_gitlab_adapter()
        self.__load_initial_data()
        self.__group_name = input('Enter new group name: ')
        self.__group_alias = input('Enter new group alias: ')
        self.__add_repositories_loop()

    def __init_gitlab_adapter(self):
        self.__gitlab_adapter = GitlabAdapter.from_connection_settings()
        self.__gitlab_adapter.connect()

    def __add_repositories_loop(self):
        print('Choose group to add repositories from:')
        self.__print_available_groups_dict()
        chosen_group_number = input('Enter group number from the list above: ')
        self.__verify_group_number_existence(chosen_group_number)
        chosen_group_number = int(chosen_group_number)
        group = self.__available_groups_dict[chosen_group_number]
        gitlab_projects = self.__gitlab_adapter.get_available_projects_for_group(group.id)
        for project in gitlab_projects:
            print(f'{project.id} {project.name} {project.url} {project.ssh_clone_url} {project.http_clone_url} {project.path_with_namespace} {project.description}')

    def __load_initial_data(self):
        groups = self.__gitlab_adapter.get_available_groups()
        self.__available_groups_dict = {i + 1: groups[i] for i in range(0, len(groups))}

    def __print_available_groups_dict(self):
        for index, value in self.__available_groups_dict.items():
            print(f'{index} {value.name} {value.url}')

    # TODO: add implementation
    def __verify_group_number_existence(self, group_number):
        pass
