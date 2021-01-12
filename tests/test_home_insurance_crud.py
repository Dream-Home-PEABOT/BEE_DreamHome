import json
import pry
from tests.BaseCase import BaseCase

class TestHomeInsuranceCrud(BaseCase):
    # POST  
    def test_successful_get_home_insurance(self):
        gecko = {
            "state": "Oklahoma",
            "average rate": 4445
        }

        response = self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(gecko))
        pry()
        id = response.json['data']['id']
        url = f'/api/v1/home_insurance/{id}'

        self.assertEqual(200, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(gecko, body['attributes'])