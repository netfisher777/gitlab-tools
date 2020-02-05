import json

from model.connection_settings import ConnectionSettings
from store.app_store import AppStore


class ConnectionSettingsStore:
    CONNECTION_SETTINGS_FILE_NAME = 'connection-settings.json'

    @staticmethod
    def save_settings(settings: ConnectionSettings):
        settings_as_json = json.dumps(settings.__dict__, indent=4)
        AppStore.dump_content_to_file(filename=ConnectionSettingsStore.CONNECTION_SETTINGS_FILE_NAME,
                                      content=settings_as_json)

    @staticmethod
    def is_settings_exist():
        return AppStore.is_file_exists(ConnectionSettingsStore.CONNECTION_SETTINGS_FILE_NAME)

    @staticmethod
    def get_settings_path():
        return AppStore.build_file_relative_path_string(ConnectionSettingsStore.CONNECTION_SETTINGS_FILE_NAME)

    @staticmethod
    def load_saved_settings():
        settings_as_json = AppStore.get_file_contents(ConnectionSettingsStore.CONNECTION_SETTINGS_FILE_NAME)
        settings_map = json.loads(settings_as_json)
        settings = ConnectionSettings.from_dict(settings_map)
        return settings
