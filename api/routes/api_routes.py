from flask import Blueprint,request,json
from api.controller.EducationController import educationcontroller
from api.controller.ReportController import reportcontroller
from api.controller.PmiController import pmicontroller
from api.controller.PropertyTaxController import propertytaxcontroller
from api.controller.HomeInsuranceController import homeinsurancecontroller
from api.controller.MortgageRateController import mortgageratecontroller


api = Blueprint("api", __name__)

@api.route('/')
def hello():
    return 'Welcome to the RESTful API Server for DreamHome!'

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

@api.route('/api/v1/pmi', methods=['GET'])
def get_all_pmi():
    return pmicontroller.index()

@api.route('/api/v1/pmi', methods=['POST'])
def add_pmi():
    return pmicontroller.add_pmi()
#
@api.route('/api/v1/pmi/<id>', methods=['PUT'])
def update_pmi(id):
    return pmicontroller.update_pmi(id)
#
@api.route('/api/v1/pmi/<id>', methods=['DELETE'])
def destroy_pmi(id):
    return pmicontroller.destroy_pmi(id)

@api.route('/api/v1/property_tax/<id>', methods=['GET'])
def get_property_tax(id):
    return propertytaxcontroller.get_property_tax(id)

@api.route('/api/v1/property_tax', methods=['POST'])
def add_property_tax():
    return propertytaxcontroller.add_property_tax()

@api.route('/api/v1/property_tax', methods=['GET'])
def all_property_tax():
    return propertytaxcontroller.index()

@api.route('/api/v1/property_tax/<id>', methods=['PUT'])
def update_property_tax(id):
    return propertytaxcontroller.update_property_tax(id)

@api.route('/api/v1/property_tax/<id>', methods=['DELETE'])
def destroy_property_tax(id):
    return propertytaxcontroller.destroy_property_tax(id)

@api.route('/api/v1/home_insurance', methods=['POST'])
def add_insurance():
    return homeinsurancecontroller.add_insurance()

@api.route('/api/v1/home_insurance/<id>', methods=['GET'])
def get_insurance(id):
    return homeinsurancecontroller.get_insurance(id)

@api.route('/api/v1/home_insurance', methods=['GET'])
def all_insurance():
    return homeinsurancecontroller.all_insurance()

@api.route('/api/v1/home_insurance/<id>', methods=['PUT'])
def update_insurance(id):
    return homeinsurancecontroller.update_insurance(id)

@api.route('/api/v1/home_insurance/<id>', methods=['DELETE'])
def destroy_insurance(id):
    return homeinsurancecontroller.destroy_insurance(id)

@api.route('/api/v1/mortgage_rate', methods=['POST'])
def add_mortgage_rate():
    return mortgageratecontroller.add_mortgage_rate()

@api.route('/api/v1/mortgage_rate/<id>', methods=['GET'])
def get_mortgage_rate(id):
    return mortgageratecontroller.get_mortgage_rate(id)

@api.route('/api/v1/mortgage_rate', methods=['GET'])
def all_mortgage_rate():
    return mortgageratecontroller.all_mortgage_rate()

@api.route('/api/v1/mortgage_rate/<id>', methods=['PUT'])
def update_mortgage_rate(id):
    return mortgageratecontroller.update_mortgage_rate(id)

@api.route('/api/v1/mortgage_rate/<id>', methods=['DELETE'])
def destroy_mortgage_rate(id):
    return mortgageratecontroller.destroy_mortgage_rate(id)
