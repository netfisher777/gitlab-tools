import json
from store.app_store import AppStore
from model.user_groups import UserGroups
from utils.string_utils import StringUtils


class UserGroupsStore:
    USER_GROUPS_FILE_NAME = 'user-groups.json'

    @classmethod
    def save(cls, user_groups: UserGroups):
        groups_as_json = json.dumps(user_groups.__dict__, default=lambda o: o.__dict__, indent=4)
        AppStore.dump_content_to_file(filename=cls.USER_GROUPS_FILE_NAME,
                                      content=groups_as_json)

    @classmethod
    def get_path(cls):
        return AppStore.build_file_relative_path_string(cls.USER_GROUPS_FILE_NAME)

    @classmethod
    def load_from_store(cls):
        if AppStore.is_file_exists(cls.USER_GROUPS_FILE_NAME):
            user_groups_data = AppStore.get_file_contents(UserGroupsStore.USER_GROUPS_FILE_NAME)
            if StringUtils.is_empty(user_groups_data):
                return UserGroups()
            user_groups_json = json.loads(user_groups_data)
            user_groups = UserGroups.from_json(user_groups_json)
            return user_groups
        else:
            return UserGroups()
