from database.db import db

class Report(db.Document):
    #Initial Post from FrontEnd
    salary = db.IntField(required=True)
    zipcode = db.IntField(required=True)
    credit_score = db.IntField(required=True)
    monthly_debt = db.IntField(required=True)
    downpayment_savings = db.IntField(required=True)
    downpayment_percentage = db.IntField(required=True)
    rent = db.IntField()
    goal_principal = db.IntField()
