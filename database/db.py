from flask_mongoengine import MongoEngine

db = MongoEngine()
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
