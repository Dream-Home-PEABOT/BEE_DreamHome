from database.db import db


class PropertyTax(db.Document):
    state = db.StringField(required=True, unique=True)
    avg_tax_rate = db.FloatField(required=True)
    annual_avg_property_tax = db.IntField(required=True)
