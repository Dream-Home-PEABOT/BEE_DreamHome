from .db import db

class Education(db.Document):
    question = db.StringField(required=True)
    explanation = db.StringField(required=True)
    source_link = db.StringField(required=True)
