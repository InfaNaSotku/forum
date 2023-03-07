from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

def create_app(config_forum):
    app = Flask(__name__)
    app.config.from_object(config_forum)

    bcrypt.init_app(app)
    db.init_app(app)


    with app.app_context():
        migrate.init_app(app, db)


    from .main import main
    from .auth import auth
    from .question import question

    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(question, url_prefix='/question')

    app.jinja_env.globals.update(zip=zip)
    app.jinja_env.globals.update(len=len)

    return app