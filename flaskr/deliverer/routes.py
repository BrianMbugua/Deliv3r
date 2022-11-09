from flask import Blueprint, render_template, request, redirect

deliverer = Blueprint('deliverer', __name__, url_prefix='/deliverer', static_folder="static", template_folder="templates")

@deliverer.route("/test")
#Do not name the route functions similar to the blueprint name
def deliverer_test():
    return "<h3> DELIVERER </h3>"

@deliverer.route('/register', methods=["GET", "POST"])
def register():

    if request.method == "POST":
        req = request.form
        print(req)
        return redirect(request.url)

    return render_template("register.html")