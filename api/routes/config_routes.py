# Non API, copy right/documentation/debugging
from flask import render_template,request, Blueprint

welcome = Blueprint("welcome", __name__)

@welcome.route('/')
def hello():
    name = "DreamHome API Server"
    return render_template('welcome.html',name=name)
