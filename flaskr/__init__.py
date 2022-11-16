from flask import Flask
from flask_bcrypt import Bcrypt

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# create and configure the app
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "super secret"
app.app_context().push()

#Initialise Database
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

#Initialise flask_login
login_manager = LoginManager() 
login_manager.init_app(app)
login_manager.login_view="login"
login_manager.login_message_category = 'info'

from flaskr.api.routes import api
from flaskr.main.routes import main
from flaskr.deliverer.routes import deliverer
from flaskr.deliveree.routes import deliveree


app.register_blueprint(api)
app.register_blueprint(main)
app.register_blueprint(deliverer)
app.register_blueprint(deliveree)


