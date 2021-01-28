from tests.BaseCase import BaseCase
from database.report import imaginative, pragmatic
import json


class TestReportCrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index=0, end_index=1, replacement=''):
        return '%s%s%s' % (text[:index], replacement, text[end_index:])

    # CREATE SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_post_report_extra_field_incorrect(self):
    # Given
        extra_field_payload = {
            "zipcode": 80209,
            "credit_score": 710,
            "salary": 5000,
            "monthly_debt": 1500,
            "downpayment_savings": 50000,
            "mortgage_term": 30,
            "downpayment_percentage": 20,
            "goal_principal": 500000,
            "rent": 0,
            "extra_extra_field": "yo yo yo yo"
        }
    # When
        extra_field_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = extra_field_response.json['data']
    # Then
        self.assertEqual(406, extra_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Report documentation. Request is missing a required field or incorrect field entered.", body['message'])

    def test_unsuccessful_post_report_field_incorrect(self):
    # Given
        incorrect_field_payload = {
            "zipcode": 'ABCDE',
            "credit_score": 710,
            "salary": 5000,
            "monthly_debt": 1500,
            "downpayment_savings": 50000,
            "mortgage_term": 30,
            "downpayment_percentage": 20,
            "goal_principal": 500000,
            "rent": 0
        }
    # When
        incorrect_field_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = incorrect_field_response.json['data']
    # Then
        self.assertEqual(406, incorrect_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Report documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # READ by ID SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_get_by_id_report_incorrect_id(self):
    # Given
        initial_post = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = initial_post.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/report/{new_id}'
    # When
        incorrect_id_response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Report record with given id doesn't exist.", body['message'])

    # UPDATE SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_put_report_incorrect_id(self):
    # Given
        initial_post = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = initial_post.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/report/{new_id}'
    # When
        incorrect_id_response = self.app.put(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Report record with given id doesn't exist.", body['message'])

    def test_unsuccessful_put_report_bad_fields(self):
    # Given
        initial_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = initial_response.json['data']['id']
        url = f'/api/v1/report/{id}'
    # When
        incorrect_field_payload = {
            "field_does_not_exist": "sorry_not_sorry"
        }
        bad_field_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = bad_field_response.json['data']
    # Then
        self.assertEqual(406, bad_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Report documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # DESTROY SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_delete_report_incorrect_id(self):
    # Given
        initial_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = initial_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/report/{new_id}'
    # When
        incorrect_id_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Report record with given id doesn't exist.", body['message'])
