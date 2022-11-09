from flask import Blueprint, render_template

api = Blueprint('api', __name__, url_prefix='/api', static_folder="static", template_folder="templates")

@api.route('getdata')
def getdata():
    return render_template('api.html')