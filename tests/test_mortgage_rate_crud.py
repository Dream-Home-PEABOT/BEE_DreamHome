import json
from tests.BaseCase import BaseCase
from database.mortgage_rate import range_620_639, range_640_659, range_660_679, range_680_699, range_700_759, range_760_850


class TestMortgageRateCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post_of_mortgage_rate(self):
    # Given
        payload = {
            "credit_score_floor": "620",
            "credit_score_ceiling":"639",
            "rate": 4.13
        }
    # When
        response = self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/mortgage_rate/{id}'
    # Then
        self.assertEqual('201 CREATED', response.status)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(payload, body['attributes'])

    # READ by ID -----------------------------------------------------------
    def test_successful_get_of_mortgage_rate(self):
    # Given
        low_range = self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_620_639))
        high_range = self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_760_850))
        id = low_range.json['data']['id']
        url = f'/api/v1/mortgage_rate/{id}'
    # When
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, high_range.json['data']['id'])
        self.assertEqual(range_620_639, body['attributes'])

    # READ all -----------------------------------------------------------
    def test_succssful_get_mortgage_rate(self):
    # Given
        self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_620_639))
        self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_640_659))
        self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_660_679))
        self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_680_699))
        self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_700_759))
        self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(range_760_850))
    # When
        response = self.app.get('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"})
        body = response.json['data']
        returned_range_620_639 = body['range_620_639']
        returned_range_640_659 = body['range_640_659']
        returned_range_660_679 = body['range_660_679']
        returned_range_680_699 = body['range_680_699']
        returned_range_700_759 = body['range_700_759']
        returned_range_760_850 = body['range_760_850']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(6, len(body))
        self.assertEqual(range_620_639, returned_range_620_639['attributes'])
        self.assertEqual(range_640_659, returned_range_640_659['attributes'])
        self.assertEqual(range_660_679, returned_range_660_679['attributes'])
        self.assertEqual(range_680_699, returned_range_680_699['attributes'])
        self.assertEqual(range_700_759, returned_range_700_759['attributes'])
        self.assertEqual(range_760_850, returned_range_760_850['attributes'])

    # UPDATE  -----------------------------------------------------------
    def test_successful_put_mortgage_rate(self):
    # Given
        payload = {
            "credit_score_floor": "Testing",
            "credit_score_ceiling":"Testing",
            "rate": 888.0
        }
        create_mortgage_rate = self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_mortgage_rate.json['data']['id']
        url = f'/api/v1/mortgage_rate/{id}'
    # When
        updated_payload = {
            "credit_score_floor": "Testing",
            "credit_score_ceiling":"Testing",
            "rate": 777.0
            }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']
    # Then
        confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
        confirmation_body = confirmation.json['data']['attributes']
        self.assertEqual(updated_payload['credit_score_floor'], confirmation_body['credit_score_floor'])
        self.assertEqual(payload['credit_score_ceiling'], confirmation_body['credit_score_ceiling'])
        self.assertNotEqual(payload['rate'], confirmation_body['rate'])
        self.assertEqual(202, response.status_code)

    # DESTROY -----------------------------------------------------------
    def test_successful_delete_mortgage_rate(self):
    # Given
        payload = {
            "credit_score_floor": "620",
            "credit_score_ceiling":"639",
            "rate": 4.13
        }
        mortgage_rate = self.app.post('/api/v1/mortgage_rate', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = mortgage_rate.json['data']['id']
        url = f'/api/v1/mortgage_rate/{id}'
    # When
        response = self.app.delete(url, headers={"Content-Type": "application/json"})
    # Then
        self.assertEqual(204, response.status_code)
