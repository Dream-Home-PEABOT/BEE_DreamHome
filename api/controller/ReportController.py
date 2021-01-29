from api.services.zip import zip_to_location
from flask import Response, request, render_template, jsonify
from api.models.report import Report
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from api.helpers.errors import APINotUniqueError, APISchemaError, APIDoesNotExistError
import pry


class ReportController():
    # GET by UID
    def get_unique_report(self):
        try:
            try:
                uid = request.get_json()
            except Exception:
                return {
                    "data": {
                        "error": 410,
                        "message":"Missing UID"
                    }
                }, 410
            try:
                report = Report.objects.get(uid=uid)
                return self.stylized_report_return(report), 200
            except Exception:
                return {
                    "data": {
                        "error": 406,
                        "message":"No report matches this user"
                    }
                }, 406
        except Exception:
            raise 500

    # GET by ID
    def get_report(self, id):
        try:
            report = Report.objects.get(id=id)

            return self.stylized_report_return(report), 200
        except (ValidationError, DoesNotExist):
            raise APIDoesNotExistError(
                "Please check your request, the Report record with given id doesn't exist.")
        except Exception:
            raise 500

    def stylized_report_return(self, report):
        city_state = zip_to_location(report.zipcode)
        beyonce_plan = report.number_of_years(0.6)
        tswift_plan = report.number_of_years(0.4)
        keanu_plan = report.number_of_years(0.2)

        stylized_report = {
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
                            "city_state": city_state,
                            "average_home_price": report.zip_to_avg_home(city_state), # THIS NEEDS TO SWITCH TO A METHOD WITHIN THE REPORT MODEL
                            #replace with report.zip_to_avg_home
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
                            "estimated_true_monthly": report.true_monthly(city_state),
                            "home_insurance_by_location": report.home_insurance(city_state),
                            "property_tax_by_location": report.property_tax(city_state),
                            "pmi_by_location": report.pmi()
                        },
                        "D_downpayment": {
                            "information": "The down payment is the portion of the purchase price that you pay out-of-pocket (as opposed to borrowing)",
                            "downpayment_percentage_selected": report.downpayment_percentage,
                            "downpayment_saved": report.downpayment_savings,
                            "downpayment_percent_saved": report.percentage_saved_based_on_principal(),
                            "plan_style": {
                                "min_savings_plan": {
                                    "savings_style_percentage": 0.2,
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
                                "med_savings_plan": {
                                    "savings_style_percentage": 0.4,
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
                                "max_savings_plan": {
                                    "savings_style_percentage": 0.6,
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
        }
        return stylized_report

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

    # PUT
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

    # DELETE
    def destroy_report(self, id):
        try:
            report = Report.objects.get(id=id)
            report.delete()
            return {
                "data": {
                    "id": 'nil',
                    "confirmation": {
                        "info": "To see this record's deletion response, please do a GET request using the url",
                        "url": f'/api/v1/report/{id}'
                    }
                }
            }, 202
        except DoesNotExist:
            raise APIDoesNotExistError(
                "Please check your request, the Report record with given id doesn't exist.")
        except Exception:
            raise 500

reportcontroller = ReportController()
