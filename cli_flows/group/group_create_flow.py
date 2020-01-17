from cli_flows.flow_base import FlowBase


class GroupCreateFlow(FlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing create new group command')
        group_name = input('Enter new group name: ')
        print('Choose ')
