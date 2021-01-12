from database.db import db

class HomeInsurance(db.Document):
    state = db.StringField(required=True, unique=True)
    average_rate = db.IntField(required=True)