from cli_flows.flow_base import FlowBase


class GroupViewFlow(FlowBase):
    def __init__(self):
        FlowBase.__init__(self)

    @staticmethod
    def start_view_groups_flow():
        print('Executing view existing groups command')
