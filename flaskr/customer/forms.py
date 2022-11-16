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