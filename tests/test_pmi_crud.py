import pry
import json
from tests.BaseCase import BaseCase
from database.pmi import downpayment_zero, downpayment_five, downpayment_ten, downpayment_fifteen

class TestPmiCrud(BaseCase):
    # POST
    def test_successful_post_pmi(self):
        # Given
        payload = {
            "downpayment_percentage": 0,
            "from_620_639": 2.25,
            "from_640_659": 2.05,
            "from_660_679": 1.90,
            "from_680_699": 1.4,
            "from_700_719": 1.15,
            "from_720_739": 0.95,
            "from_740_759": 0.75,
            "from_760_850": 0.55,
        }
        # When
        response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/pmi/{id}'
        # Then
        self.assertEqual(200, response.status_code)

        get_pmi = self.app.get(url, headers={"Content-Type": "application/json"})
        body = get_pmi.json['data']

        self.assertEqual(id, body['id'])
        self.assertEqual(payload, body['attributes'])

# GET single
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


# Get all
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

# PUT
    def test_successful_put_pmi(self):
        # Given
        payload = {
            "downpayment_percentage": 0,
            "from_620_639": 2.25,
            "from_640_659": 2.05,
            "from_660_679": 1.90,
            "from_680_699": 1.4,
            "from_700_719": 1.15,
            "from_720_739": 0.95,
            "from_740_759": 0.75,
            "from_760_850": 0.55,
        }


        create_pmi = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_pmi.json['data']['id']
        url = f'/api/v1/pmi/{id}'
# When
        updated_payload = {
            "downpayment_percentage": 0,
            "from_620_639": 3.6,
            "from_640_659": 2.05,
            "from_660_679": 1.90,
            "from_680_699": 1.4,
            "from_700_719": 1.15,
            "from_740_759": 0.87,
            "from_760_850": 0.49,
            "from_720_739": 0.95,
        }

        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']
        # pry()
# Then
        confirmation = self.app.get(confirmation_url, headers={'Content-Type': 'application/json'})
        confirmation_body = confirmation.json['data']['attributes']

        self.assertEqual(updated_payload['from_620_639'], confirmation_body['from_620_639'])
        self.assertNotEqual(payload['from_620_639'], confirmation_body['from_620_639'])

        self.assertEqual(updated_payload['from_740_759'], confirmation_body['from_740_759'])
        self.assertNotEqual(payload['from_740_759'], confirmation_body['from_740_759'])

        self.assertEqual(updated_payload['from_760_850'], confirmation_body['from_760_850'])
        self.assertNotEqual(payload['from_760_850'], confirmation_body['from_760_850'])

        self.assertEqual(updated_payload['from_640_659'], confirmation_body['from_640_659'])
        self.assertEqual(updated_payload['from_660_679'], confirmation_body['from_660_679'])
        self.assertEqual(updated_payload['from_680_699'], confirmation_body['from_680_699'])
        self.assertEqual(updated_payload['from_700_719'], confirmation_body['from_700_719'])
        self.assertEqual(updated_payload['from_720_739'], confirmation_body['from_720_739'])


# DESTROY
    def test_successful_delete_pmi(self):
# Given
        payload = {
            "downpayment_percentage": 0,
            "from_620_639": 3.6,
            "from_640_659": 2.05,
            "from_660_679": 1.90,
            "from_680_699": 1.4,
            "from_700_719": 1.15,
            "from_740_759": 0.87,
            "from_760_850": 0.49,
            "from_720_739": 0.95,
        }
        create_pmi = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        url = create_pmi.json['data']['confirmation']['url']
# When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        # pry()
# Then
        self.assertEqual('nil', body['id'])
