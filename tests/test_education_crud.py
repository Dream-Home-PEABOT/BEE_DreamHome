import json
from tests.BaseCase import BaseCase

class TestEducationCrud(BaseCase):
    # GET single

    # GET all

    # POST
    def test_post_education_response(self):
        # Given
        payload = {
            "classification": "Annual Salary",
            "question": "What is your net monthly salary?",
            "description": "Gross income is the total amount you earn (typically over the course of a year) before expenses. Net income is the profit your business earns after expenses ",
            "information": "Depending on the home price you're aiming for, you may want to wait a year or two before you apply for a mortgage if you've just moved into a higher-paying role. The longer you stay in your higher-paying position, the more your lender may be willing to loan you.",
            "note":"The amount of money you earn plays a smaller role in getting a mortgage than you might think. ",
            "source": "https://www.rocketmortgage.com"
        }

        # When
        response = self.app.post('/api/v1/education', headers={"Content-Type": "application/json"}, data=json.dumps(payload))

        # Then
        self.assertEqual(200, response.status_code)

    # PUT

    # DESTROY
