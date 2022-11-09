from flask import Flask

from flaskr.api.routes import api
from flaskr.main.routes import main
from flaskr.deliverer.routes import deliverer
from flaskr.deliveree.routes import deliveree


def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    app.register_blueprint(api)
    app.register_blueprint(main)
    app.register_blueprint(deliverer)
    app.register_blueprint(deliveree)

    return app

