import unittest
from database.createdb import init_db

class BaseTest(unittest.TestCase):

    def setUp(self):
        init_db()
