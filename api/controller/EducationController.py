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
        education = Education.objects.get(id=id).to_json()
        return Response(education, mimetype="application/json", status=200)

    # GET all
    def index(self):
        educations = Education.objects()

        def convert_snake(string):
            return '_'.join(
                sub('([A-Z][a-z]+)', r' \1',
                sub('([A-Z]+)', r' \1',
                string.replace('-', ' '))).split()).lower()

        get_all_education_objects = {}

        for e in educations:
            get_all_education_objects[convert_snake(e.classification)] = {
                "type": str(e),
                "id": str(e.id),
                "attributes": {
                    "classification": e.classification,
                    "question": e.question,
                    "description": e.description,
                    "information": e.information,
                    "note": e.note,
                    "source": e.source
                }
            }

        return {"data": get_all_education_objects}, 200

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
