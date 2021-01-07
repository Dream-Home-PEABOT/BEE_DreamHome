from flask import Flask
from database.db import initialize_db
from api.routes.api_routes import api

app = Flask(__name__, template_folder = 'api/views')

app.config.from_envvar('ENV_FILE_LOCATION')

initialize_db(app)

@app.route('/')
def hello():
    return 'Welcome to your dream home server!'

app.register_blueprint(api)

app.run()
