import requests
import json
import pry
import os

def zip_to_location(zip):
    # api_key = os.environ.get('ZIP_LOCATION_API_KEY')
    # format = 'json'
    # units = 'degrees'
    # url = f'http://www.zipcodeapi.com/rest/{api_key}/info.{format}/{zip}/{units}'
    #
    # response = requests.get(url)
    # if response.status_code == 404:
    #     return 'Denver, CO'
    #
    # json_response = json.loads(response.text)
    # city = json_response['city']
    # state = json_response['state']
    # return f'{city}, {state}'

    # UNTIL YOU MOCK THE BEHAVIOR ABOVE
    return 'San Antonio, TX'

def zip_to_avg_home(zip):
    return 350000
