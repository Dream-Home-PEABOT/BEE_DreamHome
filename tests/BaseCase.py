import unittest
from dreamhome import app
from database.db import db

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client() #talks to flask
        self.db = db.get_db() #talks to database
            # add records here (maybe) given, when, then

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
