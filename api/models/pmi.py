from database.db import db


class Pmi(db.Document):
    downpayment_percentage = db.IntField(required=True, unique=True)
    range_620_639 = db.FloatField(required=True)
    range_640_659 = db.FloatField(required=True)
    range_660_679 = db.FloatField(required=True)
    range_680_699 = db.FloatField(required=True)
    range_700_719 = db.FloatField(required=True)
    range_720_739 = db.FloatField(required=True)
    range_740_759 = db.FloatField(required=True)
    range_760_850 = db.FloatField(required=True)
