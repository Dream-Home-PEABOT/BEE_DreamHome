from flask import Response, request
from api.models.median_home_value import MedianHomeValue
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
import pry


class MedianHomeValueController():
    def add_median_home_value(self):
        try:
            body = request.get_json()
            median_home = MedianHomeValue(**body)
            median_home.save()
            id = median_home.id
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": 'To see this new record, please do a GET request using the url',
                        "url": f'/api/v1/median-house-value/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("This Median House Value record's classification already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Median House Value documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500

    # def get_median_home_value(self, id):

    # def all_median_home_value(self):
    # def update_median_home_value(self, id):
    # def destroy_median_home_value(self, id):
medianhomevaluecontroller = MedianHomeValueController()
