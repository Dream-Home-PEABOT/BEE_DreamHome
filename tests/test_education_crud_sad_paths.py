from tests.BaseCase import BaseCase
from database.education import savings
import json
import pry


class TestEducationCrudSadPath(BaseCase):
    def ReplaceStringByIndex(self, text, index = 0, end_index = 1, replacement = ''):
        return '%s%s%s'%(text[:index], replacement, text[end_index:])

    # GET single
    def test_unsuccessful_get_by_id_education_incorrect_id(self):
        # Given
        savings_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))

        id = savings_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/education/{new_id}'

        # When
        incorrect_id_response = self.app.get(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']

        # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Education record with given id doesn't exist.", body['message'])

    # PUT
    def test_unsuccessful_update_education_incorrect_id(self):
        # Given
        savings_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))

        id = savings_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/education/{new_id}'

        # When
        incorrect_id_response = self.app.put(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']

        # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Education record with given id doesn't exist.", body['message'])

    def test_unsuccessful_update_education_bad_fields(self):
        # Given
        savings_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))

        id = savings_response.json['data']['id']
        url = f'/api/v1/education/{id}'

        # When
        extra_field_payload = {
            "bad_attribute": "Oops",
            "classification": "Classification",
            "question": "Question",
            "description": "Description",
            "information": "Information",
            "note": "Note",
            "source": "Source"
        }
        bad_field_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = bad_field_response.json['data']

        # Then
        self.assertEqual(406, bad_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Education documentation. Request is missing a required field or incorrect field entered.", body['message'])

    # DESTROY
    def test_unsuccessful_delete_education_incorrect_id(self):
        # Given
        savings_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))

        id = savings_response.json['data']['id']
        new_id = self.ReplaceStringByIndex(id, 0, 5, '12345')
        url = f'/api/v1/education/{new_id}'

        # When
        incorrect_id_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        body = incorrect_id_response.json['data']

        # Then
        self.assertNotEqual(id, new_id)
        self.assertEqual(400, incorrect_id_response.status_code)
        self.assertEqual('Does Not Exist Error', body['error'])
        self.assertEqual("Please check your request, the Education record with given id doesn't exist.", body['message'])

    # POST
    def test_unsuccessful_post_education_not_unique(self):
        # Given
        initial_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))

        # When
        error_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(savings))
        body = error_response.json['data']

        # Then
        self.assertEqual(400, error_response.status_code)
        self.assertEqual('Not Unique Error', body['error'])
        self.assertEqual("This education record's classification already exists in the database", body['message'])

    def test_unsuccessful_post_education_extra_field_incorrect(self):
        # Given
        extra_field_payload = {
            "bad_attribute": "Oops",
            "classification": "Classification",
            "question": "Question",
            "description": "Description",
            "information": "Information",
            "note": "Note",
            "source": "Source"
        }

        # When
        extra_field_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(extra_field_payload))
        body = extra_field_response.json['data']

        # Then
        self.assertEqual(406, extra_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Education documentation. Request is missing a required field or incorrect field entered.", body['message'])

    def test_unsuccessful_post_education_field_incorrect(self):
        # Given
        incorrect_field_payload = {
            "classification": 7,
            "question": "Question",
            "description": "Description",
            "information": "Information",
            "note": "Note",
            "source": "Source"
        }

        # When
        incorrect_field_response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(incorrect_field_payload))
        body = incorrect_field_response.json['data']

        # Then
        self.assertEqual(406, incorrect_field_response.status_code)
        self.assertEqual('Schema Error', body['error'])
        self.assertEqual("Please check the Education documentation. Request is missing a required field or incorrect field entered.", body['message'])
