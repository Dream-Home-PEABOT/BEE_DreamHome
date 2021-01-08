import pry
import json
from tests.BaseCase import BaseCase

class TestRecordCrud(BaseCase):
    # CREATE
    def test_successful_post_record(self):
        # Given
        payload = {
          "salary": 55000,
          "zipcode": 11111,
          "credit": 695,
          "monthly_debt": 1100,
          "downpayment_savings": 10000,
          "downpayment_percentage": 10,
          "rent": 1800,
          "goal_principal": 0
        }
        # When
        response = self.app.post('/api/v1/record', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/record/{id}'

        response = self.app.get(url, hearders={'Content-Type': "application/json"})

        body = response.json['data']
        pry()

        # Then
        self.assertEqual(200, response.status_code)
    # UPDATE
    # Given
    # When
    # Then

    # DESTROY
    # Given
    # When
    # Then
