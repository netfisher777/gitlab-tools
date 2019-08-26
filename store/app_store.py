from pathlib import Path


class AppStore:

    APP_DIR_NAME = 'gitlab-tools'
    FILE_ENCODING = 'utf-8'

    @staticmethod
    def dump_content_to_file(filename: str, content: str):
        app_home_path = AppStore.get_app_home_path()
        app_home_path.mkdir(parents=True, exist_ok=True)
        file_path = Path.joinpath(app_home_path, filename)
        with file_path.open('w', encoding=AppStore.FILE_ENCODING) as file:
            file.write(content)

    @staticmethod
    def is_file_exists(filename: str):
        file_path = AppStore.build_file_relative_path(filename)
        return file_path.exists()

    @staticmethod
    def get_app_home_path():
        return Path.joinpath(Path.home(), AppStore.APP_DIR_NAME)

    @staticmethod
    def build_file_relative_path(filename: str):
        app_home_path = AppStore.get_app_home_path()
        file_path = Path.joinpath(app_home_path, filename)
        return file_path

    @staticmethod
    def build_file_relative_path_string(filename: str):
        file_path = AppStore.build_file_relative_path(filename)
        return str(file_path)

    @staticmethod
    def get_file_contents(filename: str):
        file_path = AppStore.build_file_relative_path(filename)
        return file_path.read_text(encoding=AppStore.FILE_ENCODING)