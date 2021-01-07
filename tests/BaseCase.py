import unittest
import json
from dreamhome import app
from database.db import db
from database.education import salary, zip, debt, savings, credit, percent, term, rent, principal

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(salary))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(zip))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(debt))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(credit))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(percent))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(term))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(rent))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(principal))

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
