from flask import Response, request, render_template
from api.models.report import Report
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
import pry

class ReportController():
    # GET single
    def get_report(self, id):
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
                    "output": {
                        "location": {
                            "zipcode": report.zipcode,
                            "city_state": report.zipcode,
                            "location_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "principal": {
                            "based_on_rent": report.principal_based_on_rent(),
                            "goal_principal": report.goal_principal,
                            "mortgage_rate": report.mortgage_rate()
                            "principal_information": "what do we want to do here?"
                        },
                        "monthly": {
                            "monthly_principal": report.monthly_principal(),
                            "estimated_true_monthly": {
                                "true_monthly": report.true_monthly(),
                                "home_insurance": report.home_insurance(),
                                "property_tax": report.property_tax(),
                                "pmi": report.pmi()
                            },
                            "monthly_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        }
                    }
                }
            }
        }, 200


    # POST
    def add_report(self):
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
        }, 201

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
