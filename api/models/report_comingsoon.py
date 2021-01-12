from database.db import db
# from api.models.user import User

class Report(db.Document):
    #Initial Post from FrontEnd
    salary = db.FloatField(required=True)
    zipcode = db.IntField(required=True)
    credit_score = db.IntField(required=True)
    monthly_debt = db.FloatField(required=True)
    downpayment_savings = db.FloatField(required=True)
    downpayment_percentage = db.FloatField(required=True)
    rent = db.FloatField()
    goal_principal = db.FloatField()
#Later
    # added_by = db.ReferenceField('User')

    def principal_based_on_rent(rent):
        return 'principal'

    def location(zipcode):
        return 'location'

    def monthly_principal(principal):
        return 'monthly_principal'

    def true_monthly(monthly_principal):
        # monthly_principal + home_insurance + pmi + property_tax
        return 'true_monthly'

    def home_insurance():
        return 'web scraped home_insurance'

    def property_tax():
        return 'web scraped property_tax'

    def pmi():
        return 'web scraped pmi'

    def percentage_saved_based_on_principal(downpayment_savings, principal):
        return 'backend magic'

    def downpayment_goal_monthly_savings(time, downpayment_savings, downpayment_percentage):
        return 'backend magic'

    def downpayment_savings_goal_end_date(time):
        return 'date'
