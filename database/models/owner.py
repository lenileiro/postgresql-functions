from ..model import Base
class OwnerModel:
    @staticmethod
    def insert_user(params):
        Base.insert('owner',
        national_id=params["national_id"],
        name=params["name"],
        email=params["email"],
        phone=params["phone"]
        )