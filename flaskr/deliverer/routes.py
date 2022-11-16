from flask import Blueprint, render_template, request, redirect, flash
from flaskr import bcrypt, db
from flaskr.deliverer.forms import RegistrationForm, LoginForm
from flaskr.models import Deliverer


deliverer = Blueprint('deliverer', __name__, url_prefix='/deliverer', static_folder="static", template_folder="../templates/deliverer")


@deliverer.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        deliverer = Deliverer(
            firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)

        db.session.add(deliverer)
        db.session.commit()
        flash('Your Account has been created! You can now login', 'success')
        return redirect('login')
    else:
        return render_template("deliverer_register.html", form=form)


@deliverer.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    return render_template("deliverer_login.html", form=form)