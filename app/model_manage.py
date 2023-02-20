from .model import User, Question, Comment
from app import db

def add_user(username : str, password : str):
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            password=password,
        )
        db.session.add(user)
        db.session.commit()
    return user