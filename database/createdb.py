import os
from psycopg2 import connect
from scripts import setup

def connect_to_db(config=None):
    db_name = os.getenv("DATABASE_URL")
    conn = connect(db_name)
    conn.set_session(autocommit=True)
    return conn

def init_db(config=None):
    conn = connect_to_db()
    cur = conn.cursor()
    setup(cur)
    print('Database created successfully')


if __name__ == '__main__':
    init_db()