from cli_flows.flow_base import FlowBase


class GroupViewFlow(FlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing view existing groups command')
