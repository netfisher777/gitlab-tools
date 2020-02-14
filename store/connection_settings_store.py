import json

from model.connection_settings import ConnectionSettings
from store.app_store import AppStore


class ConnectionSettingsStore:
    CONNECTION_SETTINGS_FILE_NAME = 'connection-settings.json'

    @classmethod
    def save(cls, settings: ConnectionSettings):
        settings_as_json = json.dumps(settings.__dict__, indent=4)
        AppStore.dump_content_to_file(filename=cls.CONNECTION_SETTINGS_FILE_NAME,
                                      content=settings_as_json)

    @classmethod
    def exists(cls):
        return AppStore.is_file_exists(cls.CONNECTION_SETTINGS_FILE_NAME)

    @classmethod
    def get_path(cls):
        return AppStore.build_file_relative_path_string(cls.CONNECTION_SETTINGS_FILE_NAME)

    @classmethod
    def load_from_store(cls):
        settings_as_json = AppStore.get_file_contents(cls.CONNECTION_SETTINGS_FILE_NAME)
        settings_map = json.loads(settings_as_json)
        settings = ConnectionSettings.from_dict(settings_map)
        return settings
