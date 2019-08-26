from store.connection_settings_store import ConnectionSettingsStore
from store.connection_settings import ConnectionSettings


def start_setup_connection_flow():
    print('Executing setup connection settings command')

    write_new_settings = True

    if ConnectionSettingsStore.is_settings_exist():
        print(f'Connection settings already exist in {ConnectionSettingsStore.get_settings_path()}: ')
        print_existing_connection_settings()
        write_new_settings = ask_user_to_overwrite_existing()

    if write_new_settings:
        setup_connection_write_new_subflow()


def ask_user_to_overwrite_existing():
    result = None
    received_correct_user_input = False
    while not received_correct_user_input:
        overwrite_input = input('Do you want to overwrite them? (y/n): ')
        if overwrite_input.lower().strip() == 'n':
            received_correct_user_input = True
            result = False
        elif overwrite_input.lower().strip() == 'y':
            received_correct_user_input = True
            result = True
    return result


def setup_connection_write_new_subflow():
    url = input('Enter url to gitlab: ')
    access_token = input('Enter your access token to gitlab: ')
    connection_settings = ConnectionSettings(gitlab_url=url, access_token=access_token)
    ConnectionSettingsStore.save_settings(connection_settings)


def start_view_connection_flow():
    print('Executing view connection settings command')
    if ConnectionSettingsStore.is_settings_exist():
        print(f'Loaded settings from {ConnectionSettingsStore.get_settings_path()}:')
        print_existing_connection_settings()
    else:
        print(f'Connection settings are not exist. Suspected path: {ConnectionSettingsStore.get_settings_path()}')


def print_existing_connection_settings():
    settings = ConnectionSettingsStore.load_saved_settings()
    print(f'Gitlab url: {settings.gitlab_url}')
    print(f'API access token: {settings.access_token}')
