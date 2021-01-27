import os
import traceback
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from database.db import initialize_db
from api.routes.api_routes import api
from api.helpers.errors import APIError

app = Flask(__name__, template_folder = 'api/views')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

app.config['MONGODB_SETTINGS'] = {
    'db': os.environ['DBNAME'],
    'host': os.environ['HOST'],
    'username': os.environ['USERNAME'],
    'password': os.environ['PASSWORD']
}

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
    app.logger.error(f"{err.description}: {response['data']['message']}")
    return jsonify(response), err.code

@app.errorhandler(500)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    app.logger.error(f"Unknown Exception: {str(err)}")
    app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
    response = {
        "data": {
            "error": "Sorry, that error is on us, please contact support if this wasn't an accident"
        }
    }
    return jsonify(response), 500

if __name__ == 'main':
    app.run(threaded=True)
