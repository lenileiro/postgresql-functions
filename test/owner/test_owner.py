import json
from test.base import BaseTest
from database.models.owner import OwnerModel

class TestPostRequest(BaseTest):

    def test_account_creation(self):
        user = {
                'national_id': 32308961,
                'name': 'anthony',
                'email': 'lenileiro@gmail.com',
                'phone': '+254729363838'
            }
        OwnerModel.insert_user(user)
        