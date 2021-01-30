import json
from tests.BaseCase import BaseCase
from database.median_home_value import florida, alaska

class TestMedianHomeCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post(self):
    # Given
        # The "florida" payload that was imported on line 12 above
    # When
        post_response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        post_data = post_response.json['data']
        id = post_data['id']
        url = f'/api/v1/median-home-value/{id}'
    # Then
        self.assertEqual(201, post_response.status_code)
        self.assertEqual('To see this new record, please do a GET request using the url', post_data['confirmation']['info'])
        self.assertEqual(url, post_data['confirmation']['url'])
    # Confirm with GET by ID
        confirmation_get_response = self.app.get(url, headers={"Content-Type": "application/json"})
        get_data = confirmation_get_response.json['data']
        self.assertEqual(id, get_data['id'])
        self.assertEqual(florida['year'], get_data['attributes']['year'])
        self.assertEqual(florida['state'], get_data['attributes']['state'])
        self.assertEqual(florida['avg_home_value'], get_data['attributes']['avg_home_value'])

    # READ by ID -----------------------------------------------------------
    def test_successful_get_by_id(self):
    # Given
        # The "florida" payload that was imported on line 12 above
        post_response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        id = post_response.json['data']['id']
        url = f'/api/v1/median-home-value/{id}'
    # When
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        data = response.json['data']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(id, data['id'])
        self.assertEqual(254607, data['attributes']['avg_home_value'])
        self.assertEqual('Florida', data['attributes']['state'])
        self.assertEqual(2020, data['attributes']['year'])

    # READ all -----------------------------------------------------------
    def test_successful_get_all(self):
    # Given
        # The "florida" payload that was imported on line 12 above
        florida_post_response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        florida_id = florida_post_response.json['data']['id']
        florida_url = f'/api/v1/median-home-value/{florida_id}'
        # The "alaska" payload that was imported on line 12 above
        alaska_post_response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(alaska))
        alaska_id = alaska_post_response.json['data']['id']
        alaska_url = f'/api/v1/median-home-value/{alaska_id}'
    # When
        all_response = self.app.get('/api/v1/median-home-value', headers={"Content-Type": "application/json"})
        data = all_response.json['data']
        data_alaska = data['home_value_of_alaska']
        data_florida = data['home_value_of_florida']
    # Then
        self.assertEqual(200, all_response.status_code)
        self.assertEqual(297111, data_alaska['attributes']['avg_home_value'])
        self.assertEqual('Alaska', data_alaska['attributes']['state'])
        self.assertEqual(2020, data_alaska['attributes']['year'])
        self.assertEqual(254607, data_florida['attributes']['avg_home_value'])
        self.assertEqual('Florida', data_florida['attributes']['state'])
        self.assertEqual(2020, data_florida['attributes']['year'])

    # UPDATE -----------------------------------------------------------
    def test_successful_put(self):
    # Given
        # The "florida" payload that was imported on line 12 above
        post_response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        id = post_response.json['data']['id']
        url = f'/api/v1/median-home-value/{id}'
    # When
        payload = {
            "year": 2021
        }
        update_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        data = update_response.json['data']
    # Then
        self.assertEqual(202, update_response.status_code)
        self.assertEqual(id, data['id'])
        self.assertEqual(url, data['confirmation']['url'])
        self.assertEqual("To see this record's updated response, please do a GET request using the url", data['confirmation']['info'])
    # Confirm with GET by ID
        confirmation_response = self.app.get(url, headers={"Content-Type": "application/json"})
        self.assertEqual(200, confirmation_response.status_code)
        self.assertEqual(2021, confirmation_response.json['data']['attributes']['year'])

    # DESTROY -----------------------------------------------------------
    def test_successful_delete(self):
    # Given
        # The "florida" payload that was imported on line 12 above
        post_response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        id = post_response.json['data']['id']
        url = f'/api/v1/median-home-value/{id}'
    # When
        delete_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        data = delete_response.json['data']
    # Then
        self.assertEqual(202, delete_response.status_code)
        self.assertEqual('nil', data['id'])
        self.assertEqual(url, data['confirmation']['url'])
        self.assertEqual("To see this record's deletion response, please do a GET request using the url", data['confirmation']['info'])
