import pry
import json
from tests.BaseCase import BaseCase
from database.pmi import downpayment_zero, downpayment_five, downpayment_ten, downpayment_fifteen

class TestPmiCrud(BaseCase):
    # POST
    def test_successful_post_pmi(self):
        # Given
        payload = {
            "downpayment_percentage": 0,
            "from_620_639": 2.25,
            "from_640_659": 2.05,
            "from_660_679": 1.90,
            "from_680_699": 1.4,
            "from_700_719": 1.15,
            "from_720_739": 0.95,
            "from_740_759": 0.75,
            "from_760_850": 0.55,
        }
        # When
        response = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(payload))
        id = response.json['data']['id']
        url = f'/api/v1/pmi/{id}'
        # Then
        self.assertEqual(200, response.status_code)

        get_pmi = self.app.get(url, headers={"Content-Type": "application/json"})
        body = get_pmi.json['data']

        self.assertEqual(id, body['id'])
        self.assertEqual(payload, body['attributes'])

# GET single
    # def test_successful_get_pmi(self):
# Given
        # create_downpayment_0 = self.app.post('/api/v1/pmi', headers={"Content-Type": "application/json"}, data=json.dumps(downpayment_zero))
        # pry()
# When
# Then



# Get all
# Given
# When
# Then
# PUT
# Given
# When
# Then
# DESTROY
# Given
# When
# Then
