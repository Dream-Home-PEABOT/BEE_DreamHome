import json
from tests.BaseCase import BaseCase
from database.education import salary, zip, debt, savings, credit, percent, term, rent, principal


class TestEducationCrud(BaseCase):
    # CREATE -----------------------------------------------------------
    def test_successful_post_education(self):
    # Given
        payload = {
            "classification": "Testing Classification",
            "question": "Testing Question",
            "description": "Testing Description",
            "information": "Testing Information",
            "note": "Testing Note",
            "source": "Testing Source",
            "order": 1
        }
    # When
        response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/education/{id}'
    # Then
        self.assertEqual(201, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['02_id'])
        self.assertEqual(payload['order'], body['03_attributes']['A_order'])
        self.assertEqual('', body['03_attributes']['H_symbol'])
        self.assertEqual(payload['classification'], body['03_attributes']['B_classification'])
        self.assertEqual(payload['note'], body['03_attributes']['F_note'])

    # READ by ID -----------------------------------------------------------
    def test_successful_get_education(self):
    # Given
        create_salary = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(salary))
        create_zip = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(zip))
        post_zip_data = create_zip.json['data']

        salary_id = create_salary.json['data']['id']
        salary_url = f'/api/v1/education/{salary_id}'
    # When
        salary_get_response = self.app.get(salary_url, headers={"Content-Type": "application/json"})
        get_salary_data = salary_get_response.json['data']
    # Then
        self.assertEqual(200, salary_get_response.status_code)
        self.assertEqual(salary_id, get_salary_data['02_id'])
        self.assertNotEqual(salary_id, post_zip_data['id'])
        self.assertEqual(salary['order'], get_salary_data['03_attributes']['A_order'])
        self.assertEqual(salary['question'], get_salary_data['03_attributes']['C_question'])
        self.assertEqual(salary['information'], get_salary_data['03_attributes']['E_information'])

    # READ all -----------------------------------------------------------
    def test_successful_get_all_education(self):
    # Given
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(salary))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(zip))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(debt))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(credit))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(percent))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(term))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(rent))
        self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(principal))
    # When
        response = self.app.get('/api/v1/education', headers={"Content-Type": "application/json"})
        body = response.json['data']
        returned_salary = body['monthly_salary']
        returned_zip = body['zip_code']
        returned_debt = body['monthly_debt']
        returned_savings = body['downpayment_savings']
        returned_credit = body['credit_score']
        returned_percent = body['downpayment_percentage']
        returned_term = body['mortgage_term']
        returned_rent = body['rent']
        returned_principal = body['goal_home_price']
    # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(9, len(body))
        self.assertEqual(salary['classification'], returned_salary['03_attributes']['B_classification'])
        self.assertEqual(zip['classification'], returned_zip['03_attributes']['B_classification'])
        self.assertEqual(debt['classification'], returned_debt['03_attributes']['B_classification'])
        self.assertEqual(savings['classification'], returned_savings['03_attributes']['B_classification'])
        self.assertEqual(credit['classification'], returned_credit['03_attributes']['B_classification'])
        self.assertEqual(percent['classification'], returned_percent['03_attributes']['B_classification'])
        self.assertEqual(term['classification'], returned_term['03_attributes']['B_classification'])
        self.assertEqual(rent['classification'], returned_rent['03_attributes']['B_classification'])
        self.assertEqual(principal['classification'], returned_principal['03_attributes']['B_classification'])

    # UPDATE -----------------------------------------------------------
    def test_successful_put_education(self):
    # Given
        payload = {
            "classification": "Testing Classification",
            "question": "Testing Question",
            "description": "Testing Description",
            "information": "Testing Information",
            "note": "Testing Note",
            "source": "Testing Source",
            "symbol": "Testing Symbol",
            "order": 1
        }
        create_education = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_education.json['data']['id']
        url = f'/api/v1/education/{id}'
    # When
        updated_payload = {
            "classification": "UPDATED Classification",
            "description": "UPDATED Description",
            "information": "UPDATED Information",
            "note": "UPDATED Note",
            "source": "UPDATED Source"
        }
        response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(updated_payload))
        confirmation_url = response.json['data']['confirmation']['url']
    # Then
        confirmation = self.app.get(confirmation_url, headers={"Content-Type": "application/json"})
        confirmation_body = confirmation.json['data']['03_attributes']
        self.assertEqual(202, response.status_code)
        self.assertEqual(updated_payload['classification'], confirmation_body['B_classification'])
        self.assertNotEqual(payload['classification'], confirmation_body['B_classification'])
        self.assertEqual(updated_payload['description'], confirmation_body['D_description'])
        self.assertNotEqual(payload['description'], confirmation_body['D_description'])
        self.assertEqual(updated_payload['information'], confirmation_body['E_information'])
        self.assertNotEqual(payload['information'], confirmation_body['E_information'])
        self.assertEqual(updated_payload['note'], confirmation_body['F_note'])
        self.assertNotEqual(payload['note'], confirmation_body['F_note'])
        self.assertEqual(updated_payload['source'], confirmation_body['G_source'])
        self.assertNotEqual(payload['source'], confirmation_body['G_source'])
        # This is a field that wasn't updated, so it only tests the final response against the original creation
        self.assertEqual(payload['question'], confirmation_body['C_question'])

    # DESTROY -----------------------------------------------------------
    def test_successful_delete_education(self):
    # Given
        payload = {
            "classification": "Testing Classification",
            "question": "Testing Question",
            "description": "Testing Description",
            "information": "Testing Information",
            "note": "Testing Note",
            "source": "Testing Source",
            "symbol": "Testing Symbol",
            "order": 1
        }
        create_education = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = create_education.json['data']['id']
        url = f'/api/v1/education/{id}'
    # When
        delete_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        data = delete_response.json['data']
    # Then
        self.assertEqual(202, delete_response.status_code)
        self.assertEqual('nil', data['id'])
        self.assertNotEqual(id, data['id'])
        self.assertEqual("To see this record's deletion response, please do a GET request using the url", data['confirmation']['info'])
        self.assertEqual(url, data['confirmation']['url'])
    # Confirm with GET by ID
        confirmation = self.app.get(url, headers={"Content-Type": "application/json"})
        confirmation_data = confirmation.json['data']
        self.assertEqual('Does Not Exist Error', confirmation_data['error'])
        self.assertEqual("Please check your request, the Education record with given id doesn't exist.", confirmation_data['message'])
