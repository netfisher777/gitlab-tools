from cli_flows.flow_base import FlowBase
from store.user_groups_store import UserGroupsStore
from store.user_projects_store import UserProjectsStore
from model.user_group import UserGroup
from model.user_project import UserProject
from typing import Dict
import sys


class GroupViewFlow(FlowBase):
    def __init__(self):
        super().__init__()
        self.__user_groups_dict: Dict[str, UserGroup] = {}
        self.__user_projects_dict: Dict[str, UserProject] = {}

    def start(self):
        super().start()
        print('Executing view existing groups command')
        self.__load_initial_data()
        self.__choose_group_alias_loop()

    def __choose_group_alias_loop(self):
        while True:
            self.__show_user_groups()
            user_input = input('Choose alias to view its contents ("all" - to view all groups): ')
            if user_input == FlowBase.ALL_COMMAND:
                print('-------------------------START OF GROUP CONTENTS-------------------------')
                self.__show_all_groups_with_contents()
                print('-------------------------END OF GROUP CONTENTS---------------------------')
            elif user_input == FlowBase.EXIT_COMMAND:
                sys.exit(0)
            elif self.__verify_chosen_group_alias(user_input):
                print('-------------------------START OF GROUP CONTENTS-------------------------')
                self.__show_group_projects(user_input)
                print('-------------------------END OF GROUP CONTENTS---------------------------')

    def __load_initial_data(self):
        self.__user_groups_dict = UserGroupsStore.load_from_store().groups
        self.__user_projects_dict = UserProjectsStore.load_from_store().projects

    def __show_user_groups(self):
        groups = self.__user_groups_dict.values()
        if len(groups) < 1:
            print('You don\'t have any group. You can add new one with "glt group -c" command')
            sys.exit(0)
        print('Available groups:')
        for group in groups:
            print(f'alias: {group.alias}, name: {group.name}')

    def __show_all_groups_with_contents(self):
        for group_alias in self.__user_groups_dict.keys():
            self.__show_group_projects(group_alias)

    def __show_group_projects(self, group_alias):
        user_group = self.__user_groups_dict[group_alias]
        print(f'Group {user_group.name}({user_group.alias}) projects:')
        for project_alias in user_group.user_project_aliases:
            user_project = self.__user_projects_dict[project_alias]
            print(f'{user_project.gitlab_project.path_with_namespace} {user_project.gitlab_project.description}')

    def __verify_chosen_group_alias(self, group_alias):
        user_group = self.__user_groups_dict.get(group_alias)
        if user_group:
            return True
        else:
            return False
