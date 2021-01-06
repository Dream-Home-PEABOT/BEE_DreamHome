from flask import Flask
from database.db import initialize_db
from api.routes.api_routes import WAAAAGH
app = Flask(__name__, template_folder = 'api/views')

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/dreamhome'
}

initialize_db(app)

@app.route("/")
def hello():
    return {"hello": "world"}
app.register_blueprint(WAAAAGH)

app.run()
