from cli_flows.flow_base import FlowBase


class GroupCreateFlow(FlowBase):
    def __init__(self):
        super().__init__()
        self.__group_name = None
        self.__group_alias = None
        self.__available_repositories = None

    def start(self):
        super().start()
        print('Executing create new group command')
        self.__init_available_repositories()
        self.__group_name = input('Enter new group name: ')
        self.__group_alias = input('Enter new group alias: ')
        print('Choose repositories to add in new group:')
        self.__print_available_repositories()

    def __init_available_repositories(self):
        pass

    def __print_available_repositories(self):
        pass
