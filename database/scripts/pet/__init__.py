def create_pet(cur):
    files = ['pet']
    for f in files:
        filepath = f'database/scripts/pet/{f}.pgsql'
        with open(filepath, mode='r') as rf:
            sql = rf.read()
            cur.execute(sql)