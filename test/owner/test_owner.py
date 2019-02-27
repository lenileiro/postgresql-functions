import json
from test.base import BaseTest
from database.models.owner import OwnerModel

class TestOwnerCreation(BaseTest):

    def test_create_owner_1(self):
        user = {
                'national_id': 32308040,
                'name': 'anthony',
                'email': 'lenileiro@gmail.com',
                'phone': '+254722447799'
            }
        OwnerModel.insert_user(user)
    
    def test_create_owner_2(self):
        user = {
                'national_id': 32308041,
                'name': 'Jane',
                'email': 'janek@gmail.com',
                'phone': '+254719457854'
            }
        OwnerModel.insert_user(user)
        