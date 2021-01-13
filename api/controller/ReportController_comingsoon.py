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
                            "city_state": report.location, #map quest service, https://www.zipcodeapi.com/Register
                            "location_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "principal": {
                            "goal_principal": report.goal_principal,
                            "principal_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "monthly": {
                            "monthly_principal": report.monthly_principal,
                            "estimated_true_monthly": {
                                "true_monthly": report.true_monthly,
                                "home_insurance": report.home_insurance,
                                "property_tax": report.property_tax,
                                "pmi": report.pmi,
                                "hoa": report.hoa
                            },
                            "monthly_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
                        },
                        "downpayment": {
                            "downpayment_percentage_selected": report.downpayment_percentage,
                            "downpayment_saved": report.downpayment_savings,
                            "downpayment_percent_saved": report.percentage_saved_based_on_principal,
                            "downpayment_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE",
                            "ten_year_plan": {
                                "one": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(1, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(1)
                                },
                                "two": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(2, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(2)
                                },
                                "three": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(3, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(3)
                                },
                                "four": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(4, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(4)
                                },
                                "five": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(5, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(5)
                                },
                                "six": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(6, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(6)
                                },
                                "seven": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(7, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(7)
                                },
                                "eight": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(8, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(8)
                                },
                                "nine": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(9, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(9)
                                },
                                "ten": {
                                    "monthly_savings": report.downpayment_goal_monthly_savings(10, report.downpayment_savings, report.downpayment_percentage),
                                    "goal_end_date": report.downpayment_savings_goal_end_date(10)
                                },
                            }
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
        }, 200

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

reportcontroller = ReportController()








#
# {
#     "data": {
#         "type": str(report),
#         "id": str(report.id),
#         "attributes": {
#             "input": {
#                 "salary": report.salary,
#                 "zipcode": report.zipcode,
#                 "credit_score": report.credit_score,
#                 "monthly_debt": report.monthly_debt,
#                 "downpayment_savings": report.downpayment_savings,
#                 "downpayment_percentage": report.downpayment_percentage,
#                 "rent": report.rent,
#                 "goal_principal": report.goal_principal,
#             },
#             "output": {
#                 "location": {
#                     "zipcode": report.zipcode,
#                     "city_state": report.location #map quest service,
#                     "location_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
#                 },
#                 "principal": {
#                     "based_on_rent": report.principal_based_on_rent, # if we take in on rent
#                     "goal_principal": report.goal_principal,
#                     "principal_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
#                 },
#                 "monthly": {
#                     "monthly_principal": report.monthly_principal,
#                     "estimated_true_monthly": {
#                         "true_monthly": report.true_monthly,
#                         "home_insurance": report.home_insurance,
#                         "property_tax": report.property_tax,
#                         "pmi": report.pmi,
#                         "hoa": report.hoa
#                     },
#                     "monthly_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE"
#                 },
#                 "downpayment": {
#                     "downpayment_percentage_selected": report.downpayment_percentage,
#                     "downpayment_saved": report.downpayment_savings,
#                     "downpayment_percent_saved": report.percentage_saved_based_on_principal,
#                     "downpayment_information": "DEAR FE, HARD CODE INFORMATION YOU WANT HERE",
#                     "ten_year_plan": {
#                         "one": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(1, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(1)
#                         },
#                         "two": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(2, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(2)
#                         },
#                         "three": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(3, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(3)
#                         },
#                         "four": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(4, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(4)
#                         },
#                         "five": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(5, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(5)
#                         },
#                         "six": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(6, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(6)
#                         },
#                         "seven": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(7, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(7)
#                         },
#                         "eight": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(8, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(8)
#                         },
#                         "nine": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(9, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(9)
#                         },
#                         "ten": {
#                             "monthly_savings": report.downpayment_goal_monthly_savings(10, report.downpayment_savings, report.downpayment_percentage),
#                             "goal_end_date": report.downpayment_savings_goal_end_date(10)
#                         },
#                     }
#                 }
#             }
#         }
#     }
# }
