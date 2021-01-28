import json
from tests.BaseCase import BaseCase


class TestReportCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post_record(self):
    # Given
        payload = {
            "zipcode": 60654,
            "credit_score": 617,
            "salary": 3000,
            "monthly_debt": 1100,
            "downpayment_savings": 1000,
            "mortgage_term": 30,
            "downpayment_percentage": 10,
            "goal_principal": 0,
            "rent": 1800
        }
    # When
        post_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = post_response.json['data']['id']
        url = f'/api/v1/report/{id}'
        data = post_response.json['data']
    # Then
        self.assertEqual(201, post_response.status_code)
        self.assertEqual(id, data['id'])
        self.assertEqual('To connect this report to a user in the future, save this url with the client', data['confirmation']['info'])
        self.assertEqual(url, data['confirmation']['url'])
    # Confirm with GET by ID
        confirmation = self.app.get(url, headers={'Content-Type': "application/json"})
        self.assertEqual(200, confirmation.status_code)

    # READ by ID -----------------------------------------------------------
    def test_successful_get_record(self):
    # Given
        payload = {
            "zipcode": 78230,
            "credit_score": 701,
            "salary": 4500,
            "monthly_debt": 1500,
            "downpayment_savings": 30000,
            "mortgage_term": 30,
            "downpayment_percentage": 20,
            "goal_principal": 450000,
            "rent": 0
        }
        post_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = post_response.json['data']['id']
        url = f'/api/v1/report/{id}'
    # When
        get_response = self.app.get(url, headers={"Content-Type": "application/json"})
        data = get_response.json['data']
        input = data['03_attributes']['input']
        location = data['03_attributes']['output']['A_location']
        principal = data['03_attributes']['output']['B_principal']
        monthly = data['03_attributes']['output']['C_monthly']
        downpayment = data['03_attributes']['output']['D_downpayment']
    # Then
        self.assertEqual(200, get_response.status_code)
        self.assertEqual(id, data['02_id'])
        self.assertEqual(payload['zipcode'], input['A_zipcode'])
        self.assertEqual('San Antonio, TX', location['city_state'])
        self.assertEqual(0, principal['principal_based_on_rent'])
        self.assertEqual(payload['goal_principal'], principal['goal_principal'])
        self.assertEqual(float, type(monthly['monthly_principal']))
        self.assertEqual(0.2, downpayment['plan_style']['min_savings_plan']['savings_style_percentage'])

    # UPDATE -----------------------------------------------------------
    def test_successful_post_report(self):
    # Given
        payload = {
            "zipcode": 60654,
            "credit_score": 617,
            "salary": 3000,
            "monthly_debt": 1100,
            "downpayment_savings": 1000,
            "mortgage_term": 30,
            "downpayment_percentage": 10,
            "goal_principal": 0,
            "rent": 1800
        }
        create_report = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_report.json['data']['id']
        url = f'/api/v1/report/{id}'
    # When
        updated_payload = {
            "salary": 3500,
            "zipcode": 60651,
            "credit_score": 640
        }
        update_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        data = update_response.json['data']
    # Then
        self.assertEqual(202, update_response.status_code)
        self.assertEqual(id, data['id'])
        self.assertEqual("To see this record's update response, please do a GET request using the url", data['confirmation']['info'])
        self.assertEqual(url, data['confirmation']['url'])
    # Confirm with GET by ID
        confirmation = self.app.get(url, headers={"Content-Type": "application/json"})
        confirmation_data = confirmation.json['data']['03_attributes']['input']
        self.assertEqual(updated_payload['zipcode'], confirmation_data['A_zipcode'])
        self.assertEqual(updated_payload['credit_score'], confirmation_data['B_credit_score'])
        self.assertEqual(updated_payload['salary'], confirmation_data['C_salary'])
        self.assertNotEqual(payload, confirmation_data)

    # DESTROY -----------------------------------------------------------
    def test_successful_delete_report(self):
    # Given
        payload = {
            "zipcode": 78230,
            "credit_score": 701,
            "salary": 4500,
            "monthly_debt": 1500,
            "downpayment_savings": 30000,
            "mortgage_term": 30,
            "downpayment_percentage": 20,
            "goal_principal": 450000,
            "rent": 0
        }
        create_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_response.json['data']['id']
        url = f'/api/v1/report/{id}'
    # When
        delete_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        data = delete_response.json['data']
    # Then
        self.assertEqual('nil', data['id'])
        self.assertNotEqual(id, data['id'])
        self.assertEqual("To see this record's deletion response, please do a GET request using the url", data['confirmation']['info'])
        self.assertEqual(url, data['confirmation']['url'])
    # Confirm with GET by ID
        confirmation = self.app.get(url, headers={"Content-Type": "application/json"})
        confirmation_data = confirmation.json['data']
        self.assertEqual('Does Not Exist Error', confirmation_data['error'])
        self.assertEqual("Please check your request, the Report record with given id doesn't exist.", confirmation_data['message'])
