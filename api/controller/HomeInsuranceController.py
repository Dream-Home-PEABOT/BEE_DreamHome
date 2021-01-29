from flask import Response, request, render_template
from api.models.home_insurance import HomeInsurance
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
from re import sub


class HomeInsuranceController():
    # single GET
    def get_insurance(self, id):
        try:
            insurance = HomeInsurance.objects.get(id=id)
            return {
                "data": {
                    "type": str(insurance),
                    "id": str(insurance.id),
                    "attributes": {
                        "state": insurance.state,
                        "annual_average_insurance_rate": insurance.annual_average_insurance_rate
                    }
                }
            }, 200
        except  (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Home Insurance record with given id doesn't exist.")
        except Exception:
            raise 500

    #POST
    def add_insurance(self):
        try:
            body = request.get_json()
            home_insurance = HomeInsurance(**body)
            home_insurance.save()
            id = home_insurance.id
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": 'To see this new record, please do a GET request using the url',
                        "url": f'/api/v1/home-insurance/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("This insurance record's classification already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500

    # GET all
    def all_insurance(self):
        try:
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
                        "annual_average_insurance_rate": homeinsurance.annual_average_insurance_rate
                    }
                }

            return {"data": json_home_insurance_objects}, 200
        except Exception:
            raise 500

    # PUT
    def update_insurance(self, id):
        try:
            home_insurance = HomeInsurance.objects.get(id=id)
            body = request.get_json()
            home_insurance.update(**body)
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": "To see this record's update response, please do a GET request using the url",
                        "url": f'/api/v1/home-insurance/{id}'
                    }
                }
            }, 202
        except (InvalidQueryError, FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Insurance record with given id doesn't exist.")
        except Exception:
            raise 500

    # DESTROY
    def destroy_insurance(self, id):
        try:
            home_insurance = HomeInsurance.objects.get(id=id)
            home_insurance.delete()
            return {
                "data": {
                    "id": 'nil',
                    "confirmation": {
                        "info": "To see this record's deletion response, please do a GET request using the url",
                        "url": f'/api/v1/home-insurance/{id}'
                    }
                }
            }, 204
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Insurance record with given id doesn't exist.")
        except Exception:
            raise 500
homeinsurancecontroller = HomeInsuranceController()
