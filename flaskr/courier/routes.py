from flask import Blueprint, render_template, request, redirect, flash, url_for
from flaskr import bcrypt, db, main
from flaskr.courier.forms import RegistrationForm, LoginForm, ServicesForm, ProfileForm
from flaskr.models import Courier, Services, Jobs
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

#Courier home page route
@courier.route('/home', methods=['POST', 'GET'])
def home():
    
    service = Services.query.filter_by(email=current_user.email).first()

    return render_template("courier_home.html", service=service)

#Courier offers page route
@courier.route('/profile', methods=["POST", "GET"])
def profile():
    form = ProfileForm()
    courier = Courier.query.filter_by(email=current_user.email).first()
    if request.method == "GET":
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.email.data = current_user.email  
    else:
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Account Information Updated SUccessfully!", "success")
        return render_template("courier_profile.html", form=form)



    return render_template("courier_profile.html", form=form)

@courier.route('/services', methods=["POST","GET"])
def services():
    form = ServicesForm()
    
    service = Services.query.filter_by(email=current_user.email).all()

    if request.method == "POST":
        if form.validate_on_submit():
            service = Services(type=form.type.data, location=form.location.data,
                               description=form.description.data, vehicle=form.vehicle.data, email=current_user.email)
            db.session.add(service)
            db.session.commit()
            flash("Service Added Successfuly", "success")
            return redirect(url_for('courier.services'))


    return render_template("courier_services.html", form=form, service=service)

@courier.route("/jobs")
def jobs():
    jobs = Jobs.query.filter_by(username=current_user.username).first()
    return render_template("courier_jobs.html")

