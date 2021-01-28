import pry
import json
from tests.BaseCase import BaseCase

class TestUserCrud(BaseCase):
    # CREATE ---------------------------------------------------
    def test_successful_post_user_registration(self):
    # Given
        email = "email@email.com"
        uid = "rajnerfiojcfiojreeroijqoie5rty6309"
        name = "Sam"
        payload = {
            "email": email,
            "uid": uid,
            "name": name
        }
    # When
        registration_response = self.app.post('/api/v1/registration', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
    # Then
        # - assert status code is 201
        self.assertEqual(201, registration_response.status_code)
        # - save response.json['data'] AS local variable "data"
        data = registration_response.json['data']
        # - assert data['confirmation']['info'] is equal to 'To see this new user, please do a GET request using the url'
        self.assertEqual(data['confirmation']['info'], 'To see this new user, please do a GET request using the url')
        # - save local variable "url" AS f'/api/v1/user/{data['id']}'
        url 
        # - assert data['confirmation']['url'] is equal to "url"
        # - If possible - call the db directly and see the last user object saved. Can you match that id to data['id']

    # Confirm with GET by ID
        - make a "confirmation" local variable that is making a GET request to the "url" from above
        - assert status code is 200
        - assert name matches payload
        - assert id matches body['id']
        - assert email matches payload
        - assert uid IS NOT RETURNED (can we look into our unittest assertion docs and see if we can check for hash keys or something)
