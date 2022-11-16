from flask import Blueprint, render_template, flash, redirect
from flaskr.customer.forms import RegistrationForm
from flaskr import db, bcrypt
from flaskr.models import Courier, Customer

customer = Blueprint('customer', __name__, url_prefix='/customer', static_folder="static", template_folder="../templates/customer")

@customer.route("/register")
#Do not name the route functions similar to the blueprint name
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
        return render_template("customer_register.html", form=form)

    return render_template("customer_register.html")