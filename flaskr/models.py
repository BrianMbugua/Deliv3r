from flaskr import db, login_manager
from datetime import datetime
from flask_login import UserMixin

#Initialise logged in Courier with Courier id
@login_manager.user_loader 
def load_user(user_id):
    return Courier.query.get(int(user_id))

#COURIER MODELS
#Create courier database table with its fields
class Courier(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Firstname  %r>' % self.firstname 
        
    def is_authenticated(self):
        return True

    def is_active(self):   
        return True           

    def is_anonymous(self):
        return False          

    def get_id(self):         
        return str(self.id)

class Services(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    vehicle = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    photo = db.Column(db.String(20), nullable=False, default="default.jpg")
    email = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle


##############################################################################################################
#CUSTOMER MODELS
#Create Customer database table
class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Username %r>' % self.username