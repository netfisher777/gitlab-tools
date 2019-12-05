from cli_flows.flow_base import FlowBase


class GroupCreateFlow(FlowBase):
    def __init__(self):
        FlowBase.__init__(self)

    @staticmethod
    def start_create_group_flow():
        print('Executing create new group command')
        group_name = input('Enter new group name: ')
        print('Choose ')
