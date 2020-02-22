from cli_flows.group.group_flow_base import GroupFlowBase
from cli_flows.flow_base import FlowBase
import sys


class GroupEditFlow(GroupFlowBase):
    def __init__(self):
        super().__init__()
        self.__chosen_group_alias: str = None

    def start(self):
        super().start()
        print('Executing edit existing group command')
        self.__choose_user_group_alias_loop()

    def __choose_user_group_alias_loop(self):
        while True:
            self._show_user_groups()
            user_input = input('Choose group alias to edit: ')
            if user_input == FlowBase.EXIT_COMMAND:
                sys.exit(0)
            elif self._verify_chosen_group_alias(user_input):
                self.__chosen_group_alias = user_input
                self.__edit_group_loop()

    def __edit_group_loop(self):
        self._show_group_projects(self.__chosen_group_alias)
