import json
from test.base import BaseTest
from database.models.pet import PetModel

class TestPostRequest(BaseTest):

    def test_create_pet_1_owner_1(self):
        pet = {
                'pet_id': 1,
                'name': 'simba',
                'age': 2,
                'owner_id': 32308040
            }
        PetModel.insert_pet(pet)
    
    def test_create_pet_2_owner_1(self):
        pet = {
                'pet_id': 3,
                'name': 'parrot',
                'age': 1,
                'owner_id': 32308040
            }
        PetModel.insert_pet(pet)
    
    def test_create_pet_1_owner_2(self):
        pet = {
                'pet_id': 2,
                'name': 'goat',
                'age': 1,
                'owner_id': 32308041
            }
        PetModel.insert_pet(pet)