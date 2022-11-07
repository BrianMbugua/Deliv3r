from flask import Flask

from .api.routes import api
from .delivery.routes import delivery

from .user.routes import user

def create_app():
    # create and configure the app
    app = Flask(__name__)
    
    app.register_blueprint(api)
    app.register_blueprint(delivery)
    app.register_blueprint(user)

    return app
