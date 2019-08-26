from store.connection_settings_store import ConnectionSettingsStore
from store.connection_settings import ConnectionSettings


def start_setup_connection_flow():
    print('Executing setup connection settings command')
    url = input('Enter url to gitlab: ')
    access_token = input('Enter your access token to gitlab: ')
    connection_settings = ConnectionSettings(gitlab_url=url, access_token=access_token)
    ConnectionSettingsStore.save_settings(connection_settings)


def start_view_connection_flow():
    print('Executing view connection settings command')
    if ConnectionSettingsStore.is_settings_exist():
        settings = ConnectionSettingsStore.load_saved_settings()
        print(f'Loaded settings from {ConnectionSettingsStore.get_settings_path()}:')
        print(f'Gitlab url: {settings.gitlab_url}')
        print(f'API access token: {settings.gitlab_url}')
    else:
        print(f'Connection settings are not exist. Suspected path: {ConnectionSettingsStore.get_settings_path()}')
