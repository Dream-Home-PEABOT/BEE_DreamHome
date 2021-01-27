import pry
import json
from tests.BaseCase import BaseCase
from database.pmi import downpayment_zero, downpayment_five, downpayment_ten, downpayment_fifteen

class TestPmiCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post_pmi(self):
    # Given
        payload = {
            "downpayment_percentage": 0,
            "range_620_639": 2.25,
            "range_640_659": 2.05,
            "range_660_679": 1.90,
            "range_680_699": 1.4,
            "range_700_719": 1.15,
            "range_720_739": 0.95,
            "range_740_759": 0.75,
            "range_760_850": 0.55,
        }
    # When
        response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/pmi/{id}'
    # Then
        self.assertEqual(201, response.status_code)
        get_pmi = self.app.get(url, headers={"Content-Type": "application/json"})
        body = get_pmi.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(payload, body['attributes'])

    # READ by ID -----------------------------------------------------------
    def test_successful_get_pmi(self):
    # Given
        create_downpayment_0 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        create_downpayment_10 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_ten))

        id = create_downpayment_0.json['data']['id']
        url = f'/api/v1/pmi/{id}'
    # When
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, create_downpayment_10.json['data']['id'])
        self.assertEqual(downpayment_zero, body['attributes'])


    # READ all -----------------------------------------------------------
    def test_successful_get_all_pmi(self):
    # Given
        create_downpayment_0 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        create_downpayment_5 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_five))
        create_downpayment_10 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_ten))
        create_downpayment_15 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_fifteen))
    # When
        response = self.app.get('/api/v1/pmi', headers={"Content-Type": "application/json"})
        body = response.json['data']
        returned_dp_zero = body['downpayment_0']
        returned_dp_five = body['downpayment_5']
        returned_dp_ten = body['downpayment_10']
        returned_dp_fifteen = body['downpayment_15']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(downpayment_zero, returned_dp_zero['attributes'])
        self.assertEqual(downpayment_five, returned_dp_five['attributes'])
        self.assertEqual(downpayment_ten, returned_dp_ten['attributes'])
        self.assertEqual(downpayment_fifteen, returned_dp_fifteen['attributes'])

    # UPDATE -----------------------------------------------------------
    def test_successful_put_pmi(self):
    # Given
        payload = {
            "downpayment_percentage": 0,
            "range_620_639": 2.25,
            "range_640_659": 2.05,
            "range_660_679": 1.90,
            "range_680_699": 1.4,
            "range_700_719": 1.15,
            "range_720_739": 0.95,
            "range_740_759": 0.75,
            "range_760_850": 0.55,
        }
        create_pmi = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_pmi.json['data']['id']
        url = f'/api/v1/pmi/{id}'
    # When
        updated_payload = {
            "downpayment_percentage": 0,
            "range_620_639": 3.6,
            "range_640_659": 2.05,
            "range_660_679": 1.90,
            "range_680_699": 1.4,
            "range_700_719": 1.15,
            "range_740_759": 0.87,
            "range_760_850": 0.49,
            "range_720_739": 0.95,
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']
    # Then
        confirmation = self.app.get(confirmation_url, headers={'Content-Type': 'application/json'})
        confirmation_body = confirmation.json['data']['attributes']
        self.assertEqual(202, response.status_code)
        self.assertEqual(updated_payload['range_620_639'], confirmation_body['range_620_639'])
        self.assertNotEqual(payload['range_620_639'], confirmation_body['range_620_639'])
        self.assertEqual(updated_payload['range_740_759'], confirmation_body['range_740_759'])
        self.assertNotEqual(payload['range_740_759'], confirmation_body['range_740_759'])
        self.assertEqual(updated_payload['range_760_850'], confirmation_body['range_760_850'])
        self.assertNotEqual(payload['range_760_850'], confirmation_body['range_760_850'])
        self.assertEqual(updated_payload['range_640_659'], confirmation_body['range_640_659'])
        self.assertEqual(updated_payload['range_660_679'], confirmation_body['range_660_679'])
        self.assertEqual(updated_payload['range_680_699'], confirmation_body['range_680_699'])
        self.assertEqual(updated_payload['range_700_719'], confirmation_body['range_700_719'])
        self.assertEqual(updated_payload['range_720_739'], confirmation_body['range_720_739'])


    # DESTROY -----------------------------------------------------------
    def test_successful_delete_pmi(self):
    # Given
        payload = {
            "downpayment_percentage": 0,
            "range_620_639": 3.6,
            "range_640_659": 2.05,
            "range_660_679": 1.90,
            "range_680_699": 1.4,
            "range_700_719": 1.15,
            "range_740_759": 0.87,
            "range_760_850": 0.49,
            "range_720_739": 0.95,
        }
        create_pmi = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        url = create_pmi.json['data']['confirmation']['url']
    # When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
    # Then
        self.assertEqual(204, response.status_code)
