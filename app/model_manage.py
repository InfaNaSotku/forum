from .model import User, Question, Comment
from app import db
from datetime import datetime
from flask import session

def add_user(username : str, password : str):
    user = User(
        username=username,
        password=password,
    )
    db.session.add(user)
    db.session.commit()
    return user

def delete_user(username : str):
    db.session.delete(User.query.filter_by(username=username).first())
    db.session.commit()

def get_user(username : str) -> bool:
    return User.query.filter_by(username=username).first()

def add_question(title : str, content=""):
    question = Question(
        title = title,
        content = content,
        date = datetime.now(),
        user = User.query.filter_by(username=session['username']).first()
    )
    db.session.add(question)
    db.session.commit()
    return question
