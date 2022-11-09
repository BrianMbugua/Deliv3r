from flask import Blueprint, render_template

deliveree = Blueprint('deliveree', __name__, url_prefix='/deliveree', static_folder="static", template_folder="../templates/deliveree")

@deliveree.route("/register")
#Do not name the route functions similar to the blueprint name
def register():
    return render_template("deliveree_register.html")