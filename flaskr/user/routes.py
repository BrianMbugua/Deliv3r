from flask import Blueprint, render_template

user = Blueprint('user', __name__,url_prefix='/user', static_folder="static", template_folder="templates")

@user.route('/')
def home():
    
    return render_template("home.html")