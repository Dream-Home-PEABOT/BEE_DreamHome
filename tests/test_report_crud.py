import pry
import json
from tests.BaseCase import BaseCase
from database.report import pragmatic, imaginative

class TestReportCrud(BaseCase):
    # GET single
    # def test_successful_get_record(self):
    #     # Given
    #     payload = {
    #     "salary": 55000.0,
    #     "zipcode": 11111,
    #     "credit_score": 695,
    #     "monthly_debt": 1100.0,
    #     "downpayment_savings": 10000.0,
    #     "downpayment_percentage": 10.0,
    #     "rent": 1800.0,
    #     "goal_principal": 0.0
    #     }
    #
    #     response1 = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    #     id = response1.json['data']['id']
    #     url = f'/api/v1/report/{id}'
    #
    #     # When
    #     get_response = self.app.get(url, headers={"Content-Type": "application/json"})
    #     # Then
    #     self.assertEqual(200, get_response.status_code)
    #     # self.assertEqual(id, )

    # GET all
    def test_get_all_only_delivers_ids(self):
        # Given
        self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(pragmatic))
        self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(imaginative))

        # When
        response = self.app.get('/api/v1/report', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)

    # CREATE
    # def test_successful_post_record(self):
    #     # Given
    #     payload = {
    #       "salary": 55000.0,
    #       "zipcode": 11111,
    #       "credit_score": 695,
    #       "monthly_debt": 1100.0,
    #       "downpayment_savings": 10000.0,
    #       "downpayment_percentage": 10.0,
    #       "rent": 1800.0,
    #       "goal_principal": 0.0
    #     }
    #     # When
    #     response1 = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    #     id = response1.json['data']['id']
    #     url = f'/api/v1/report/{id}'
    #
    #     response2 = self.app.get(url, headers={'Content-Type': "application/json"})
    #
    #     body = response1.json
    #
    #     # Then
    #     self.assertEqual(201, response1.status_code)
    #     self.assertEqual(str, type(id))
    #
    #
    # # PUT
    # def test_successful_update_report(self):
    # # Given
    #     payload = {
    #         "salary": 55000.0,
    #         "zipcode": 11111,
    #         "credit_score": 695,
    #         "monthly_debt": 1100.0,
    #         "downpayment_savings": 10000.0,
    #         "downpayment_percentage": 10.0,
    #         "rent": 1800.0,
    #         "goal_principal": 0.0
    #     }
    #     create_report = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    #     id = create_report.json['data']['id']
    #     url = f'/api/v1/report/{id}'
    # # When
    #     updated_payload = {
    #         "salary": 150000.0,
    #         "zipcode": 80016,
    #         "credit_score": 500
    #     }
    #     response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
    #     confirmation_url = response.json['data']['confirmation']['url']
    #
    # # Then
    #     confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
    #     confirmation_body = confirmation.json['data']['attributes']['input']
    #     self.assertEqual(202, response.status_code)
    #     self.assertEqual(updated_payload['salary'], confirmation_body['salary'])
    #     self.assertEqual(updated_payload['zipcode'], confirmation_body['zipcode'])
    #     self.assertEqual(updated_payload['credit_score'], confirmation_body['credit_score'])
    #     # self.assertNotEqual(payload, confirmation_body)
    #
    #     # DESTROY
    # def test_successful_delete_report(self):
    #     # Given
    #     payload = {
    #         "salary": 55000.0,
    #         "zipcode": 11111,
    #         "credit_score": 695,
    #         "monthly_debt": 1100.0,
    #         "downpayment_savings": 10000.0,
    #         "downpayment_percentage": 10.0,
    #         "rent": 1800.0,
    #         "goal_principal": 0.0
    #     }
    #
    #     create_report = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    #     id = create_report.json['data']['id']
    #     url = f'/api/v1/report/{id}'
    #
    #     # When
    #     delete_report = self.app.delete(url, headers={"Content-Type": "application/json"})
    #     body = delete_report.json['data']
    #     # Then
    #     self.assertEqual('nil', body['id'])
    #     # Once you have error handling done, the following can be tested
    #         # confirmation = self.app.get(url, headers={"Content-Type": "application/json"})
    #         # confirmation_body = confirmation.json
