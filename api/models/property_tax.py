from database.db import db

class PropertyTax(db.Document):
    state = db.StringField(required=True, unique=True)
    tax_rate = db.FloatField(required=True)
    avg_property_tax = db.IntField(required=True)