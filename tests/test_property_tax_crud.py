import json
from tests.BaseCase import BaseCase
from database.property_tax import texas, kentucky, nevada


class TestPropertyTaxCrud(BaseCase):
    # CREATE  -----------------------------------------------------------
    def test_successful_post_propertey_tax(self):
    # Given
        new_state = {
        "state": "West Kansas",
        "avg_tax_rate": 0.32,
        "annual_avg_property_tax": 1200,
        }
    # When
        response = self.app.post('/api/v1/property-tax', headers={"Content-Type": "application/json"}, data=json.dumps(new_state))
        id = response.json['data']['id']
        url = f'/api/v1/property-tax/{id}'
    # Then
        self.assertEqual(201, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(new_state, body['attributes'])

    # READ by ID -----------------------------------------------------------
    def test_successful_get_property_tax(self):
    # Given
        create_state = self.app.post('/api/v1/property-tax', headers={"Content-Type": "application/json"}, data=json.dumps(texas))
        create_state2 = self.app.post('/api/v1/property-tax', headers={"Content-Type": "application/json"}, data=json.dumps(kentucky))
        id = create_state.json['data']['id']
        url = f'/api/v1/property-tax/{id}'
    # When
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, create_state2.json['data']['id'])
        self.assertEqual(texas, body['attributes'])

    # READ all -----------------------------------------------------------
    def test_succssful_get_property_tax(self):
    # Given
        self.app.post('/api/v1/property-tax',headers={"Content-Type": "application/json"}, data=json.dumps(texas))
        self.app.post('/api/v1/property-tax',headers={"Content-Type": "application/json"}, data=json.dumps(kentucky))
        self.app.post('/api/v1/property-tax',headers={"Content-Type": "application/json"}, data=json.dumps(nevada))
    # When
        response = self.app.get('/api/v1/property-tax', headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        # There are already 2 records in the system for CO and IL
        self.assertEqual(5, len(body))
        self.assertEqual(texas, body['texas']['attributes'])
        self.assertEqual(kentucky, body['kentucky']['attributes'])
        self.assertEqual(nevada, body['nevada']['attributes'])

    # UPDATE  -----------------------------------------------------------
    def test_successful_put_education(self):
    # Given
        payload = {
            "state": "West Virginia",
            "avg_tax_rate": 0.57,
            "annual_avg_property_tax": 802
        }
        create_property_tax = self.app.post('/api/v1/property-tax', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_property_tax.json['data']['id']
        url = f'/api/v1/property-tax/{id}'
    # When
        updated_payload = {
            "state": "Best Virginia",
            "avg_tax_rate": 0.69,
            "annual_avg_property_tax": 420
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']
    # Then
        confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
        confirmation_body = confirmation.json['data']['attributes']
        self.assertEqual(updated_payload['state'], confirmation_body['state'])
        self.assertNotEqual(payload['state'], confirmation_body['state'])
    # This is the only field that wasn't updated, so it only tests the final response against the original creation
        self.assertEqual(updated_payload['avg_tax_rate'], confirmation_body['avg_tax_rate'])
        self.assertNotEqual(payload['avg_tax_rate'], confirmation_body['avg_tax_rate'])
        self.assertEqual(updated_payload['annual_avg_property_tax'], confirmation_body['annual_avg_property_tax'])
        self.assertNotEqual(payload['annual_avg_property_tax'], confirmation_body['annual_avg_property_tax'])
        self.assertEqual(202, response.status_code)

    # DESTROY -----------------------------------------------------------
    def test_successful_delete_property_tax(self):
    # Given
        payload = {
            "state": "West Kansas",
            "avg_tax_rate": 0.32,
            "annual_avg_property_tax": 1200
        }
        create_state = self.app.post('/api/v1/property-tax', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_state.json['data']['id']
        url = f'/api/v1/property-tax/{id}'
    # When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual('nil', body['id'])
    # Once you have error handling done, the following can be tested
        # confirmation = self.app.get(url, headers={"Content-Type": "application/json"})
        # confirmation_body = confirmation.json
