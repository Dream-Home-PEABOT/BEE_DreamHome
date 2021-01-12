from database.db import db

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
