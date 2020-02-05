from cli_flows.flow_base import FlowBase
from gitlab_api.gitlab_adapter import GitlabAdapter
from gitlab_api.gitlab_group import GitlabGroup
from gitlab_api.gitlab_project import GitlabProject
from typing import Dict


class GroupCreateFlow(FlowBase):
    def __init__(self):
        super().__init__()
        self.__group_name = None
        self.__group_alias = None
        self.__available_groups_dict: Dict[int, GitlabGroup] = None
        self.__current_projects_dict: Dict[int, GitlabProject] = None
        self.__gitlab_adapter: GitlabAdapter = None

    def start(self):
        super().start()
        print('Executing create new group command')
        self.__init_gitlab_adapter()
        self.__load_initial_data()
        self.__group_name = input('Enter new group name: ')
        self.__group_alias = input('Enter new group alias: ')
        self.__choose_available_groups_loop()

    def __init_gitlab_adapter(self):
        self.__gitlab_adapter = GitlabAdapter.from_connection_settings()
        self.__gitlab_adapter.connect()

    def __load_initial_data(self):
        gitlab_groups = self.__gitlab_adapter.get_available_groups()
        self.__available_groups_dict = {i + 1: gitlab_groups[i] for i in range(0, len(gitlab_groups))}

    def __choose_available_groups_loop(self):
        print('Choose group number to add projects from:')
        self.__show_available_groups()
        chosen_group_number = input('Enter group number from the list above: ')
        self.__verify_chosen_group_number(chosen_group_number)
        chosen_group_number = int(chosen_group_number)
        self.__load_available_projects_for_group(chosen_group_number)
        self.__choose_from_current_projects_loop()

    def __show_available_groups(self):
        for index, group in self.__available_groups_dict.items():
            print(f'{index} {group.name} {group.url}')

    def __load_available_projects_for_group(self, group_number: int):
        group = self.__available_groups_dict[group_number]
        gitlab_projects = self.__gitlab_adapter.get_available_projects_for_group(group.id)
        self.__current_projects_dict = {i + 1: gitlab_projects[i] for i in range(0, len(gitlab_projects))}

    def __choose_from_current_projects_loop(self):
        print('Choose project number to add in your group:')
        self.__show_current_projects()
        while True:
            chosen_project_number = input(
                f'Enter project number from the list above ({FlowBase.RETURN_BACK_COMMAND} - to return back): ')
            if chosen_project_number == FlowBase.RETURN_BACK_COMMAND:
                self.__choose_available_groups_loop()
            else:
                self.__verify_chosen_project_number(chosen_project_number)
                chosen_project_number = int(chosen_project_number)


    def __show_current_projects(self):
        for index, project in self.__current_projects_dict:
            print(f'{index} {project.name} {project.path_with_namespace} {project.description}')

    # TODO: add implementation
    def __verify_chosen_group_number(self, group_number):
        pass

    # TODO: add implementation
    def __verify_chosen_project_number(self, project_number):
        pass
