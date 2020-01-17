from cli_flows.flow_base import FlowBase


class GroupEditFlow(FlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing edit existing group command')
