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
                            "mortgage_term": report.mortgage_term
                        },
                        "output": {
                            "location": {
                                "zipcode": report.zipcode,
                                "city_state": report.city_state(),
                                "average_home_price": report.home_price_by_zip(),
                                "information": "The term ZIP is an acronym for Zone Improvement Plan"
                            },
                            "principal": {
                                "principal_based_on_rent": report.principal_based_on_rent(),
                                "goal_principal": report.goal_principal,
                                "mortgage_rate": report.mortgage_rate(),
                                "information": "Your principal is the amount that you borrow from a lender. The interest is extra money that goes to your lender in exchange for giving you a loan."
                            },
                            "monthly": {
                                "monthly_principal": report.monthly_principal(),
                                "estimated_true_monthly": report.true_monthly(),
                                "home_insurance_by_location": report.home_insurance(),
                                "property_tax_by_location": report.property_tax(),
                                "pmi_by_location": report.pmi(),
                                "information": "This is an estimate of what your monthly expenses will be in purchasing a home in the zipcode your provided."
                            },
                            "downpayment": {
                                "downpayment_percentage_selected": report.downpayment_percentage,
                                "downpayment_saved": report.downpayment_savings,
                                "downpayment_percent_saved": report.percentage_saved_based_on_principal(),
                                "information": "The down payment is the portion of the purchase price that you pay out-of-pocket (as opposed to borrowing)",
                                "plan_style": {
                                # salary versus debt
                                #why:
                                    # currently, simplistic math
                                    # first year is always discouraging
                                    # doesn't  match based on salary and debt
                                # new:
                                    # only a percentage after debt and salary
                                    # five year plan, where the first number that starts with the year that's attuned to your current FINANCIAL SITUATION! *APPROPRIATE YEAR
                                # Example
                                #     monthly salary = x
                                #     debt = y
                                #     available = x - y - rent
                                # beyonce = .5 of available
                                    # three timelines
                                # taylor_swift = .3 of available
                                    # three timelines
                                # keanu_reece = .1 of available
                                    # three timelines
                                    "THIS BECOMES A DYNAMIC NUMBER": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(1),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(1)
                                    },
                                    "2": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(2),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(2)
                                    },
                                    "3": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(3),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(3)
                                    },
                                    "4": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(4),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(4)
                                    },
                                    "5": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(5),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(5)
                                    },
                                    "6": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(6),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(6)
                                    },
                                    "7": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(7),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(7)
                                    },
                                    "8": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(8),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(8)
                                    },
                                    "9": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(9),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(9)
                                    },
                                    "10": {
                                        "monthly_savings": report.downpayment_goal_monthly_savings(10),
                                        "goal_end_date": report.downpayment_savings_goal_end_date(10)
                                    }
                                }
                            }
                        }
                    }
                }
            }, 200
        except (ValidationError, DoesNotExist):
            raise APIDoesNotExistError(
                "Please check your request, the Report record with given id doesn't exist.")
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
            raise APISchemaError(
                "Please check the Report documentation. Request is missing a required field or incorrect field entered.")
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
            raise APISchemaError(
                "Please check the Report documentation. Request is missing a required field or incorrect field entered.")
        except DoesNotExist:
            raise APIDoesNotExistError(
                "Please check your request, the Report record with given id doesn't exist.")
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
            raise APIDoesNotExistError(
                "Please check your request, the Report record with given id doesn't exist.")
        except Exception:
            raise 500

reportcontroller = ReportController()
