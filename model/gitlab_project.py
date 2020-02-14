class GitlabProject:
    def __init__(self, id: int, ssh_clone_url: str, http_clone_url: str, url: str, name: str, description: str,
                 path_with_namespace: str):
        self.id = id
        self.ssh_clone_url = ssh_clone_url
        self.http_clone_url = http_clone_url
        self.url = url
        self.name = name
        self.description = description
        self.path_with_namespace = path_with_namespace

    @classmethod
    def from_json(cls, data):
        return cls(**data)
