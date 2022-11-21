from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from flask_wtf.file import FileAllowed, FileField, FileRequired
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
    type = SelectField(u'Service Type', choices=[('Taxi', 'Taxi'), ('Cargo Heavy', 'Cargo Heavy'), ('Cargo Medium', 'Cargo Medium'), ('Cargo Light', 'Cargo Light'), ('Cargo Feather', 'Cargo Feather')])
    location = StringField('Location', validators=[DataRequired()])
    vehicle = SelectField(u'Vehicle Type', choices=[('', ''), ('PICKUP', 'PICKUP'), ('CAR', 'CAR'), ('LORRY', 'LORRY'), ('MOTORCYCLE', 'MOTORCYCLE'), ('TROLLEY', 'TROLLEY')], validators=[DataRequired()])
    description = TextAreaField('Vehicle description')
    photo = FileField('Photo', validators=[FileAllowed(['jpg', 'png']), DataRequired()])
    submit = SubmitField('ADD')
