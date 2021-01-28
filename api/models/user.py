from database.db import db
import pry


class User(db.Document):
    name = db.StringField(required=True)
    uid = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True, unique=True)
    blarg = db
    pry()
    reports = db.ListField(db.ReferenceField('Report', reverse_delete_rule=db.PULL))


User.register_delete_rule(Report, 'added_by', db.CASCADE)
# Allows our user to
# - register user
# - login user
# - if a logged in user does a report, is it connected???!?!
