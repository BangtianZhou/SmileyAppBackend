# Dummy Attraction
# All class name default as service
from services.location.api import db_api
class service():

    def __init__(self):
        pass

    def test(self):
        print('request attraction service succeed')

    def test_db_connection(self):
        data = db_api.test()
        return data

    def find_nearby_attractions(self):
        pass
