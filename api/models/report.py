from database import db

class Report(db.Document):
    salary = db.FloatField(required=True)
    zipcode = db.IntField(required=True)
    credit = db.IntField(required=True)
    monthly_debt = db.FloatField(required=True)
    downpayment_savings = db.FloatField(required=True)
    downpayment_percentage = db.IntField(required=True)
    rent = db.FloatField()
    goal_principal = db.FloatField()
