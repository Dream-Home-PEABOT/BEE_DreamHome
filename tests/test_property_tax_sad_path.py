from tests.BaseCase import BaseCase
from database.property_tax import colorado
import json


class TestPropertyTaxCrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index=0, end_index=1, replacement=''):
        return '%s%s%s' % (text[:index], replacement, text[end_index:])

    # CREATE SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_post_property_tax_not_unique(self):
    # Given
        initial_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))
    # When
        error_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))
        body = error_response.json['data']
    # Then
        self.assertEqual(400, error_response.status_code)
        self.assertEqual('Not Unique Error', body['error'])
        self.assertEqual("This Tax record's classification already exists in the database", body['message'])

    def test_unsuccessful_post_property_tax_extra_field_incorrect(self):
    # Given
        extra_field_payload = {
            "bad_attribute": "Oops",
            "too_much_money": 10000000000,
            "what_is_this": "i_dont_even"
        }
    # When
        extra_field_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = extra_field_response.json['data']
    # Then
        self.assertEqual(406, extra_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Property Tax documentation. Request is missing a required field or incorrect field entered.", body['message'])

    def test_unsuccessful_post_property_tax_field_incorrect(self):
    # Given
        incorrect_field_payload = {
            "state": 79,
            "annual_average_insurance_rate": 1200
        }
    # When
        incorrect_field_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = incorrect_field_response.json['data']
    # Then
        self.assertEqual(406, incorrect_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Property Tax documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # READ by ID SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_get_by_id_property_tax_incorrect_id(self):
    # Given
        tax_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))

        id = tax_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/property_tax/{new_id}'
    # When
        incorrect_id_response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Property Tax record with given id doesn't exist.", body['message'])

    # UPDATE SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_put_property_tax_incorrect_id(self):
    # Given
        tax_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))

        id = tax_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/property_tax/{new_id}'
    # When
        incorrect_id_response = self.app.put(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Tax record with given id doesn't exist.", body['message'])

    def test_unsuccessful_put_property_tax_bad_fields(self):
    # Given
        tax_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))

        id = tax_response.json['data']['id']
        url = f'/api/v1/property_tax/{id}'
    # When
        extra_field_payload = {
            "bad_attribute": "Oops",
            "too_much_money": 10000000000
        }
        bad_field_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = bad_field_response.json['data']
    # Then
        self.assertEqual(406, bad_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Property Tax documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # DESTROY SAD PATHS -----------------------------------------------------------
    def test_unsuccessful_delete_property_tax_incorrect_id(self):
    # Given
        tax_response = self.app.post('/api/v1/property_tax', headers={"Content-Type": "application/json"}, data=json.dumps(colorado))

        id = tax_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/property_tax/{new_id}'
    # When
        incorrect_id_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']
    # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Tax record with given id doesn't exist.", body['message'])
