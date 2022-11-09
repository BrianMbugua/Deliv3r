from flask import Blueprint, render_template, request, redirect

deliverer = Blueprint('deliverer', __name__, url_prefix='/deliverer', static_folder="static", template_folder="../templates/deliverer")


@deliverer.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        req = request.form
        print(req)
        return redirect(request.url)

    return render_template("deliverer_register.html")