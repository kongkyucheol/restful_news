import os.path


class AdminRepo:
    filename = "admin.txt"

    def __init__(self):
        self.data = [
            {'key': 'opennews', 'title': 'OpenNews', 'urlType': 'remote', 'valid_time': 60,'valid':True},
            {'key': 'hd_all', 'title': '한경 닷컴', 'urlType': 'local', 'valid_time': 1,'valid':True},
            {'key': 'hd_finance', 'title': '한경 증권', 'urlType': 'local', 'valid_time': 1,'valid':False},
        ]

    def post(self, json):
        self.data = json

    def get(self):
        return self.data
