from database.db import db

class Pmi(db.Document):
    downpayment_percentage = db.IntField(required=True, unique=True)
    from_620_639 = db.FloatField(required=True)
    from_640_659 = db.FloatField(required=True)
    from_660_679 = db.FloatField(required=True)
    from_680_699 = db.FloatField(required=True)
    from_700_719 = db.FloatField(required=True)
    from_720_739 = db.FloatField(required=True)
    from_740_759 = db.FloatField(required=True)
    from_760_850 = db.FloatField(required=True)
