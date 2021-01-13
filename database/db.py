# from flask_mongoengine import MongoEngine
import pymongo
import os

uri = os.environ.get('MONGODB_URI')
client = pymongo.MongoClient(uri)
db = client['dreamhome']

def initialize_db(app):
    db.init_app(app)

# stream = open(options.filename, 'r')
# yamlData = yaml.load(stream)
# jsonData = json.dumps(yamlData)
# id = StringIO(jsonData)
#
# ...calling class, etc, then
# self.appCollection.insert(me)

# https://stackoverflow.com/questions/21712181/python-insert-yaml-in-mongodb
