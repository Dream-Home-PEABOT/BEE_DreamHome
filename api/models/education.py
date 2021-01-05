from database import db

class Education(db.Document):
    question = db.StringField(required=True)
    description = db.StringField(required=True)
    definition = db.StringField()
    source = db.StringField(required=True)
