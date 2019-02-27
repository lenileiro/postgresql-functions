from ..model import Base
class PetModel:
    @staticmethod
    def insert_pet(params):
        Base.insert('pet',
        pet_id=params["pet_id"],
        name=params["name"],
        age=params["age"],
        owner_id=params["owner_id"]
        )