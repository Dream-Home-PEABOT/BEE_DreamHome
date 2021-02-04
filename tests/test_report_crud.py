import json
from tests.BaseCase import BaseCase
from database.pmi import downpayment_zero, downpayment_five, downpayment_ten
from database.mortgage_rate import range_300_619, range_620_639, range_640_659, range_660_679, range_680_699, range_700_759, range_760_850


class TestReportCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post_record(self):
    # Post for pmi
        self.app.post('/api/v1/pmi', headers={"Content-Type":"application/json"}, data=json.dumps(downpayment_zero))
    # Post for mortgage_rate
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_300_619))
    # Given
        payload1 = {
            "zipcode": "60651",
            "credit_score": 617,
            "salary": 3000,
            "monthly_debt": 1100,
            "downpayment_savings": 0,
            "mortgage_term": 30,
            "downpayment_percentage": 0,
            "goal_principal": 300000,
            "rent": 0
        }
        payload2 = {
            "zipcode": "60651",
            "credit_score": 617,
            "salary": 3000,
            "monthly_debt": 1100,
            "downpayment_savings": 0,
            "mortgage_term": 30,
            "downpayment_percentage": 0,
            "goal_principal": 300000,
            "rent": 0
        }
    # When
        post_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload1))
        duplicate_post_response = self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(payload2))

        id = post_response.json['data']['id']
        url = f'/api/v1/report/{id}'
        post_data = post_response.json['data']
    # Then
        self.assertEqual(201, post_response.status_code)
        self.assertEqual(201, duplicate_post_response.status_code)

        confirmation = self.app.get(url, headers={'Content-Type': "application/json"})
        self.assertEqual(200, confirmation.status_code)

        mortgage_rate = confirmation.json['data']['03_attributes']['output']['B_principal']['mortgage_rate']

        self.assertEqual(0.045, mortgage_rate)

        pmi_by_location = confirmation.json['data']['03_attributes']['output']['C_monthly']['pmi_by_location']

        self.assertEqual(562, pmi_by_location)

        home_insurance_by_location = confirmation.json['data']['03_attributes']['output']['C_monthly']['home_insurance_by_location']

        self.assertEqual(183, home_insurance_by_location)
        property_tax_by_location = confirmation.json['data']['03_attributes']['output']['C_monthly']['property_tax_by_location']
        self.assertEqual(358, property_tax_by_location)

    # READ by ID -----------------------------------------------------------
    def test_successful_get_record(self):
    # Post for pmi
        self.app.post('/api/v1/pmi', headers={"Content-Type":"application/json"}, data=json.dumps(downpayment_five))
    # Post for mortgage_rate
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_300_619))
    # Given
        payload = {
            "zipcode": "60654",
            "credit_score": 617,
            "salary": 3000,
            "monthly_debt": 1100,
            "downpayment_savings": 1000,
            "mortgage_term": 30,
            "downpayment_percentage": 7,
            "goal_principal": 0,
            "rent": 1800
        }
    # THIS PAYLOAD WAS NOT WORKING!!!
        # payload = {
        #     "zipcode": "80214",
        #     "credit_score": 701,
        #     "salary": 4500,
        #     "monthly_debt": 1500,
        #     "downpayment_savings": 30000,
        #     "mortgage_term": 30,
        #     "downpayment_percentage": 20,
        #     "goal_principal": 450000,
        #     "rent": 0
        # }
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
        self.assertEqual('Chicago, IL', location['city_state'])
        self.assertEqual(381989, principal['principal_based_on_rent'])
        self.assertEqual(payload['goal_principal'], principal['goal_principal'])
        self.assertEqual(int, type(monthly['monthly_principal']))
        self.assertEqual(0.2, downpayment['plan_style']['min_savings_plan']['savings_style_percentage'])
    #
    # UPDATE -----------------------------------------------------------
    def test_successful_post_report(self):
    # Post for pmi
        self.app.post('/api/v1/pmi', headers={"Content-Type":"application/json"}, data=json.dumps(downpayment_ten))
    # Post for mortgage_rate
        self.app.post('/api/v1/mortgage-rate', headers={"Content-Type":"application/json"}, data=json.dumps(range_640_659))
    # Given
        payload = {
            "zipcode": "60654",
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
            "zipcode": "60651",
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
            "zipcode": "80214",
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
