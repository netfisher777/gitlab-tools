from cli_flows.flow_base import FlowBase
from abc import abstractmethod
from model.user_group import UserGroup
from model.user_project import UserProject
from store.user_groups_store import UserGroupsStore
from store.user_projects_store import UserProjectsStore
from typing import Dict
import sys


class GroupFlowBase(FlowBase):
    def __init__(self):
        super().__init__()
        self._user_groups_dict: Dict[str, UserGroup] = {}
        self._user_projects_dict: Dict[str, UserProject] = {}

    @abstractmethod
    def start(self):
        super().start()
        self._load_initial_data()

    def _load_initial_data(self):
        self._user_groups_dict = UserGroupsStore.load_from_store().groups
        self._user_projects_dict = UserProjectsStore.load_from_store().projects

    def _show_user_groups(self):
        groups = self._user_groups_dict.values()
        if len(groups) < 1:
            print('You don\'t have any group. You can add a new one with "glt group -c" command')
            sys.exit(0)
        print('Available groups:')
        for group in groups:
            print(f'alias: {group.alias}, name: {group.name}')

    def _show_group_projects(self, group_alias):
        user_group = self._user_groups_dict[group_alias]
        print(f'Group {user_group.name}({user_group.alias}) projects:')
        for project_alias in user_group.user_project_aliases:
            user_project = self._user_projects_dict[project_alias]
            print(f'alias = {user_project.alias}, path = {user_project.gitlab_project.path_with_namespace}, description = {user_project.gitlab_project.description}')

    def _verify_chosen_group_alias(self, group_alias):
        user_group = self._user_groups_dict.get(group_alias)
        if user_group:
            return True
        else:
            return False
