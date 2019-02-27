from database.createdb import connect_to_db
from ..model import Base

conn = connect_to_db()
conn.set_session(autocommit=True)
cur = conn.cursor()
class OwnerModel:
    @staticmethod
    def insert_user(params):
        Base.insert('owner',
        national_id=params["national_id"],
        name=params["name"],
        email=params["email"],
        phone=params["phone"]
        )

    @staticmethod
    def pets(_id):
        cur.execute(f"SELECT * FROM find_pets({_id});")
        found_data = cur.fetchall()
        return found_data