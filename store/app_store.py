from pathlib import Path


class AppStore:
    APP_DIR_NAME = 'gitlab-tools'
    FILE_ENCODING = 'utf-8'

    @classmethod
    def dump_content_to_file(cls, filename: str, content: str):
        app_home_path = cls.get_app_home_path()
        app_home_path.mkdir(parents=True, exist_ok=True)
        file_path = Path.joinpath(app_home_path, filename)
        with file_path.open('w', encoding=cls.FILE_ENCODING) as file:
            file.write(content)

    @classmethod
    def is_file_exists(cls, filename: str):
        file_path = cls.build_file_relative_path(filename)
        return file_path.exists()

    @classmethod
    def get_app_home_path(cls):
        return Path.joinpath(Path.home(), cls.APP_DIR_NAME)

    @classmethod
    def build_file_relative_path(cls, filename: str):
        app_home_path = cls.get_app_home_path()
        file_path = Path.joinpath(app_home_path, filename)
        return file_path

    @classmethod
    def build_file_relative_path_string(cls, filename: str):
        file_path = cls.build_file_relative_path(filename)
        return str(file_path)

    @classmethod
    def get_file_contents(cls, filename: str):
        file_path = cls.build_file_relative_path(filename)
        return file_path.read_text(encoding=cls.FILE_ENCODING)
