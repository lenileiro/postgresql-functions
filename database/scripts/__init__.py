from .owner import create_owner
from .pet import create_pet

def setup(cur):
    with open("database/scripts/setup.pgsql", mode='r') as rf:
            sql = rf.read()
            cur.execute(sql)

    create_owner(cur)
    create_pet(cur)