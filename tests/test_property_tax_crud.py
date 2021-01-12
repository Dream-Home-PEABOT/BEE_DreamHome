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

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(body))
        self.assertEqual(colorado, body['colorado']['attributes'])
        self.assertEqual(kentucky, body['kentucky']['attributes'])
        self.assertEqual(illnois, body['illnois']['attributes'])
     
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

    # PUT
    def test_successful_put_education(self):
        # Given
        payload = {
            "state": "West Virginia",
            "tax_rate": 0.57,
            "avg_property_tax": 802
        }

        create_property_tax = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_property_tax.json['data']['id']
        url = f'/api/v1/property_tax/{id}'

        # When
        updated_payload = {
            "state": "Best Virginia",
            "tax_rate": 0.69,
            "avg_property_tax": 420
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']

        # Then
        confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
        confirmation_body = confirmation.json['data']['attributes']

        self.assertEqual(updated_payload['state'], confirmation_body['state'])
        self.assertNotEqual(payload['state'], confirmation_body['state'])

        # This is the only field that wasn't updated, so it only tests the final response against the original creation
        self.assertEqual(updated_payload['tax_rate'], confirmation_body['tax_rate'])
        self.assertNotEqual(payload['tax_rate'], confirmation_body['tax_rate'])

        self.assertEqual(updated_payload['avg_property_tax'], confirmation_body['avg_property_tax'])
        self.assertNotEqual(payload['avg_property_tax'], confirmation_body['avg_property_tax'])

        self.assertEqual(200, response.status_code)

    # DESTROY
    def test_successful_delete_property_tax(self):
        # Given
        payload = {
            "state": "West Kansas",
            "tax_rate": 0.32,
            "avg_property_tax": 1200
        }
        create_state = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_state.json['data']['id']
        url = f'/api/v1/property_tax/{id}'

        # When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = response.json['data']

        # Then
        self.assertEqual('nil', body['id'])
        # Once you have error handling done, the following can be tested
        # confirmation = self.app.get(url, headers={"Content-Type": "application/json"})
        # confirmation_body = confirmation.json
