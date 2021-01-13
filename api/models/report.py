import pry
from database.db import db
import math
import datetime

class Report(db.Document):
    salary = db.IntField(required=True)
    zipcode = db.IntField(required=True)
    credit_score = db.IntField(required=True)
    monthly_debt = db.IntField(required=True)
    downpayment_savings = db.IntField(required=True)
    downpayment_percentage = db.IntField(required=True)
    rent = db.IntField(default=0)
    goal_principal = db.IntField(default=0)

    def number_payments(self):
        return 360

    def true_monthly(self):
        tm = self.rent + self.home_insurance() + self.property_tax()
        if self.downpayment_percentage < 20:
            tm += self.pmi()
        return tm

    def home_insurance(self):
        return 125

    def mortgage_rate(self):
        return 0.045

    def pmi(self):
        return 45

    def property_tax(self):
        return 100

    def monthly_principal(self):
        return self.rent

    def percentage_saved_based_on_principal(self):
        return self.downpayment_percentage #fix this!

    def downpayment_goal_monthly_savings(self, year):
        monthly_goal = self.downpayment_savings / (year * 12) #fix this!
        return round(monthly_goal)

    def downpayment_savings_goal_end_date(self, year):
        now = datetime.datetime.now()
        month = now.month
        current_year = now.year
        day = now.day
        new_year = current_year + year
        date = f'{month}/{day}/{new_year}'
        return date


    def principal_based_on_rent(self):
        monthly = self.rent
        percentage = self.downpayment_percentage / 100
        annual_interest = self.mortgage_rate()
        monthly_interest = annual_interest / 12
        number_payments = self.number_payments()

        exponent = math.pow((1 + monthly_interest), number_payments)

        numerator = (monthly) * (exponent - 1)

        denomenator = (percentage) * (monthly_interest * exponent)

        imaginative_principal = numerator / denomenator
        return round(imaginative_principal)
