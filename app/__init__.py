from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(config_forum):
    app = Flask(__name__)
    app.config.from_object(config_forum)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    from .main import main
    from .auth import auth
    
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')


    return app