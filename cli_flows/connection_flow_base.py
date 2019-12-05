from store.connection_settings_store import ConnectionSettingsStore
from cli_flows.flow_base import FlowBase


class ConnectionFlowBase(FlowBase):
    def __init__(self):
        FlowBase.__init__(self)

    @staticmethod
    def print_existing_connection_settings():
        settings = ConnectionSettingsStore.load_saved_settings()
        print(f'Gitlab url: {settings.gitlab_url}')
        print(f'API access token: {settings.access_token}')
