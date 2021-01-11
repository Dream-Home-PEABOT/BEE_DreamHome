import pry
import json
from tests.BaseCase import BaseCase
from database.property_tax import colorado, kentucky, illnois


class TestPropertyTaxCrud(BaseCase):
    # single GET
    def test_successful_get_property_tax(self):
        create_state = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))
        create_state2 = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(kentucky))

        id = create_state.json['data']['id']
        url = f'/api/v1/property_tax/{id}'

        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, create_state2.json['data']['id'])
        self.assertEqual(colorado, body['attributes'])

    # GET all
    def test_succssful_get_property_tax(self):
        self.app.post('/api/v1/property_tax',headers={"Content-Type": "application/json"}, data=json.dumps(colorado))
        self.app.post('/api/v1/property_tax',headers={"Content-Type": "application/json"}, data=json.dumps(kentucky))
        self.app.post('/api/v1/property_tax',headers={"Content-Type": "application/json"}, data=json.dumps(illnois))
      
        response = self.app.get('/api/v1/property_tax', headers={"Content-Type": "application/json"})
        body = response.json['data']
        returned_state = body['state']
        returned_tax_rate = body['tax_rate']
        returned_avg_property_tax_rate = body['avg_property_tax_rate']

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(body))
        self.assertEqual(colorado, returned_salar['attributes'])
        self.assertEqual(kentucky, returned_zip['attributes'])
        self.assertEqual(illnois, returned_debt['attributes'])
     
     # POST
    def test_successful_post_propertey_tax(self):
        # Given
        new_state = {
            "state": "West Kansas",
            "tax_rate": 0.32,
            "avg_property_tax": 1200,
        }

        response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(new_state))
        id = response.json['data']['id']
        url = f'/api/v1/property_tax/{id}'

        self.assertEqual(200, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(new_state, body['attributes'])
