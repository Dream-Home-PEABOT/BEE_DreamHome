from flask import Response, request, render_template
from api.models.home_insurance import HomeInsurance
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from re import sub
import pry

class HomeInsuranceController():
    #POST
    def add_insurance(self):
        # try:
        body = request.get_json()
        pry()
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

homeinsurancecontroller = HomeInsuranceController()
