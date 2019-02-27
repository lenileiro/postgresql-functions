def create_owner(cur):
    files = ['owner']
    for f in files:
        filepath = f'database/scripts/owner/{f}.pgsql'
        with open(filepath, mode='r') as rf:
            sql = rf.read()
            cur.execute(sql)