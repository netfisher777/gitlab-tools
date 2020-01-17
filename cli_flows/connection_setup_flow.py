from store.connection_settings_store import ConnectionSettingsStore
from store.connection_settings import ConnectionSettings
from cli_flows.connection_flow_base import ConnectionFlowBase
from cli_flows.flow_base import FlowBase


class ConnectionSetupFlow(ConnectionFlowBase):
    def __init__(self):
        super().__init__()

    def start(self):
        super().start()
        print('Executing setup connection settings command')

        write_new_settings = True

        if ConnectionSettingsStore.is_settings_exist():
            print(f'Connection settings already exist in {ConnectionSettingsStore.get_settings_path()}: ')
            ConnectionFlowBase.print_existing_connection_settings()
            write_new_settings = FlowBase.ask_user_to_overwrite_existing('Do you want to overwrite them? (y/n):')

        if write_new_settings:
            ConnectionSetupFlow.__write_new_settings_subflow()

    @staticmethod
    def __write_new_settings_subflow():
        url = input('Enter url to gitlab: ')
        access_token = input('Enter your access token to gitlab: ')
        connection_settings = ConnectionSettings(gitlab_url=url, access_token=access_token)
        ConnectionSettingsStore.save_settings(connection_settings)
