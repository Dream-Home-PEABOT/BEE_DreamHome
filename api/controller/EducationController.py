from flask import Response, request
from api.models.education import Education
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import EducationAlreadyExistsError
from flask import render_template
import pry

class EducationController():
    def __init__(self):
        pass
    # def get(self):

    def index(self):
        return render_template('education_documentation.html')

    def create(self):
        try:
            body = request.get_json()
            education = Education(**body) #will require auth later
            education.save()
            id = education.id
            return {"id": str(id)}, 200
        except NotUniqueError():
            pry()
            raise EducationAlreadyExistsError
        except Exception:
            raise InternalServerError
educationcontroller = EducationController()
