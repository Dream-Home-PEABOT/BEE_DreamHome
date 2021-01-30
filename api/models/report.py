import math
import datetime
from database.db import db
from api.models.pmi import Pmi
from api.models.mortgage_rate import MortgageRate
from api.models.home_insurance import HomeInsurance
from api.models.property_tax import PropertyTax
from api.models.median_home_value import MedianHomeValue
from api.helpers.state_abbrev_to_full import states


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
    uid = db.StringField()

    def zip_to_avg_home(self, city_state):
        abbrev_state = city_state[-2:]
        state = states[abbrev_state]
        median_home = MedianHomeValue.objects.get(state=state)
        return median_home.avg_home_value

    def number_payments(self):
        return self.mortgage_term * 12

    def home_insurance(self, city_state):
        zip = self.zipcode
        grab_state = city_state[-2:]
        state = states[grab_state]
        home_insurance = HomeInsurance.objects.get(state=state)
        monthly_insurance = home_insurance.annual_average_insurance_rate / 12
        return round(monthly_insurance)

    def mortgage_rate(self):
        report_cs = self.credit_score
        if report_cs <= 619:
            user_ceiling = "619"
        elif report_cs in range(620, 640):
            user_ceiling = "639"
        elif report_cs in range(640, 660):
            user_ceiling = "659"
        elif report_cs in range(660, 680):
            user_ceiling = "679"
        elif report_cs in range(680, 700):
            user_ceiling = "699"
        elif report_cs in range(700, 760):
            user_ceiling = "759"
        elif report_cs in range(760, 851):
            user_ceiling = "850"

        mortgage_rate = MortgageRate.objects.get(credit_score_ceiling=user_ceiling)
        rate = mortgage_rate.rate / 100
        return round(rate, 4)

    def property_tax(self, city_state):
        zip = self.zipcode
        grab_state = city_state[-2:]
        state = states[grab_state]
        property_tax = PropertyTax.objects.get(state=state)
        monthly_property_tax = property_tax.annual_avg_property_tax / 12
        return round(monthly_property_tax)

    def pmi(self):
        report_dp = self.downpayment_percentage
        if report_dp <= 4:
            guarded_dp = 0
        elif report_dp in range(5, 10):
            guarded_dp = 5
        elif report_dp in range(10, 15):
            guarded_dp = 10
        elif report_dp in range(15, 20):
            guarded_dp = 15
        else:
            return "No PMI required for a 20 percent or higher downpayment."

        report_cs = self.credit_score
        pmi = Pmi.objects.get(downpayment_percentage=guarded_dp)

        if report_cs <= 639:
            collector = pmi.range_620_639
        elif report_cs in range(640, 660):
            collector = pmi.range_640_659
        elif report_cs in range(660, 680):
            collector = pmi.range_660_679
        elif report_cs in range(680, 700):
            collector = pmi.range_680_699
        elif report_cs in range(700, 720):
            collector = pmi.range_700_719
        elif report_cs in range(720, 740):
            collector = pmi.range_720_739
        elif report_cs in range(740, 760):
            collector = pmi.range_740_759
        elif report_cs in range(760, 851):
            collector = pmi.range_760_850

        if self.goal_principal == 0:
            principal = self.principal_based_on_rent()
        else:
            principal = self.goal_principal

        reduced_principal = (1 - (pmi.downpayment_percentage / 100)) * principal
        annual_pmi = reduced_principal * (collector / 100)
        monthly_pmi = (annual_pmi / 12)
        return round(monthly_pmi)

    def true_monthly(self, city_state):
        tm = self.rent + self.home_insurance(city_state) + self.property_tax(city_state)
        if self.downpayment_percentage < 20:
            tm += self.pmi()
        return tm

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

        downpayment = (principal - self.downpayment_savings) * (self.downpayment_percentage / 100)
        monthly_goal = downpayment / (year * 12)
        return round(monthly_goal)

    def number_of_years(self, savings_style):
        monthly_pay = self.salary
        monthly_debt = self.monthly_debt

        if self.rent == 0:
            monthly_living_expense = self.monthly_principal()
            principal = self.goal_principal
        else:
            monthly_living_expense = self.rent
            principal = self.principal_based_on_rent()

        remaining_monthly = monthly_pay - monthly_debt - monthly_living_expense
        savings_cap = remaining_monthly * savings_style

        downpayment = (principal - self.downpayment_savings) * (self.downpayment_percentage / 100)
        potential_monthly_savings = downpayment / 12
        year = 1
        static_monthly = potential_monthly_savings
        while potential_monthly_savings > savings_cap:
            potential_monthly_savings = static_monthly / year
            year += 1
        else:
            dynamic_years = (year, year + 2,  year + 4)
        return dynamic_years
