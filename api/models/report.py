import pry
from database.db import db
import math

class Report(db.Document):
    #Initial Post from FrontEnd
    salary = db.IntField(required=True)
    zipcode = db.IntField(required=True)
    credit_score = db.IntField(required=True)
    monthly_debt = db.IntField(required=True)
    downpayment_savings = db.IntField(required=True)
    downpayment_percentage = db.IntField(required=True)
    rent = db.IntField(default=0)
    goal_principal = db.IntField(default=0)

    def principal_based_on_rent(self):
        monthly = self.rent
        percentage = self.downpayment_percentage / 100
        annual_interest = self.mortgage_rate()
        monthly_interest = annual_interest / 12
        number_payments = 360
        exponent = math.pow((1 + monthly_interest), number_payments)
        numerator = (monthly) * (exponent - 1)
        denomenator = (percentage) * (monthly_interest * exponent)
        imaginative_principal = numerator / denomenator
        pry()
        return imaginative_principal

    def monthly_principal(self):
        pass



    def true_monthly(self):
        pass
    def home_insurance(self):
        pass

    def mortgage_rate(self):
        return 0.045

    def pmi(self):
        pass
    def property_tax(self):
        pass
