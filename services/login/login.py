# Dummy Login
# All class name default as service
from services.login.api import db_api
class service():

    def __init__(self):
        pass

    def test(self):
        print('request login service succeed')

    def test_db_connection(self):
        data = db_api.test()
        return data

    def login(self, email):
        pass

    def logout(self, email):
        pass

    def create_user(self, email, password, name):
        pass

    def get_profile(self, usr_id):
        pass