from cli_flows.flow_base import FlowBase
from gitlab_api.gitlab_adapter import GitlabAdapter
from model.gitlab_group import GitlabGroup
from model.gitlab_project import GitlabProject
from model.user_project import UserProject
from model.editable_user_group import EditableUserGroup
from store.user_projects_store import UserProjectsStore
from store.user_groups_store import UserGroupsStore
from model.user_projects import UserProjects
from model.user_group import UserGroup
from typing import Dict
import sys


class GroupCreateFlow(FlowBase):
    def __init__(self):
        super().__init__()
        self.__available_groups_dict: Dict[int, GitlabGroup] = None
        self.__current_projects_dict: Dict[int, GitlabProject] = None
        self.__editable_user_group: EditableUserGroup = EditableUserGroup()
        self.__gitlab_adapter: GitlabAdapter = None

    def start(self):
        super().start()
        print('Executing create new group command')
        self.__init_gitlab_adapter()
        self.__load_initial_data()
        name = input('Enter new group name: ')
        alias = input('Enter new group alias: ')
        self.__editable_user_group.name = name
        self.__verify_group_alias(alias)
        self.__editable_user_group.alias = alias
        self.__choose_available_groups_loop()

    def __init_gitlab_adapter(self):
        self.__gitlab_adapter = GitlabAdapter.from_connection_settings()
        self.__gitlab_adapter.connect()

    def __load_initial_data(self):
        gitlab_groups = self.__gitlab_adapter.get_available_groups()
        self.__available_groups_dict = {i + 1: gitlab_groups[i] for i in range(0, len(gitlab_groups))}

    def __choose_available_groups_loop(self):
        while True:
            print('Choose group number to add projects from:')
            self.__show_available_groups()
            user_input = input('Enter group number from the list above: ')
            if user_input in [FlowBase.RETURN_BACK_COMMAND, FlowBase.EXIT_COMMAND]:
                print('Exit command execution without saving')
                sys.exit(0)
            elif user_input == FlowBase.SAVE_COMMAND:
                self.__save_user_group()
            else:
                self.__verify_chosen_group_number(user_input)
                chosen_group_number = int(user_input)
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
            user_input = input('Enter project number from the list above: ')
            if user_input == FlowBase.RETURN_BACK_COMMAND:
                return
            elif user_input == FlowBase.EXIT_COMMAND:
                print('Exit command execution without saving')
                sys.exit(0)
            elif user_input == FlowBase.SAVE_COMMAND:
                self.__save_user_group()
            else:
                self.__add_chosen_project(user_input)

    def __show_current_projects(self):
        for index, project in self.__current_projects_dict.items():
            print(f'{index} {project.name} {project.path_with_namespace} {project.description}')

    def __save_user_group(self):
        group_name = self.__editable_user_group.name
        group_alias = self.__editable_user_group.alias
        print(f'Saving group with name = {group_name}, alias = {group_alias}')
        new_projects_list = self.__editable_user_group.projects_list
        user_projects = UserProjectsStore.load_from_store()
        user_projects.add_projects(new_projects_list)
        UserProjectsStore.save(user_projects)
        new_projects_aliases = [project.alias for project in new_projects_list]
        new_user_group = UserGroup(group_name, group_alias, new_projects_aliases)
        user_groups = UserGroupsStore.load_from_store()
        user_groups.add_group(new_user_group)
        UserGroupsStore.save(user_groups)
        sys.exit(0)

    def __add_chosen_project(self, chosen_project_number):
        self.__verify_chosen_project_number(chosen_project_number)
        chosen_project_number = int(chosen_project_number)
        chosen_project = self.__current_projects_dict[chosen_project_number]
        project_alias = input(f'Enter unique alias for project {chosen_project.path_with_namespace}: ')
        self.__verify_project_alias(project_alias)
        user_project = UserProject()
        user_project.alias = project_alias
        user_project.gitlab_project = chosen_project
        self.__editable_user_group.add_project(user_project)

    # TODO: add implementation
    def __verify_group_alias(self, group_alias):
        pass

    # TODO: add implementation
    def __verify_chosen_group_number(self, group_number):
        pass

    # TODO: add implementation
    def __verify_chosen_project_number(self, project_number):
        pass

    # TODO: add implementation
    def __verify_project_alias(self, project_alias):
        pass
