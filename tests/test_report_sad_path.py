from tests.BaseCase import BaseCase
from database.report import imaginative, pragmatic
import json
import pry


class TestReportCrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index=0, end_index=1, replacement=''):
        return '%s%s%s' % (text[:index], replacement, text[end_index:])

    #single GET
    def test_unsuccessful_get_by_id_report_incorrect_id(self):
        # Given
        tax_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = tax_response.json['data']['id']
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

    # PUT
    def test_unsuccessful_update_report_incorrect_id(self):
        # Given
        tax_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = tax_response.json['data']['id']
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

    def test_unsuccessful_update_report_bad_fields(self):
        # Given
        tax_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = tax_response.json['data']['id']
        url = f'/api/v1/report/{id}'

        # When
        incorrect_field_payload = {
            "salary": 75000.0,
            "zipcode": 11112,
            "credit_score": 760,
            "monthly_debt": 1300.0,
            "downpayment_savings": 20000.0,
            "downpayment_percentage": 10.0,
            "this_one_is_wrong": "sorry"
        }
        bad_field_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = bad_field_response.json['data']

        # Then
        self.assertEqual(406, bad_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Report documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # DESTROY
    def test_unsuccessful_delete_report_incorrect_id(self):
        # Given
        tax_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        id = tax_response.json['data']['id']
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

    # POST
    def test_unsuccessful_post_report_extra_field_incorrect(self):
        # Given
        extra_field_payload = {
            "salary": 75000.0,
            "zipcode": 11112,
            "credit_score": 760,
            "monthly_debt": 1300.0,
            "downpayment_savings": 20000.0,
            "downpayment_percentage": 10.0,
            "goal_principal": 0.0,
            "oops_one_more": "my_bad"
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
            "salary": 75000.0,
            "zipcode": 11112,
            "credit_score": 760,
            "monthly_debt": 1300.0,
            "downpayment_savings": 20000.0,
            "downpayment_percentage": 10.0,
            "goal_principal": "zero point zero"
        }

        # When
        incorrect_field_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = incorrect_field_response.json['data']

        # Then
        self.assertEqual(406, incorrect_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Report documentation. Request is missing a required field or incorrect field entered.", body['message'])
