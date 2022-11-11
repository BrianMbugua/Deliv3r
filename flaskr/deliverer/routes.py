from flask import Blueprint, render_template, request, redirect
from flaskr.deliverer.forms import RegistrationForm
from flaskr.models import Deliverer


deliverer = Blueprint('deliverer', __name__, url_prefix='/deliverer', static_folder="static", template_folder="../templates/deliverer")


@deliverer.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

   


    return render_template("deliverer_register.html", form=form)