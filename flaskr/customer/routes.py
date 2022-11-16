from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user

from flaskr import db, bcrypt
from flaskr.models import Customer
from flaskr.customer.forms import RegistrationForm, LoginForm


customer = Blueprint('customer', __name__, url_prefix='/customer', static_folder="static", template_folder="../templates/customer")

@customer.route("/register", methods=["GET", "POST"])
#Do not name the route functions similar to the blueprint name
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        
        customer = Customer(
            username=form.username.data, email=form.email.data, password=hashed_password)

        db.session.add(customer)
        db.session.commit()
        flash('Your Account has been created! You can now login', 'success')
        return redirect(url_for('customer.login'))
    else:
        return render_template("customer_register.html", form=form)

    return render_template("customer_register.html")



@customer.route('/login', methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        customer = Customer.query.filter_by(username=form.username.data).first()

        #if customer exists in the database, proceed to validate the password and email entered
        if customer:
            #Check entered password against the hashed password stored in the database
            if bcrypt.check_password_hash(customer.password, form.password.data):
                login_user(customer)
                #Load the next webpage
                next_page = request.args.get('next')
                flash('Log In Successful', 'success')
                return redirect(next_page) if next_page else redirect(url_for('customer.home'))
            else:
                flash('Log In Unsuccessful. Check Password and Try Again.', 'danger')
        else:
            flash('Log In Unsuccessful. No user exists with that email. Check email and Try Again.', 'danger')
            return render_template("customer_login.html")

    return render_template("customer_login.html", form=form)

@customer.route('/logout')
def logout():
    logout_user()
    flash('Log Out Successful!', 'success')
    return redirect(url_for('main.home'))

@customer.route('/home')
def home():
    return render_template("customer_home.html")

