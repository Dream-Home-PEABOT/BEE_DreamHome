from flask import Flask
from database.db import initialize_db

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/dreamhome'
}

initialize_db(app)

@app.route("/")
def hello():
    return {"hello": "world"}

app.run()
