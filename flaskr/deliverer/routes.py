from flask import Blueprint, render_template, request, redirect
from flaskr.deliverer.forms import RegistrationForm
from flaskr.models import Deliverer, db


deliverer = Blueprint('deliverer', __name__, url_prefix='/deliverer', static_folder="static", template_folder="../templates/deliverer")


@deliverer.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.is_submitted():
        form_data = request.form

        deliverer = Deliverer.query.filter_by(email=form_data["password"]).first()
        print(deliverer)
        if deliverer is None:
            deliverer = Deliverer(firstname=form_data["firstname"], lastname=form_data["lastname"], email=form_data["email"], password=form_data["password"])
            db.session.add(deliverer)
            db.session.commit()

        return redirect(request.url)


    return render_template("deliverer_register.html", form=form)