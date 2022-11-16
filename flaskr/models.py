from flaskr import db, login_manager
from datetime import datetime
from flask_login import UserMixin

#Initialise logged in deliverer with deliverer id
@login_manager.user_loader 
def load_user(user_id):
    return Deliverer.query.get(int(user_id))


#Create Deliverer database table with its fields
class Deliverer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name  %r>' % self.firstname 