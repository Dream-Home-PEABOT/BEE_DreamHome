import json
from tests.BaseCase import BaseCase
from database.home_insurance import florida


class TestHomeInsuranceCrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index=0, end_index=1, replacement=''):
        return '%s%s%s' % (text[:index], replacement, text[end_index:])

    # CREATE SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_post_insurance_not_unique(self):
    # Given
        initial_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
    # When
        error_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        body = error_response.json['data']
    # Then
        self.assertEqual(400, error_response.status_code)
        self.assertEqual('Not Unique Error', body['error'])
        self.assertEqual("This insurance record's classification already exists in the database", body['message'])

    def test_unsuccessful_post_home_insurance_extra_field_incorrect(self):
    # Given
        extra_field_payload = {
            "bad_attribute": "Oops",
            "too_much_money": 10000000000,
            "what_is_this": "i_dont_even"
        }
    # When
        extra_field_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = extra_field_response.json['data']
    # Then
        self.assertEqual(406, extra_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.", body['message'])

    def test_unsuccessful_post_home_insurance_field_incorrect(self):
    # Given
        incorrect_field_payload = {
            "state": 79,
            "annual_average_insurance_rate": 1200
        }
    # When
        incorrect_field_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = incorrect_field_response.json['data']
    # Then
        self.assertEqual(406, incorrect_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # READ by ID SAD PATHS  -----------------------------------------------------------
    def test_unsuccessful_get_by_id_home_insurance_incorrect_id(self):
    # Given
        insurance_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))

        id = insurance_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/home-insurance/{new_id}'
    # When
        incorrect_id_response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Home Insurance record with given id doesn't exist.", body['message'])

    # UPDATE SAD PATHS  -----------------------------------------------------------
    def test_unsuccessful_put_home_insurance_incorrect_id(self):
    # Given
        insurance_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))

        id = insurance_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/home-insurance/{new_id}'
    # When
        incorrect_id_response = self.app.put(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Insurance record with given id doesn't exist.", body['message'])


    def test_unsuccessful_put_home_insurance_bad_fields(self):
    # Given
        insurance_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))

        id = insurance_response.json['data']['id']
        url = f'/api/v1/home-insurance/{id}'
    # When
        extra_field_payload = {
            "bad_attribute": "Oops",
            "too_much_money": 10000000000
        }
        bad_field_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = bad_field_response.json['data']
    # Then
        self.assertEqual(406, bad_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # DESTROY SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_delete_home_insurance_incorrect_id(self):
    # Given
        insurance_response = self.app.post('/api/v1/home-insurance', headers={"Content-Type": "application/json"}, data=json.dumps(florida))

        id = insurance_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/home-insurance/{new_id}'
    # When
        incorrect_id_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Insurance record with given id doesn't exist.", body['message'])
