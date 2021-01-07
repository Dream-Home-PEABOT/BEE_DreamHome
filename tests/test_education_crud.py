import pry
import json
from tests.BaseCase import BaseCase
from database.education import salary, zip, debt, savings, credit, percent, term, rent, principal


class TestEducationCrud(BaseCase):
    # GET single
    # def test_successful_get_education(self, id):

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

        # Then
        self.assertEqual(200, response.status_code)

    # PUT

    # DESTROY
