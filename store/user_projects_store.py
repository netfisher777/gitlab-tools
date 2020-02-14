import json
from store.app_store import AppStore
from model.user_projects import UserProjects
from utils.string_utils import StringUtils


class UserProjectsStore:
    USER_PROJECTS_FILE_NAME = 'user-projects.json'

    @staticmethod
    def save(user_projects: UserProjects):
        settings_as_json = json.dumps(user_projects.__dict__, default=lambda o: o.__dict__, indent=4)
        AppStore.dump_content_to_file(filename=UserProjectsStore.USER_PROJECTS_FILE_NAME,
                                      content=settings_as_json)

    @staticmethod
    def exist():
        return AppStore.is_file_exists(UserProjectsStore.USER_PROJECTS_FILE_NAME)

    @staticmethod
    def get_path():
        return AppStore.build_file_relative_path_string(UserProjectsStore.USER_PROJECTS_FILE_NAME)

    @staticmethod
    def load_from_store():
        if AppStore.is_file_exists(UserProjectsStore.USER_PROJECTS_FILE_NAME):
            user_projects_data = AppStore.get_file_contents(UserProjectsStore.USER_PROJECTS_FILE_NAME)
            if StringUtils.is_empty(user_projects_data):
                return None
            user_projects_json = json.loads(user_projects_data)
            user_projects = UserProjects.from_json(user_projects_json)
            return user_projects
        else:
            return None
