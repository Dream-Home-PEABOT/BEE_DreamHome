from database.db import db

class MortgageRate(db.document):
    credit_score_range = db.StringField(required=True, unique=True)
    rate = FloatField(required=True)
