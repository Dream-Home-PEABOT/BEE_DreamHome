from tests.BaseCase import BaseCase
from database.pmi import downpayment_zero
import json
import pry


class TestPMICrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index=0, end_index=1, replacement=''):
        return '%s%s%s' % (text[:index], replacement, text[end_index:])

    # CREATE SAD PATHS  -----------------------------------------------------------
    def test_unsuccessful_post_pmi_not_unique(self):
    # Given
        initial_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
    # When
        error_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        body = error_response.json['data']
    # Then
        self.assertEqual(400, error_response.status_code)
        self.assertEqual('Not Unique Error', body['error'])
        self.assertEqual("This PMI record's classification already exists in the database", body['message'])

    def test_unsuccessful_post_pmi_extra_field_incorrect(self):
    # Given
        extra_field_payload = {
            "downpayment_percentage": 0,
            "range_620_639": 'two point 59',
            "range_640_659": '2.05',
            "range_660_679": '1.90',
            "range_680_699": '1.4',
            "range_700_719": '1.15',
            "range_720_739": '0.95',
            "range_740_759": '0.75',
            "range_760_850": '0.55'
        }
    # When
        extra_field_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = extra_field_response.json['data']
    # Then
        self.assertEqual(406, extra_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the PMI documentation. Request is missing a required field or incorrect field entered.", body['message'])

    def test_unsuccessful_post_pmi_field_incorrect(self):
    # Given
        incorrect_field_payload = {
            "state": 79,
            "annual_average_insurance_rate": 1200
        }
    # When
        incorrect_field_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = incorrect_field_response.json['data']
    # Then
        self.assertEqual(406, incorrect_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the PMI documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # READ by ID SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_get_by_id_pmi_incorrect_id(self):
    # Given
        tax_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        id = tax_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/pmi/{new_id}'
    # When
        incorrect_id_response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the PMI record with given id doesn't exist.", body['message'])

    # UPDATE SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_update_pmi_incorrect_id(self):
    # Given
        tax_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        id = tax_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/pmi/{new_id}'
    # When
        incorrect_id_response = self.app.put(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the PMI record with given id doesn't exist.", body['message'])

    def test_unsuccessful_update_pmi_bad_fields(self):
    # Given
        tax_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        id = tax_response.json['data']['id']
        url = f'/api/v1/pmi/{id}'
    # When
        extra_field_payload = {
            "downpayment_percentage": 0,
            "range_620_639": 2.25,
            "range_640_659": 2.05,
            "range_660_679": 1.90,
            "range_680_699": 1.4,
            "range_700_719": 1.15,
            "range_720_739": 0.95,
            "range_740_759": 0.75,
            "range_760_850": 0.55,
            "and_one_more": 0.00
        }
        bad_field_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = bad_field_response.json['data']
    # Then
        self.assertEqual(406, bad_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Property PMI documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # DESTROY SAD PATHS  -----------------------------------------------------------
    def test_unsuccessful_delete_pmi_incorrect_id(self):
    # Given
        tax_response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        id = tax_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/pmi/{new_id}'
    # When
        incorrect_id_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the PMI record with given id doesn't exist.", body['message'])
