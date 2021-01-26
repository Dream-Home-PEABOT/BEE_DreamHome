import pry
from database.db import db
import math
import datetime

class Report(db.Document):
    zipcode = db.IntField(required=True)
    credit_score = db.IntField(required=True)
    salary = db.IntField(required=True)
    monthly_debt = db.IntField(required=True)
    downpayment_savings = db.IntField(required=True)
    mortgage_term = db.IntField(default=0)
    downpayment_percentage = db.IntField(required=True)
    goal_principal = db.IntField(default=0)
    rent = db.IntField(default=0)

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
        rate = 0.0
        if self.credit_score in range(300, 639):
           rate = 4.072
        elif self.credit_score in range(640, 659):
            rate = 3.526
        elif self.credit_score in range(660, 679):
            rate = 3.096
        elif self.credit_score in range(680, 699):
            rate = 2.882
        elif self.credit_score in range(700, 759):
            rate = 2.705
        elif self.credit_score in range(760, 850):
            rate = 2.483

        rate = rate / 100
        return round(rate, 4)

    def city_state(self):
        # 80209 entered for zip
        return "Denver, CO"

    def home_price_by_zip(self):
        return "$834,278"

    def pmi(self):
        return 45

    def property_tax(self):
        return 100

    def monthly_principal(self):
        if self.rent != 0:
            return self.rent
        principal = self.goal_principal - self.downpayment_savings
        annual_interest = self.mortgage_rate()
        monthly_interest = annual_interest / 12
        percentage = self.downpayment_percentage / 100
        exponent = math.pow((1 + monthly_interest), self.number_payments())
        numerator = ((1 - percentage) * principal) * (monthly_interest) * (exponent)
        denominator = exponent - 1
        monthly = numerator / denominator
        return round(monthly, 2)

    def percentage_saved_based_on_principal(self):
        if self.goal_principal == 0.0:
            principal = self.principal_based_on_rent()
        else:
            principal = self.goal_principal
        percent_saved = (self.downpayment_savings / principal) * 100
        return round(percent_saved, 2)

    def downpayment_savings_goal_end_date(self, year):
        now = datetime.datetime.now()
        month = now.month
        current_year = now.year
        day = now.day
        new_year = current_year + year
        date = f'{month}/{day}/{new_year}'
        return date

    def principal_based_on_rent(self):
        if self.goal_principal != 0:
            return 0
        monthly = self.rent
        annual_interest = self.mortgage_rate()
        monthly_interest = annual_interest / 12
        percentage = 1 - (self.downpayment_percentage / 100)
        exponent = math.pow((1 + monthly_interest), self.number_payments())
        numerator = (exponent - 1) * (monthly)
        denominator = (monthly_interest) * (exponent) * (percentage)
        imaginative_principal = numerator / denominator
        return round(imaginative_principal)

    def downpayment_goal_monthly_savings(self, year):
        if self.goal_principal == 0.0:
            principal = self.principal_based_on_rent()
        else:
            principal = self.goal_principal
        downpayment = principal * (self.downpayment_percentage / 100)
        downpayment -= self.downpayment_savings
        monthly_goal = downpayment / (year * 12)
        return round(monthly_goal)
