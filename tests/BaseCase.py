import unittest
import json
from app import app
from database.db import db
from database.mortgage_rate import range_300_619, range_620_639, range_640_659, range_660_679, range_680_699, range_700_759, range_760_850
from database.home_insurance import illinois, colorado
hi_il_insurance = illinois
hi_co_insurance = colorado
from database.property_tax import illinois, colorado

class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()
        # Post for mortgage_rate
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_300_619))
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_620_639))
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_640_659))
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_660_679))
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_680_699))
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_700_759))
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_760_850))
        # Post for insurance
        self.app.post('/api/v1/home-insurance', headers={"Content-Type":"application/json"}, data=json.dumps(hi_il_insurance))
        self.app.post('/api/v1/home-insurance', headers={"Content-Type":"application/json"}, data=json.dumps(hi_co_insurance))
        # Post for property tax
        self.app.post('/api/v1/property-tax', headers={"Content-Type":"application/json"}, data=json.dumps(illinois))
        self.app.post('/api/v1/property-tax', headers={"Content-Type":"application/json"}, data=json.dumps(colorado))
        # Post for median home price

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
