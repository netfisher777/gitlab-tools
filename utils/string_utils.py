class StringUtils:
    def __init__(self):
        pass

    @staticmethod
    def is_empty(data):
        data = data.strip() if data else ''
        if not data:
            return True
        else:
            return False
