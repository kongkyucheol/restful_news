import os.path


class AdminRepo:
    filename = "admin.txt"

    def __init__(self):
        self.data = [
            {'0': 'OpenNews'},
            {'1': '한경닷컴'},
        ]

    def post(self, json):
        self.data = json

    def get(self):
        return self.data
