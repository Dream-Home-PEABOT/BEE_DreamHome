from flask import Blueprint,request,json
from api.controller.EducationController import educationcontroller
from api.controller.ReportController import reportcontroller
from api.controller.PropertyTaxController import propertytaxcontroller

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


@api.route('/api/v1/property_tax/<id>', methods=['GET'])
def get_property_tax(id):
    return propertytaxcontroller.get_property_tax(id)

@api.route('/api/v1/property_tax', methods=['POST'])
def add_property_tax():
    return propertytaxcontroller.add_property_tax()


@api.route('/api/v1/property_tax', methods=['GET'])
def all_property_tax():
    return propertytaxcontroller.index()
