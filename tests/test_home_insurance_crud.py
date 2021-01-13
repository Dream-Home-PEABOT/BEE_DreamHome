import json
import pry
from tests.BaseCase import BaseCase
from database.insurance import gecko, country_farm, postgressive

class TestHomeInsuranceCrud(BaseCase):
    # POST  
    def test_successful_post_home_insurance(self):
        gecko = {
            "state": "Oklahoma",
            "average_rate": 4445
        }

        response = self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(gecko))
        id = response.json['data']['id']
        url = f'/api/v1/home_insurance/{id}'

        self.assertEqual(201, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(gecko, body['attributes'])

    # single GET
    def test_successful_get_home_insurance(self):
        insurance1 = self.app.post(
            '/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(gecko))
        insurance2 = self.app.post(
            '/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(country_farm))

        id = insurance1.json['data']['id']
        url = f'/api/v1/home_insurance/{id}'

        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, insurance2.json['data']['id'])
        self.assertEqual(gecko, body['attributes'])

    # GET all
    def test_succssful_get_property_tax(self):
        self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(gecko))
        self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(country_farm))
        self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(postgressive))

        response = self.app.get('/api/v1/home_insurance', headers={"Content-Type": "application/json"})
        body = response.json['data']

        self.assertEqual(200, response.status_code)
        self.assertEqual(3, len(body))
        self.assertEqual(gecko, body['colorado']['attributes'])
        self.assertEqual(country_farm, body['kentucky']['attributes'])
        self.assertEqual(postgressive, body['illnois']['attributes'])

    # PUT
    def test_successful_put_education(self):
        # Given
        payload = {
            "state": "Best Virginia",
            "average_rate": 1200
        }

        create_insurance = self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_insurance.json['data']['id']
        url = f'/api/v1/home_insurance/{id}'

        # When
        updated_payload = {
            "state": "West Virginia",
            "average_rate": 2486
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']

        # Then
        confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
        confirmation_body = confirmation.json['data']['attributes']

        self.assertEqual(updated_payload['state'], confirmation_body['state'])
        self.assertNotEqual(payload['state'], confirmation_body['state'])

        # This is the only field that wasn't updated, so it only tests the final response against the original creation
        self.assertEqual(updated_payload['average_rate'], confirmation_body['average_rate'])
        self.assertNotEqual(payload['average_rate'], confirmation_body['average_rate'])

        self.assertEqual(200, response.status_code)

     # DESTROY
    def test_successful_delete_insurance(self):
        # Given
        payload = {
            "state": "West Kansas",
            "average_rate": 3000
        }
        insurance1 = self.app.post('/api/v1/home_insurance', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = insurance1.json['data']['id']
        url = f'/api/v1/home_insurance/{id}'

        # When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = response.json['data']

        # Then
        self.assertEqual('nil', body['id'])
