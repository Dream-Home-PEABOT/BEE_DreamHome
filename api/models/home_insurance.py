from database.db import db


class HomeInsurance(db.Document):
    state = db.StringField(required=True, unique=True)
    annual_average_insurance_rate = db.IntField(required=True)
