from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from flaskr.models import Courier

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(min=2, max=10)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=10)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])   
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        courier = Courier.query.filter_by(email=email.data).first()
        if courier:
            raise ValidationError('Email is already linked to another account.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

    def validate_email(self, email):
        courier = Courier.query.filter_by(email=email.data).first()
        if not courier:
            raise ValidationError('Email is NOT linked to any account.')

class ServicesForm(FlaskForm):
    type = SelectField(u'Service Type', choices=[('TXI', 'Taxi'), ('CH', 'Cargo Heavy'), ('CM', 'Cargo Medium'), ('CL', 'Cargo Light'), ('CF', 'Cargo Feather')])
    