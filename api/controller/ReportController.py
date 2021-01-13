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
                    "output": {
                        "location": {
                            "zipcode": 'report.zipcode',
                            "city_state": 'report.location',
                            "location_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "principal": {
                            "based_on_rent": 'report.principal_based_on_rent', # if we take in on rent
                            "goal_principal": 'report.goal_principal',
                            "principal_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "monthly": {
                            "monthly_principal": 'report.monthly_principal',
                            "estimated_true_monthly": {
                                "true_monthly": 'report.true_monthly',
                                "home_insurance": 'report.home_insurance',
                                "property_tax": 'report.property_tax',
                                "pmi": 'report.pmi',
                                "hoa": 'report.hoa'
                            },
                            "monthly_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "downpayment": {
                            "downpayment_percentage_selected": 'report.downpayment_percentage',
                            "downpayment_saved": 'report.downpayment_savings',
                            "downpayment_percent_saved": 'report.percentage_saved_based_on_principal',
                            "downpayment_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE",
                            "ten_year_plan": {
                                "one": {
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "two":{
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "three": {
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "four": {
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "five":{
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "six":{
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "seven":{
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "eight": {
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "nine":{
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                                "ten": {
                                    "monthly_savings":'report.downpayment_goal_monthly_savings',
                                    "goal_end_date": 'report.downpayment_savings_goal_end_date'
                                },
                            }
                        }
                    }
                }
            }
        }, 200
        except (ValidationError, DoesNotExist):
            raise APIDoesNotExistError("Please check your request, the Report record with given id doesn't exist.")
        except Exception:
            raise 500


    # POST
    def add_report(self):
        try:
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
        except (FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Report documentation. Request is missing a required field or incorrect field entered.")
        except Exception:
            raise 500

    def update_report(self, id):
        try:
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
            }, 202
        except (InvalidQueryError, FieldDoesNotExist, ValidationError):
            raise APISchemaError("Please check the Report documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Report record with given id doesn't exist.")
        except Exception:
            raise 500

    def destroy_report(self, id):
        try:
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
        except DoesNotExist:
            raise APIDoesNotExistError("Please check your request, the Report record with given id doesn't exist.")
        except Exception:
            raise 500
reportcontroller = ReportController()
