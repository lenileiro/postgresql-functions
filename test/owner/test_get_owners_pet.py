import json
from test.base import BaseTest
from database.models.owner import OwnerModel
from database.models.pet import PetModel

class TestGetOwnersPet(BaseTest):

    def test_create_owner_with_pet(self):
        user = {
                'national_id': 2222222,
                'name': 'anthony',
                'email': 'lenileiro@gmail.com',
                'phone': '+254722447799'
            }
        OwnerModel.insert_user(user)

        simba = {
                'pet_id': 50,
                'name': 'simba',
                'age': 2,
                'owner_id': 2222222
            }

        rabbit = {
                'pet_id': 51,
                'name': 'rabbit',
                'age': 2,
                'owner_id': 2222222
            }
            
        PetModel.insert_pet(rabbit)
        PetModel.insert_pet(simba)

        response = OwnerModel.pets(2222222)
        #name
        self.assertIsInstance(response[0][0], str)
        self.assertIsInstance(response[1][0], str)
        #age
        self.assertIsInstance(response[0][1], int)
        self.assertIsInstance(response[1][1], int)