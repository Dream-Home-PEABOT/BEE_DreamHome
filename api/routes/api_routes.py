from flask import Blueprint,request,json
from api.controller.EducationController import educationcontroller

api = Blueprint("api", __name__)

@api.route('/api/v1/education/<id>', methods=['GET'])
def get_education(id):
    return educationcontroller.get_education(id)

@api.route('/api/v1/education', methods=['GET'])
def home():
    return educationcontroller.index()

@api.route('/api/v1/education', methods=['POST'])
def add_education():
    return educationcontroller.add_education()

@api.route('/api/v1/education/<id>', methods=['PUT'])
def update_education(id):
    return educationcontroller.update_education(id)

@api.route('/api/v1/education/<id>', methods=['DELETE'])
def destroy_education(id):
    return educationcontroller.destroy_education(id)
