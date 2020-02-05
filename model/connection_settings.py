class ConnectionSettings:
    def __init__(self, gitlab_url: str, access_token: str):
        self.gitlab_url = gitlab_url
        self.access_token = access_token

    @staticmethod
    def from_dict(dictionary):
        gitlab_url = dictionary['gitlab_url']
        access_token = dictionary['access_token']
        return ConnectionSettings(gitlab_url=gitlab_url, access_token=access_token)
