from flask import Blueprint, render_template, request, redirect, flash, url_for
from flaskr import bcrypt, db, main
from flaskr.deliverer.forms import RegistrationForm, LoginForm
from flaskr.models import Deliverer
from flask_login import login_user, login_required, current_user, logout_user


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

    if form.validate_on_submit():
        deliverer = Deliverer.query.filter_by(email=form.email.data).first()

        #if deliverer exists in the database, proceed to validate the password and email entered
        if deliverer:
            #Check entered password against the hashed password stored in the database
            if bcrypt.check_password_hash(deliverer.password, form.password.data):
                login_user(deliverer)
                #Load the next webpage
                next_page = request.args.get('next')
                flash('Log In Successful', 'success')
                return redirect(next_page) if next_page else redirect(url_for('deliverer.home'))
            else:
                flash('Log In Unsuccessful. Check Password and Try Again.', 'danger')
        else:
            flash('Log In Unsuccessful. No user exists with that email. Check email and Try Again.', 'danger')
            return render_template("deliverer_login.html")

    return render_template("deliverer_login.html", form=form)

@deliverer.route('/logout')
def logout():
    logout_user()
    flash('Log Out Successful!', 'success')
    return redirect(url_for('main.home'))

@deliverer.route('/home')
def home():

    return render_template("deliverer_home.html")
