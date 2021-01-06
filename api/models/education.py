from database import db

class Education(db.Document):
    classification = db.StringField(required=True)
    question = db.StringField(required=True)
    description = db.StringField(required=True)
    information = db.StringField()
    note = db.StringField()
    source = db.StringField(required=True)
