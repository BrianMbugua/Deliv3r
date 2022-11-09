from flask import Blueprint, render_template

deliveree = Blueprint('deliveree', __name__, url_prefix='/deliveree', static_folder="static", template_folder="templates")

@deliveree.route("/test")
#Do not name the route functions similar to the blueprint name
def deliveree_test():
    return "<h3> DELIVEREE </h3>"