from store.connection_settings_store import ConnectionSettingsStore
from cli_flows.connection.connection_flow_base import ConnectionFlowBase


class ConnectionViewFlow(ConnectionFlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing view connection settings command')
        if ConnectionSettingsStore.exists():
            print(f'Loaded settings from {ConnectionSettingsStore.get_path()}:')
            ConnectionFlowBase.print_existing_connection_settings()
        else:
            print(f'Connection settings do not exist. Expected path: {ConnectionSettingsStore.get_path()}')
