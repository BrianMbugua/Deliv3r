from urllib import request
from flask import Blueprint, render_template, request, redirect

delivery = Blueprint('delivery', __name__, url_prefix='/delivery', static_folder="static", template_folder="templates1")

@delivery.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        req = request.form
        print(req)
        return redirect(request.url)

    return render_template("register.html")