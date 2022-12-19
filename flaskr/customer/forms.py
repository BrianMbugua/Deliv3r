from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from flaskr.models import Courier, Customer

class RegistrationForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])   
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        courier = Courier.query.filter_by(email=email.data).first()
        if courier:
            raise ValidationError('Email is already linked to another account.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_email(self, email):
        customer = Customer.query.filter_by(email=email.data).first()
        if not customer:
            raise ValidationError('Email is NOT linked to any account.')

class JobsForm(FlaskForm):
    type = SelectField(u'Job Type', choices=[('Job Type', ''),('Taxi', 'Taxi'), ('Cargo Heavy', 'Cargo Heavy'), ('Cargo Medium', 'Cargo Medium'), ('Cargo Light', 'Cargo Light'), ('Cargo Feather', 'Cargo Feather')], validators=[DataRequired()])
    pick_location = StringField('Pick-up Location', validators=[DataRequired()])
    drop_location = StringField('Drop-off Location', validators=[DataRequired()])
    vehicle = SelectField(u'Vehicle Required', choices=[('', ''), ('PICKUP', 'PICKUP'), ('CAR', 'CAR'), ('LORRY', 'LORRY'), ('MOTORCYCLE', 'MOTORCYCLE'), ('TROLLEY', 'TROLLEY')], validators=[DataRequired()])
    description = TextAreaField('Job description')
    submit = SubmitField('ADD')
