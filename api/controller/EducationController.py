from flask import Response, request
from api.models.education import Education
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import EducationAlreadyExistsError
from flask import render_template
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
        return {"id": str(id)}, 200
        # except NotUniqueError():
        #     raise EducationAlreadyExistsError
        # except Exception:
        #     raise InternalServerError

    # PUT
    def update_education(self, id):
        education = Education.objects.get(id=id)
        body = request.get_json()
        education.update(**body)
        return {"id": str(id), "to_see_update": "Run GET /api/v1/education or GET /api/v1/<id>"}, 200

    # DESTROY
    def destroy_education(self, id):
        education = Education.objects.get(id=id)
        education.delete()
        return {"id": 'nil', "to_see_removal": "Run GET /api/v1/education or GET /api/v1/<id>"}, 200

educationcontroller = EducationController()
