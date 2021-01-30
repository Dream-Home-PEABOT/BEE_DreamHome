from database.db import db


class MedianHomeValue(db.Document):
    year = db.IntField(required=True)
    state = db.StringField(required=True, unique=True)
    avg_home_value = db.IntField(required=True)
    median_top_tier = db.IntField()
    median_single_family_value = db.IntField()
    median_bottom_tier = db.IntField()
    median_condo_value = db.IntField()
