from flask import Flask, jsonify
from database.db import initialize_db
from api.routes.api_routes import api
from api.helpers.errors import APIError
import traceback
import pry

app = Flask(__name__, template_folder = 'api/views')

app.config.from_envvar('ENV_FILE_LOCATION')

@app.route('/')
def hello():
    return 'Welcome to your dream home server!'

app.register_blueprint(api)
initialize_db(app)

@app.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {
        "data": {
            "error": err.description,
            "message": ""
        }
    }
    if len(err.args) > 0:
        response["data"]["message"] = err.args[0]
    # Add some logging so that we can monitor different types of errors
    app.logger.error(f"{err.description}: {response['data']['message']}")
    return jsonify(response), err.code

app.run()
