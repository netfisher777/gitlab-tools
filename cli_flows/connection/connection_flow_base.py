from store.connection_settings_store import ConnectionSettingsStore
from cli_flows.flow_base import FlowBase
from abc import abstractmethod


class ConnectionFlowBase(FlowBase):
    def __init__(self):
        super().__init__()

    @staticmethod
    def print_existing_connection_settings():
        settings = ConnectionSettingsStore.load_from_store()
        print(f'Gitlab url: {settings.gitlab_url}')
        print(f'API access token: {settings.access_token}')

    @abstractmethod
    def start(self):
        super().start()
