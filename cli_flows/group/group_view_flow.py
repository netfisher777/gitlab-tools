from cli_flows.flow_base import FlowBase
from cli_flows.group.group_flow_base import GroupFlowBase
import sys


class GroupViewFlow(GroupFlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing view existing groups command')
        self.__choose_user_group_alias_loop()

    def __choose_user_group_alias_loop(self):
        while True:
            self._show_user_groups()
            user_input = input('Choose group alias to view its contents ("all" - to view all groups): ')
            if user_input == FlowBase.ALL_COMMAND:
                print('-------------------------START OF GROUP CONTENTS-------------------------')
                self.__show_all_groups_with_contents()
                print('-------------------------END OF GROUP CONTENTS---------------------------')
            elif user_input == FlowBase.EXIT_COMMAND:
                sys.exit(0)
            elif self._verify_chosen_group_alias(user_input):
                print('-------------------------START OF GROUP CONTENTS-------------------------')
                self._show_group_projects(user_input)
                print('-------------------------END OF GROUP CONTENTS---------------------------')

    def __show_all_groups_with_contents(self):
        for group_alias in self._user_groups_dict.keys():
            self._show_group_projects(group_alias)
