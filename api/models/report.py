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

    # An IMAGINATIVE user does not have a goal principal in mind, but can give their current rental information to get an estimate of what they could afford by relating rent to monthly principal
    # A PRAGMATIC user knows the goal principal they are seeking, therefore will not enter rent and all calculations are based on the goal principal they entered
    # Helper Method for pmi && ReportController guard against goal principal vs rent
    def imaginative_or_pragmatic(self):
        if (self.goal_principal != 0) and (self.rent != 0 ):
            self.rent = 0

    # Helper method for monthly_principal && principal_based_on_rent
    def number_payments(self):
        if self.mortgage_term < 5:
            self.mortgage_term = 5
        return self.mortgage_term * 12

    # Helper method for zip_to_avg_home && home_insurance && property_tax
    def convert_abbreviation_to_full_state_name(self, city_state):
        abbrev_state = city_state[-2:]
        state = states[abbrev_state]
        return state

    # 1/5 Data Points for Report - BASED ON STATE
    def zip_to_avg_home(self, city_state):
        state = self.convert_abbreviation_to_full_state_name(city_state)
        median_home = MedianHomeValue.objects.get(state=state)
        return median_home.avg_home_value

    # 2/5 Data Points for Report - BASED ON STATE
    def home_insurance(self, city_state):
        state = self.convert_abbreviation_to_full_state_name(city_state)
        home_insurance = HomeInsurance.objects.get(state=state)
        monthly_insurance = home_insurance.annual_average_insurance_rate / 12
        return round(monthly_insurance)

    # 3/5 Data Points for Report - BASED ON STATE
    def property_tax(self, city_state):
        state = self.convert_abbreviation_to_full_state_name(city_state)
        property_tax = PropertyTax.objects.get(state=state)
        monthly_property_tax = property_tax.annual_avg_property_tax / 12
        return round(monthly_property_tax)

    # 4/5 Data Points for Report - BASED ON CREDIT SCORE
    def mortgage_rate(self):
        user_ceiling = self.credit_to_mortgage_range(self.credit_score)
        mortgage_rate = MortgageRate.objects.get(credit_score_ceiling=user_ceiling)
        rate = mortgage_rate.rate / 100
        return round(rate, 4)

    # 5/5 Data Points for Report - BASED ON DOWNPAYMENT PERCENTAGE USER SELECTS && CREDIT SCORE
    def pmi(self):
        guarded_dp = self.downpayment_percentage_to_db_pmi_object_range(self.downpayment_percentage)
        if type(guarded_dp) == str:
            return guarded_dp

        principal = self.principal_imaginative_or_pragmatic()
        pmi = Pmi.objects.get(downpayment_percentage=guarded_dp)
        monthly_pmi = self.monthly_pmi_calculation(principal, pmi)
        return round(monthly_pmi)

    # Helper Method for mortgage_rate
    def credit_to_mortgage_range(self, credit_score):
        if credit_score <= 619:
            user_ceiling = "619"
        elif credit_score in range(620, 640):
            user_ceiling = "639"
        elif credit_score in range(640, 660):
            user_ceiling = "659"
        elif credit_score in range(660, 680):
            user_ceiling = "679"
        elif credit_score in range(680, 700):
            user_ceiling = "699"
        elif credit_score in range(700, 760):
            user_ceiling = "759"
        elif credit_score in range(760, 851):
            user_ceiling = "850"
        return user_ceiling

    # Helper Method for pmi
    def monthly_pmi_calculation(self, principal, pmi):
        collector = self.credit_to_pmi_range(self.credit_score, pmi)
        reduced_principal = (1 - (pmi.downpayment_percentage / 100)) * principal
        annual_pmi = reduced_principal * (collector / 100)
        monthly_pmi = (annual_pmi / 12)
        return monthly_pmi

    # Helper Method fo pmi
    def downpayment_percentage_to_db_pmi_object_range(self, downpayment):
        if downpayment <= 4:
            guarded_dp = 0
        elif downpayment in range(5, 10):
            guarded_dp = 5
        elif downpayment in range(10, 15):
            guarded_dp = 10
        elif downpayment in range(15, 20):
            guarded_dp = 15
        else:
            return "No PMI required for a 20 percent or higher downpayment."
        return guarded_dp

    # Helper Method for monthly_pmi_calculation
    def credit_to_pmi_range(self, credit_score, pmi):
        if credit_score <= 639:
            collector = pmi.range_620_639
        elif credit_score in range(640, 660):
            collector = pmi.range_640_659
        elif credit_score in range(660, 680):
            collector = pmi.range_660_679
        elif credit_score in range(680, 700):
            collector = pmi.range_680_699
        elif credit_score in range(700, 720):
            collector = pmi.range_700_719
        elif credit_score in range(720, 740):
            collector = pmi.range_720_739
        elif credit_score in range(740, 760):
            collector = pmi.range_740_759
        elif credit_score in range(760, 851):
            collector = pmi.range_760_850
        return collector

    # Helper Method for pmi && percentage_saved_based_on_principal && downpayment_goal_monthly_savings
    def principal_imaginative_or_pragmatic(self):
        if self.goal_principal == 0:
            principal = self.principal_based_on_rent()
        else:
            principal = self.goal_principal
        return principal

    # ReportController stylized report function call
    def percentage_saved_based_on_principal(self):
        principal = self.principal_imaginative_or_pragmatic()
        percent_saved = (self.downpayment_savings / principal) * 100
        return round(percent_saved, 2)

    # ReportController stylized report function call
    def downpayment_goal_monthly_savings(self, year):
        if year == 0:
            return 0

        principal = self.principal_imaginative_or_pragmatic()

        potential_downpayment = principal * (self.downpayment_percentage / 100)
        if self.downpayment_savings >= potential_downpayment:
            downpayment = self.downpayment_savings
        downpayment = (principal - self.downpayment_savings) * (self.downpayment_percentage / 100)

        monthly_goal = downpayment / (year * 12)
        return round(monthly_goal)

    # ReportController stylized report function call
    def true_monthly(self, city_state):
        tm = self.rent + self.home_insurance(city_state) + self.property_tax(city_state)
        if self.downpayment_percentage < 20:
            tm += self.pmi()
        return tm

    # Helper Method for number_of_years && ReportController stylized report function call
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

    # Helper Method for number_of_years && principal_imaginative_or_pragmatic && ReportController stylized report function call
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
        if imaginative_principal < 30000:
            imaginative_principal = 30000
        return round(imaginative_principal)

    # ReportController stylized report function call
    def downpayment_savings_goal_end_date(self, year):
        now = datetime.datetime.now()
        month = now.month
        current_year = now.year
        day = now.day
        new_year = current_year + year
        date = f'{month}/{day}/{new_year}'
        return date

    # ReportController stylized report function call
    def number_of_years(self, savings_style):
        principal = self.principal_imaginative_or_pragmatic()
        potential_downpayment = principal * (self.downpayment_percentage / 100)
        if self.downpayment_savings >= potential_downpayment:
            dynamic_years = (0, 0, 0)
        else:
            monthly_living_expenses = self.calc_monthly_living_expense()
            remaining_monthly = self.calc_remaining_monthly_expense(monthly_living_expenses)
            downpayment = (principal - self.downpayment_savings) * (self.downpayment_percentage / 100)
            potential_monthly_savings = downpayment / 12
            year = 1
            static_monthly = potential_monthly_savings
            savings_cap = remaining_monthly * savings_style
            while potential_monthly_savings > savings_cap:
                potential_monthly_savings = static_monthly / year
                year += 1
            else:
                dynamic_years = (year, year + 2,  year + 4)
        return dynamic_years

    def calc_remaining_monthly_expense(self, monthly_living_expense):
        remaining_monthly = self.salary - self.monthly_debt - monthly_living_expense
        if remaining_monthly < 500:
            remaining_monthly = 500
        return remaining_monthly

    def calc_monthly_living_expense(self):
        if self.rent == 0:
            monthly_living_expense = self.monthly_principal()
        else:
            monthly_living_expense = self.rent
        return monthly_living_expense
