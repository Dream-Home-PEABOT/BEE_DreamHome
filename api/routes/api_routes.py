from flask import Blueprint,request,json
from api.controller.EducationController import educationcontroller

WAAAAGH = Blueprint("WAAAAGH", __name__)
@WAAAAGH.route('/education', methods=['GET'])
def home():
    return educationcontroller.index()
# @api.route('/registration', methods=['GET'])
# def register():
#     return homecontroller.register()
# @api.route('/registration', methods=['POST'])
# def registeruser():
#     return homecontroller.registeruser()