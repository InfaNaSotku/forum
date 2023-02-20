import os

class config(object):

    SECRET_KEY = os.getenv("SECRET_KEY") or "secret_key"

    SQLALCHEMY_DATABASE_URI = "sqlite:///forum.db"