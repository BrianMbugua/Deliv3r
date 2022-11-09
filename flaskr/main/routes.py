from flask import Blueprint, render_template

main = Blueprint('main', __name__, static_folder="static", template_folder="../templates/main")

@main.route("/")
#Do not name the route functions similar to the blueprint name
def home():
    return render_template('home.html')