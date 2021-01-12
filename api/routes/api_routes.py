from flask import Blueprint,request,json
from api.controller.EducationController import educationcontroller
from api.controller.ReportController import reportcontroller
from api.controller.PmiController import pmicontroller

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

@api.route('/api/v1/report/<id>', methods=['GET'])
def get_report(id):
    return reportcontroller.get_report(id)

@api.route('/api/v1/report', methods=['POST'])
def add_report():
    return reportcontroller.add_report()

@api.route('/api/v1/report/<id>', methods=['PUT'])
def update_report(id):
    return reportcontroller.update_report(id)

@api.route('/api/v1/report/<id>', methods=['DELETE'])
def destroy_report(id):
    return reportcontroller.destroy_report(id)

@api.route('/api/v1/pmi/<id>', methods=['GET'])
def get_pmi(id):
    return pmicontroller.get_pmi(id)
#
# @api.route('/api/v1/pmi', methods=['GET'])
# def home():
#     return pmicontroller.index()

@api.route('/api/v1/pmi', methods=['POST'])
def add_pmi():
    return pmicontroller.add_pmi()
#
# @api.route('/api/v1/pmi/<id>', methods=['PUT'])
# def update_pmi(id):
#     return pmicontroller.update_pmi(id)
#
# @api.route('/api/v1/pmi/<id>', methods=['DELETE'])
# def destroy_pmi(id):
#     return pmicontroller.destroy_pmi(id)
