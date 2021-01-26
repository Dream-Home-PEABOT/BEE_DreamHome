from database.db import db

class MortgageRate(db.document):
    credit_score_floor = db.StringField(required=True, unique=True)
    credit_score_cieling = db.StringField(required=True, unique=True)
    rate = FloatField(required=True)
