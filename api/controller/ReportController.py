from flask import Response, request, render_template
from api.models.report import Report
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
import pry
import json


class ReportController():
    # GET single
    def get_report(self, id):
        try:
            report = Report.objects.get(id=id)
            beyonce_plan = report.number_of_years(0.5)
            tswift_plan = report.number_of_years(0.3)
            keanu_plan = report.number_of_years(0.1)

            return {
                "data": {
                    "01_type": str(report),
                    "02_id": str(report.id),
                    "03_attributes": {
                        "input": {
                            "A_zipcode": report.zipcode,
                            "B_credit_score": report.credit_score,
                            "C_salary": report.salary,
                            "D_monthly_debt": report.monthly_debt,
                            "E_downpayment_savings": report.downpayment_savings,
                            "F_mortgage_term": report.mortgage_term,
                            "G_downpayment_percentage": report.downpayment_percentage,
                            "H_goal_principal": report.goal_principal,
                            "I_rent": report.rent
                        },
                        "output": {
                            "A_location": {
                                "information": "By providing a zipcode, we can report location specific information such as average home price.",
                                "zipcode": report.zipcode,
                                "city_state": report.city_state(),
                                "average_home_price": report.home_price_by_zip(),
                            },
                            "B_principal": {
                                "information": "Your principal is the amount that you borrow from a lender. The interest is extra money that goes to your lender in exchange for giving you a loan.",
                                "mortgage_rate": report.mortgage_rate(),
                                "goal_principal": report.goal_principal,
                                "principal_based_on_rent": report.principal_based_on_rent()
                            },
                            "C_monthly": {
                                "information": "This is an estimate of what your monthly expenses will be in purchasing a home in the zipcode your provided.",
                                "monthly_principal": report.monthly_principal(),
                                "estimated_true_monthly": report.true_monthly(),
                                "home_insurance_by_location": report.home_insurance(),
                                "property_tax_by_location": report.property_tax(),
                                "pmi_by_location": report.pmi()
                            },
                            "D_downpayment": {
                                "information": "The down payment is the portion of the purchase price that you pay out-of-pocket (as opposed to borrowing)",
                                "downpayment_percentage_selected": report.downpayment_percentage,
                                "downpayment_saved": report.downpayment_savings,
                                "downpayment_percent_saved": report.percentage_saved_based_on_principal(),
                                "plan_style": {
                                    "01_keanu_frugal": {
                                        "saving_style_percentage": 0.1,
                                        "plan_1": {
                                            "number_of_years": keanu_plan[0],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(keanu_plan[0]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(keanu_plan[0])
                                        },
                                        "plan_2": {
                                            "number_of_years": keanu_plan[1],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(keanu_plan[1]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(keanu_plan[1])
                                        },
                                        "plan_3": {
                                            "number_of_years": keanu_plan[2],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(keanu_plan[2]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(keanu_plan[2])
                                        }
                                    },
                                    "02_tswift_moderate": {
                                        "saving_style_percentage": 0.3,
                                        "plan_1": {
                                            "number_of_years": tswift_plan[0],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(tswift_plan[0]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(tswift_plan[0])
                                        },
                                        "plan_2": {
                                            "number_of_years": tswift_plan[1],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(tswift_plan[1]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(tswift_plan[1])
                                        },
                                        "plan_3": {
                                            "number_of_years": tswift_plan[2],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(tswift_plan[2]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(tswift_plan[2])
                                        }
                                    },
                                    "03_beyonce": {
                                        "saving_style_percentage": 0.5,
                                        "plan_1": {
                                            "number_of_years": beyonce_plan[0],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(beyonce_plan[0]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(beyonce_plan[0])
                                        },
                                        "plan_2": {
                                            "number_of_years": beyonce_plan[1],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(beyonce_plan[1]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(beyonce_plan[1])
                                        },
                                        "plan_3": {
                                            "number_of_years": beyonce_plan[2],
                                            "monthly_savings": report.downpayment_goal_monthly_savings(beyonce_plan[2]),
                                            "goal_end_date": report.downpayment_savings_goal_end_date(beyonce_plan[2])
                                        }
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
