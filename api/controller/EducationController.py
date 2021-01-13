from flask import Response, request, render_template
from api.models.education import Education
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
from re import sub
import pry

class EducationController():
    # GET single
    def get_education(self, id):
        try:
            education = Education.objects.get(id=id)
            return {
                "data": {
                    "type": str(education),
                    "id": str(education.id),
                    "attributes": {
                        "classification": education.classification,
                        "question": education.question,
                        "description": education.description,
                        "information": education.information,
                        "note": education.note,
                        "source": education.source
                    }
                }
            }, 200
        except (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Education record with given id doesn't exist.")
        except Exception:
            raise 500

    # GET all
    def index(self):
        try:
            all_education = Education.objects()

            def convert_snake(string):
                return '_'.join(
                    sub('([A-Z][a-z]+)', r' \1',
                    sub('([A-Z]+)', r' \1',
                    string.replace('-', ' '))).split()).lower()



            json_education_objects = {}

            for education in all_education:
                json_education_objects[convert_snake(education.classification)] = {
                    "type": str(education),
                    "id": str(education.id),
                    "attributes": {
                        "classification": education.classification,
                        "question": education.question,
                        "description": education.description,
                        "information": education.information,
                        "note": education.note,
                        "source": education.source
                    }
                }

            return {"data": json_education_objects}, 200
        except Exception:
            raise 500

    # POST
    def add_education(self):
        try:
            body = request.get_json()
            education = Education(**body)
            education.save()
            id = education.id
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": 'To see this new record, please do a GET request using the url',
                        "url": f'/api/v1/education/{id}'
                    }
                }
            }, 201
        except NotUniqueError:
            raise APINotUniqueError("This education record's classification already exists in the database")
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Education documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500

    # PUT
    def update_education(self, id):
        try:
            education = Education.objects.get(id=id)
            body = request.get_json()
            education.update(**body)
            return {
                "data": {
                    "id": str(id),
                    "confirmation": {
                        "info": "To see this record's update response, please do a GET request using the url",
                        "url": f'/api/v1/education/{id}'
                    }
                }
            }, 200
        except (InvalidQueryError, FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Education documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Education record with given id doesn't exist.")
        except Exception:
            raise 500

    # DESTROY
    def destroy_education(self, id):
        try:
            education = Education.objects.get(id=id)
            education.delete()
            return {
                "data": {
                    "id": 'nil',
                    "confirmation": {
                        "info": "To see this record's deletion response, please do a GET request using the url",
                        "url": f'/api/v1/education/{id}'
                    }
                }
            }, 200
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Education record with given id doesn't exist.")
        except Exception:
            raise 500

educationcontroller = EducationController()
