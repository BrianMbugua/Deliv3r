from flaskr import db
from datetime import datetime


class Deliverer(db.Model):
    id = db.Column(db.Integer, primmary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name  %r>' % self.first_name 