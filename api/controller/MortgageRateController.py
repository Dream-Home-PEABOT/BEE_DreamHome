from flask import Response, request
from api.models.mortgage_rate import MortgageRate
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
from re import sub
import pry

class MortgageRateController():

    #single GET
    def get_mortgage_rate(self, id):
        try:
            mortgage_rate = MortgageRate.objects.get(id=id)
            return {
                "data": {
                    "type": str(mortgage_rate),
                    "id": str(mortgage_rate.id),
                    "attributes": {
                        "credit_score_floor": mortgage_rate.credit_score_floor,
                        "credit_score_ceiling": mortgage_rate.credit_score_ceiling,
                        "rate": mortgage_rate.rate
                    }
                }
            }, 200
        except  (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Home Insurance record with given id doesn't exist.")
        except Exception:
            raise 500
    #POST
    def add_mortgage_rate(self):
        try:
            body = request.get_json()
            mortgage_rate = MortgageRate(**body)
            mortgage_rate.save()
            id = mortgage_rate.id
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": 'To see this new record, please do a GET request using the url',
                        "url": f'/api/v1/mortgage_rate/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("This insurance record's classification already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500
    #PUT
    def update_mortgage_rate(self, id):
        try:
            mortgage_rate = MortgageRate.objects.get(id=id)
            body = request.get_json()
            mortgage_rate.update(**body)
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": "To see this record's update response, please do a GET request using the url",
                        "url": f'/api/v1/mortgage_rate/{id}'
                    }
                }
            }, 202
        except (InvalidQueryError, FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Home Insurance documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Insurance record with given id doesn't exist.")
        except Exception:
            raise 500
    #GET all
    def all_mortgage_rate(self):
        try:
            all_mortgage_rates = MortgageRate.objects()

            def convert_snake(string):
                return '_'.join(
                sub('([A-Z][a-z]+)', r' \1',
                sub('([A-Z]+)', r' \1',
                string.replace('-', ' '))).split()).lower()

            json_mortgage_rate_objects = {}
            for mortgage_rate in all_mortgage_rates:
                json_mortgage_rate_objects[convert_snake(f'range_{mortgage_rate.credit_score_floor}_{mortgage_rate.credit_score_ceiling}')] = {
                    "type": str(mortgage_rate),
                    "id": str(mortgage_rate.id),
                    "attributes": {
                        "rate": mortgage_rate.rate,
                        "credit_score_ceiling": mortgage_rate.credit_score_ceiling,
                        "credit_score_floor": mortgage_rate.credit_score_floor
                    }
                }

            return {"data": json_mortgage_rate_objects}, 200
        except Exception:
            raise 500
    #DELETE
    def destroy_mortgage_rate(self, id):
        try:
            mortgage_rate = MortgageRate.objects.get(id=id)
            mortgage_rate.delete()
            return {
                "data": {
                    "id": 'nil',
                    "confirmation": {
                        "info": "To see this record's deletion response, please do a GET request using the url",
                        "url": f'/api/v1/mortgage_rate/{id}'
                    }
                }
            }, 204
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Mortgage Rate record with given id doesn't exist.")
        except Exception:
            raise 500
mortgageratecontroller = MortgageRateController()
