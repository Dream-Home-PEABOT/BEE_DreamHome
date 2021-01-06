from flask import Response, request
from api.models.education import Education
from flask import render_template

class EducationController():
    def __init__(self):
        pass
    # def get(self):

    def index(self):   
        return render_template('index.html')
educationcontroller = EducationController()