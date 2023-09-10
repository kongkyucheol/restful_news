import os.path


class AdminRepo:
    filename = "admin.txt"

    def __init__(self):
        self.data = [
            {'key': 'opennews', 'title': 'OpenNews', 'url': 'remote', 'valid': '60'},
            {'key': 'hd_all', 'title': '한경 닷컴', 'url': 'local', 'valid': '1'},
            {'key': 'hd_finance', 'title': '한경 닷컴(증권)', 'url': 'local', 'valid': '1'},
        ]

    def post(self, json):
        self.data = json

    def get(self):
        return self.data
