from store.connection_settings_store import ConnectionSettingsStore
from cli_flows.connection.connection_flow_base import ConnectionFlowBase


class ConnectionViewFlow(ConnectionFlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing view connection settings command')
        if ConnectionSettingsStore.is_settings_exist():
            print(f'Loaded settings from {ConnectionSettingsStore.get_settings_path()}:')
            ConnectionFlowBase.print_existing_connection_settings()
        else:
            print(f'Connection settings are not exist. Suspected path: {ConnectionSettingsStore.get_settings_path()}')
