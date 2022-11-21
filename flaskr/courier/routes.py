from flask import Blueprint, render_template, request, redirect, flash, url_for
from flaskr import bcrypt, db, main
from flaskr.courier.forms import RegistrationForm, LoginForm
from flaskr.models import Courier
from flask_login import login_user, login_required, current_user, logout_user


courier = Blueprint('courier', __name__, url_prefix='/courier', static_folder="static", template_folder="../templates/courier")


@courier.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        courier = Courier(
            firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password)

        db.session.add(courier)
        db.session.commit()
        flash('Your Account has been created! You can now login', 'success')
        return redirect('login')
    else:
        return render_template("courier_register.html", form=form)


@courier.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        courier = Courier.query.filter_by(email=form.email.data).first()

        #if courier exists in the database, proceed to validate the password and email entered
        if courier:
            #Check entered password against the hashed password stored in the database
            if bcrypt.check_password_hash(courier.password, form.password.data):
                login_user(courier)
                #Load the next webpage
                next_page = request.args.get('next')
                flash('Log In Successful', 'success')
                return redirect(next_page) if next_page else redirect(url_for('courier.home'))
            else:
                flash('Log In Unsuccessful. Check Password and Try Again.', 'danger')
        else:
            flash('Log In Unsuccessful. No user exists with that email. Check email and Try Again.', 'danger')
            return render_template("courier_login.html")

    return render_template("courier_login.html", form=form)

@courier.route('/logout')
def logout():
    logout_user()
    flash('Log Out Successful!', 'success')
    return redirect(url_for('main.home'))

@courier.route('/home')
def home():

    return render_template("courier_home.html")