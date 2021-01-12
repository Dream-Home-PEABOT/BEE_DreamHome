from tests.BaseCase import BaseCase
import json
import pry

class TestReportCrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index = 0, end_index = 1, replacement = ''):
        return '%s%s%s'%(text[:index], replacement, text[end_index:])
# GET single
    def test_unsuccessful_get_by_id_report_incorrect_id(self):
        # Given
        payload = {
        "salary": 55000.0,
        "zipcode": 11111,
        "credit_score": 695,
        "monthly_debt": 1100.0,
        "downpayment_savings": 10000.0,
        "downpayment_percentage": 10.0,
        "rent": 1800.0,
        "goal_principal": 0.0
        }

        report_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = report_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/report/{new_id}'
        # When
        incorrect_id_response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
        #Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual("Does Not Exist Error",body['error'])
        self.assertEqual("Please check your request, the Report record given id doesn't exist", body['message'])

# POST
    def test_unsuccessful_update_report_incorrect_id(self):
        payload = {
        "salary": 55000.0,
        "zipcode": 11111,
        "credit_score": 695,
        "monthly_debt": 1100.0,
        "downpayment_savings": 10000.0,
        "downpayment_percentage": 10.0,
        "rent": 1800.0,
        "goal_principal": 0.0
        }

        report_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
#Given
#When
#Then

# UPDATE
#Given
#When
#Then

# DESTROY
#Given
#When
#Then
