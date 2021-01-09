from flask import Response, request, render_template
from api.models.education import Education
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import EducationAlreadyExistsError
from re import sub
import pry

class EducationController():
    # GET single
    def get_education(self, id):
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

    # GET all
    def index(self):
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

    # POST
    def add_education(self):
        # try:
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
        }, 200
        # except NotUniqueError():
        #     raise EducationAlreadyExistsError
        # except Exception:
        #     raise InternalServerError

    # PUT
    def update_education(self, id):
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

    # DESTROY
    def destroy_education(self, id):
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

educationcontroller = EducationController()
