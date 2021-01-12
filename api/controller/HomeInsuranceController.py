from flask import Response, request, render_template
from api.models.home_insurance import HomeInsurance
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from re import sub
import pry

class HomeInsuranceController():
    # single GET
    def get_insurance(self, id):
        insurance = HomeInsurance.objects.get(id=id)
        return {
            "data": {
                "type": str(insurance),
                "id": str(insurance.id),
                "attributes": {
                    "state": insurance.state,
                    "average_rate": insurance.average_rate
                }
            }
        }, 200

    #POST
    def add_insurance(self):
        # try:
        body = request.get_json()
        home_insurance = HomeInsurance(**body)
        home_insurance.save()
        id = home_insurance.id
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": 'To see this new record, please do a GET request using the url',
                    "url": f'/api/v1/home_insurance/{id}'
                }
            }
        }, 200
    
    # GET all
    def all_insurance(self):
        all_insurance = HomeInsurance.objects()

        def convert_snake(string):
            return '_'.join(
            sub('([A-Z][a-z]+)', r' \1',
            sub('([A-Z]+)', r' \1',
            string.replace('-', ' '))).split()).lower()

        json_home_insurance_objects = {}
        for homeinsurance in all_insurance:
            json_home_insurance_objects[convert_snake(homeinsurance.state)] = {
                "type": str(homeinsurance),
                "id": str(homeinsurance.id),
                "attributes": {
                    "state": homeinsurance.state,
                    "average_rate": homeinsurance.average_rate
                }
            }

        return {"data": json_home_insurance_objects}, 200

    # PUT
    def update_insurance(self, id):
        home_insurance = HomeInsurance.objects.get(id=id)
        body = request.get_json()
        home_insurance.update(**body)
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": "To see this record's update response, please do a GET request using the url",
                    "url": f'/api/v1/home_insurance/{id}'
                }
            }
        }, 200

    # DESTROY
    def destroy_insurance(self, id):
        home_insurance = HomeInsurance.objects.get(id=id)
        home_insurance.delete()
        return {
            "data": {
                "id": 'nil',
                "confirmation": {
                    "info": "To see this record's deletion response, please do a GET request using the url",
                    "url": f'/api/v1/home_insurance/{id}'
                }
            }
        }, 200
homeinsurancecontroller = HomeInsuranceController()
