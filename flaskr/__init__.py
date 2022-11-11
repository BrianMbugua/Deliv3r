from flask import Flask

from flask_sqlalchemy import SQLAlchemy

# create and configure the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "super secret"


db = SQLAlchemy(app)



from flaskr.api.routes import api
from flaskr.main.routes import main
from flaskr.deliverer.routes import deliverer
from flaskr.deliveree.routes import deliveree


app.register_blueprint(api)
app.register_blueprint(main)
app.register_blueprint(deliverer)
app.register_blueprint(deliveree)


