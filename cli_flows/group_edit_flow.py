from cli_flows.flow_base import FlowBase


class GroupEditFlow(FlowBase):
    def __init__(self):
        FlowBase.__init__(self)

    @staticmethod
    def start_edit_group_flow():
        print('Executing edit existing group command')
