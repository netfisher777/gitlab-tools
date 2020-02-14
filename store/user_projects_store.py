import json
from store.app_store import AppStore
from model.user_projects import UserProjects
from utils.string_utils import StringUtils


class UserProjectsStore:
    USER_PROJECTS_FILE_NAME = 'user-projects.json'

    @classmethod
    def save(cls, user_projects: UserProjects):
        projects_as_json = json.dumps(user_projects.__dict__, default=lambda o: o.__dict__, indent=4)
        AppStore.dump_content_to_file(filename=cls.USER_PROJECTS_FILE_NAME,
                                      content=projects_as_json)

    @classmethod
    def get_path(cls):
        return AppStore.build_file_relative_path_string(cls.USER_PROJECTS_FILE_NAME)

    @classmethod
    def load_from_store(cls):
        if AppStore.is_file_exists(cls.USER_PROJECTS_FILE_NAME):
            user_projects_data = AppStore.get_file_contents(cls.USER_PROJECTS_FILE_NAME)
            if StringUtils.is_empty(user_projects_data):
                return UserProjects()
            user_projects_json = json.loads(user_projects_data)
            user_projects = UserProjects.from_json(user_projects_json)
            return user_projects
        else:
            return UserProjects()
