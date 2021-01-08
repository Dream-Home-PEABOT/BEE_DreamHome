import pry
import json
from tests.BaseCase import BaseCase
from database.education import salary, zip, debt, savings, credit, percent, term, rent, principal


class TestEducationCrud(BaseCase):
    # GET single
    def test_successful_get_education(self):
        # Given
        create_salary = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(salary))
        create_zip = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(zip))

        id = create_salary.json['data']['id']
        url = f'/api/v1/education/{id}'

        # When
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual(id, body['id'])
        self.assertNotEqual(id, create_zip.json['data']['id'])
        self.assertEqual(salary, body['attributes'])

    # GET all
    def test_succssful_get_education(self):
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
        returned_salary = body['annual_salary']
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
        self.assertEqual(salary, returned_salary['attributes'])
        self.assertEqual(zip, returned_zip['attributes'])
        self.assertEqual(debt, returned_debt['attributes'])
        self.assertEqual(savings, returned_savings['attributes'])
        self.assertEqual(credit, returned_credit['attributes'])
        self.assertEqual(percent, returned_percent['attributes'])
        self.assertEqual(term, returned_term['attributes'])
        self.assertEqual(rent, returned_rent['attributes'])
        self.assertEqual(principal, returned_principal['attributes'])

    # POST
    def test_successful_post_education(self):
        # Given
        payload = {
            "classification": "Testing Classification",
            "question": "Testing Question",
            "description": "Testing Description",
            "information": "Testing Information",
            "note": "Testing Note",
            "source": "Testing Source"
        }

        # When
        response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/education/{id}'

        # Then
        self.assertEqual(200, response.status_code)
        response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = response.json['data']
        self.assertEqual(id, body['id'])
        self.assertEqual(payload, body['attributes'])

    # PUT
    def test_successful_put_education(self):
        # Given
        payload = {
            "classification": "Testing Classification",
            "question": "Testing Question",
            "description": "Testing Description",
            "information": "Testing Information",
            "note": "Testing Note",
            "source": "Testing Source"
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
        confirmation_body = confirmation.json['data']['attributes']

        self.assertEqual(updated_payload['classification'], confirmation_body['classification'])
        self.assertNotEqual(payload['classification'], confirmation_body['classification'])

        # This is the only field that wasn't updated, so it only tests the final response against the original creation
        self.assertEqual(payload['question'], confirmation_body['question'])

        self.assertEqual(updated_payload['description'], confirmation_body['description'])
        self.assertNotEqual(payload['description'], confirmation_body['description'])

        self.assertEqual(updated_payload['information'], confirmation_body['information'])
        self.assertNotEqual(payload['information'], confirmation_body['information'])

        self.assertEqual(updated_payload['note'], confirmation_body['note'])
        self.assertNotEqual(payload['note'], confirmation_body['note'])

        self.assertEqual(updated_payload['source'], confirmation_body['source'])
        self.assertNotEqual(payload['source'], confirmation_body['source'])

        self.assertEqual(200, response.status_code)

    # DESTROY
