import json
import pry
from tests.BaseCase import BaseCase


class TestAuthorization(BaseCase):

    def test_get_report_by_user(self):
    #Given
        harry_uid = 'jhdfs783uy4ir98f7ygh2jeuwidsi8943yrih'

        harry_report = {
            "zipcode": 80209,
            "credit_score": 710,
            "salary": 5000,
            "monthly_debt": 1500,
            "downpayment_savings": 50000,
            "mortgage_term": 30,
            "downpayment_percentage": 20,
            "goal_principal": 500000,
            "rent": 0,
            "uid": harry_uid
        }
        self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(harry_report))

        ginny_uid = 'bdj857ytwgyurf897yughjjjw98d7yugh4b3ei'
        ginny_report = {
            "zipcode": 80209,
            "credit_score": 720,
            "salary": 8000,
            "monthly_debt": 2500,
            "downpayment_savings": 60000,
            "mortgage_term": 30,
            "downpayment_percentage": 10,
            "goal_principal": 600000,
            "rent": 0,
            "uid": ginny_uid
        }
        self.app.post('/api/v1/report', headers={"Content-Type": "application/json"}, data=json.dumps(ginny_report))
        #     - uid
    # #When
        harry_response = self.app.get('/api/v1/report/unique', headers={"Content-Type": "application/json"}, data=json.dumps(harry_uid))
        harry_data = harry_response.json['data']
    # #Then
        self.assertEqual(200, harry_response.status_code)
        self.assertEqual(harry_report['credit_score'], harry_data['03_attributes']['input']['B_credit_score'])
        self.assertNotEqual(ginny_report['credit_score'], harry_data['03_attributes']['input']['B_credit_score'])
        #  #when

        ginny_response = self.app.get('/api/v1/report/unique', headers={"Content-Type": "application/json"}, data=json.dumps(ginny_uid))
        ginny_data = ginny_response.json['data']
    # #Then
        self.assertEqual(200, ginny_response.status_code)
        self.assertEqual(ginny_report['credit_score'], ginny_data['03_attributes']['input']['B_credit_score'])
        self.assertNotEqual(harry_report['credit_score'], ginny_data['03_attributes']['input']['B_credit_score'])



    #unregistered user w/ report that registers AND UID ADDED
    #Given

    # unregistered user has already created a report w/o a uid
    #     - generate correct report
    #     - generate false report
    #
    # unregistered user registers
    #     -  local variable uid
    #
    # can put a uid to a correct report
    #
    # confirm correct report has uid and not false report
    # confirm using new route that will automatically search by uid api/v1/report/unique
    #     - find report matched to the uid
    #     - otherwise it'll return an error
    #         - this user does not have a report yet/assigned

    #When
    #Then
