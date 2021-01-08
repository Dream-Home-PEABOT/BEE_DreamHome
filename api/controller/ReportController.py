from flask import Response, request
from api.models.report import Report
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from flask import render_template
import pry

class ReportController():
    def add_report(self):
        body = request.get_json()
        # make the report exist
        report = Report(**body)
        report.save()
        id = report.id
        # have it return an
        return {
            "data": {
                "id": str(id),
                "confirmation": {
                    "info": 'To connect this report to a user in the future, save this url with the client',
                    "url": f'/api/v1/record/{id}'
                }
            }
        }, 200

# GET single
    def get_report(self, id):
        report = Report.objects.get(id=id)
        return {
            "data": {
                "type": string(report),
                "id": str(report.id)
            }
        }

# GET all
