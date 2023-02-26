from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_forum):
    app = Flask(__name__)
    app.config.from_object(config_forum)

    db.init_app(app)
    with app.app_context():
        migrate.init_app(app, db)


    from .main import main
    from .auth import auth
    from .question import question

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(question, url_prefix='/question')

    return app