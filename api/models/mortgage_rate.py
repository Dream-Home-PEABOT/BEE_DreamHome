from database.db import db

class MortgageRate(db.Document):
    credit_score_floor = db.StringField(required=True, unique=True)
    credit_score_cieling = db.StringField(required=True, unique=True)
    rate = db.FloatField(required=True)
