import json
from tests.BaseCase import BaseCase
from database.pmi import downpayment_zero, downpayment_five, downpayment_ten, downpayment_fifteen
from database.mortgage_rate import range_300_619, range_620_639, range_640_659, range_660_679, range_680_699, range_700_759, range_760_850
from database.home_insurance import illinois, colorado
hi_il_insurance = illinois
hi_co_insurance = colorado
import pry
from database.median_home_value import illinois
mhv_illinois = illinois
from database.property_tax import illinois, colorado
from database.median_home_value import florida

class TestMedianHomeCrud(BaseCase):
    def test_successful_post(self):
    # Given
        # florida payload off in line 12
    # When
        response = self.app.post('/api/v1/median-home-value', headers={"Content-Type": "application/json"}, data=json.dumps(florida))
        id = response.json['data']['id']
        url = f'/api/v1/median-home-value/{id}'

        get_response = self.app.get(url, headers={"Content-Type": "application/json"})
        all_response = self.app.get('/api/v1/median-home-value', headers={"Content-Type": "application/json"})
        pry()

        payload = {
            "year": 2021
        }
        update_response = self.app.put(url, headers={"Content-Type": "application/json"}, data=json.dumps(payload))



        delete_response = self.app.delete(url, headers={"Content-Type": "application/json"})
        pry()
    # Then
