import pry
import json
from tests.BaseCase import BaseCase

class TestEducationCrud(BaseCase):
    # GET single

    # GET all
    def test_succssful_get_education(self):
        # Given
            # All done in setup, see education.py seed in database

        # When
        response = self.app.get('/api/v1/education', headers={"Content-Type": "application/json"})

        # Then
        self.assertEqual(200, response.status_code)

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
