from flask import Response, request
from api.models.median_home_value import MedianHomeValue
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError


class MedianHomeValueController():
    # CREATE
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
                        "url": f'/api/v1/median-home-value/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("This Median House Value record's classification already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Median House Value documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500

    # READ by ID
    def get_median_home_value(self, id):
        try:
            median_home = MedianHomeValue.objects.get(id=id)
            return {
                "data": {
                    "type": str(median_home),
                    "id": str(median_home.id),
                    "attributes": {
                        "year": median_home.year,
                        "state": median_home.state,
                        "avg_home_value": median_home.avg_home_value,
                        "median_top_tier": median_home.median_top_tier,
                        "median_single_family_value": median_home.median_single_family_value,
                        "median_bottom_tier": median_home.median_bottom_tier,
                        "median_condo_value": median_home.median_condo_value
                    }
                }
            }, 200
        except (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Median Home Value record with given id doesn't exist.")
        except Exception:
            raise 500

    # READ all
    def all_median_home_value(self):
        try:
            all_median_home_value = MedianHomeValue.objects()
            json_median_home_value_objects = {}
            for median_home_value in all_median_home_value:
                json_median_home_value_objects[f'home_value_of_{median_home_value.state.lower()}'] = {
                    "type": str(median_home_value),
                    "id": str(median_home_value.id),
                    "attributes": {
                        "year": median_home_value.year,
                        "state": median_home_value.state,
                        "avg_home_value": median_home_value.avg_home_value,
                        "median_top_tier": median_home_value.median_top_tier,
                        "median_single_family_value": median_home_value.median_single_family_value,
                        "median_bottom_tier": median_home_value.median_bottom_tier,
                        "median_condo_value": median_home_value.median_condo_value
                    }
                }
            return { "data": json_median_home_value_objects}, 200
        except Exception:
            raise 500

    # UPDATE
    def update_median_home_value(self, id):
        try:
            median_home_value = MedianHomeValue.objects.get(id=id)
            body = request.get_json()
            median_home_value.update(**body)
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": "To see this record's updated response, please do a GET request using the url",
                        'url': f'/api/v1/median-home-value/{id}'
                    }
                }
            }, 202
        except (InvalidQueryError, FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Median Home Value documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Median Home Value record with given id doesn't exist.")
        except Exception:
            raise 500

    # DESTROY
    def destroy_median_home_value(self, id):
        try:
            median_home_value = MedianHomeValue.objects.get(id=id)
            median_home_value.delete()
            return {
                "data": {
                    "id": 'nil',
                    "confirmation": {
                        "info": "To see this record's deletion response, please do a GET request using the url",
                        "url": f'/api/v1/median-home-value/{id}'
                    }
                }
            }, 202
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Median Home Value record with given id doesn't exist.")
        except Exception:
            raise 500

medianhomevaluecontroller = MedianHomeValueController()
