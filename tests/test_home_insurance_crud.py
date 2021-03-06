import json
from tests.BaseCase import BaseCase
from database.home_insurance import florida, california, washington


class TestHomeInsuranceCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post_home_insurance(self):
    # Given
        payload = {
            "state": "TestState",
            "annual_average_insurance_rate": 1111
        }
    # When
        response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/home-insurance/{id}'
    # Then
        self.assertEqual(201, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(payload, body['attributes'])

    # READ by ID -----------------------------------------------------------
    def test_successful_get_home_insurance(self):
    # Given
        insurance1 = self.app.post(
            '/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        insurance2 = self.app.post(
            '/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(california))
        id = insurance1.json['data']['id']
        url = f'/api/v1/home-insurance/{id}'
    # When
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, insurance2.json['data']['id'])
        self.assertEqual(florida, body['attributes'])

    # READ all -----------------------------------------------------------
    def test_succssful_get_property_tax(self):
    # Given
        self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(california))
        self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(washington))
    # When
        response = self.app.get('/api/v1/home-insurance', headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        # There are already records for CO and IL
        self.assertEqual(5, len(body))
        self.assertEqual(florida, body['florida']['attributes'])
        self.assertEqual(california, body['california']['attributes'])
        self.assertEqual(washington, body['washington']['attributes'])

    # UPDATE -----------------------------------------------------------
    def test_successful_put_education(self):
    # Given
        payload = {
            "state": "Best Virginia",
            "annual_average_insurance_rate": 1200
        }
        create_insurance = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_insurance.json['data']['id']
        url = f'/api/v1/home-insurance/{id}'
    # When
        updated_payload = {
            "state": "West Virginia",
            "annual_average_insurance_rate": 2486
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']
    # Then
        confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
        confirmation_body = confirmation.json['data']['attributes']
        self.assertEqual(updated_payload['state'], confirmation_body['state'])
        self.assertNotEqual(payload['state'], confirmation_body['state'])
    # This is the only field that wasn't updated, so it only tests the final response against the original creation
        self.assertEqual(updated_payload['annual_average_insurance_rate'], confirmation_body['annual_average_insurance_rate'])
        self.assertNotEqual(payload['annual_average_insurance_rate'], confirmation_body['annual_average_insurance_rate'])
        self.assertEqual(202, response.status_code)

    # DESTROY -----------------------------------------------------------
    def test_successful_delete_insurance(self):
    # Given
        payload = {
            "state": "West Kansas",
            "annual_average_insurance_rate": 3000
        }
        insurance1 = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = insurance1.json['data']['id']
        url = f'/api/v1/home-insurance/{id}'
    # When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
    # Then
        self.assertEqual(204, response.status_code)
