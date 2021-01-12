from flask import Response, request, render_template
from api.models.report import Report
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
import pry

class ReportController():
    # GET single
    def get_report(self, id):
        try:
            report = Report.objects.get(id=id)
            return {
                "data": {
                    "type": str(report),
                    "id": str(report.id),
                    "attributes": {
                        "input": {
                            "salary": report.salary,
                            "zipcode": report.zipcode,
                            "credit_score": report.credit_score,
                            "monthly_debt": report.monthly_debt,
                            "downpayment_savings": report.downpayment_savings,
                            "downpayment_percentage": report.downpayment_percentage,
                            "rent": report.rent,
                            "goal_principal": report.goal_principal,

                        },
                        "output": {}
                    }
                }
            }, 200
        except (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Report record given id doesn't exist")
        except Exception:
            raise 500

    # POST
    def add_report(self):
        # try:
        body = request.get_json()
        # make the report exist
        report = Report(**body)
        report.save()
        id = report.id
        # have it return an id
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": 'To connect this report to a user in the future, save this url with the client',
                    "url": f'/api/v1/report/{id}'
                }
            }
        }, 200
        # except NotUniqueError:
        #     raise APINotUniqueError("This report record's salary")

    def update_report(self, id):
        report = Report.objects.get(id=id)
        body = request.get_json()
        report.update(**body)
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": "To see this record's update response, please do a GET request using the url",
                    "url": f'/api/v1/report/{id}'
                }
            }
        }, 200

    def destroy_report(self, id):
        report = Report.objects.get(id=id)
        report.delete()
        return {
            "data": {
                "id": 'nil',
                "confirmation": {
                    "info": "To see this record's deletion response, please do a GET request using the url",
                    "url": f'/api/v1/education/{id}'
                }
            }
        }, 200

reportcontroller = ReportController()
