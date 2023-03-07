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
    questions = User.query.filter_by(username=username).first().questions
    for question in questions:
        delete_question(question=question)
    db.session.delete(User.query.filter_by(username=username).first())
    db.session.commit()

def get_user(username : str) -> bool:
    return User.query.filter_by(username=username).first()

def add_question(title : str, content=''):
    question = Question(
        title = title,
        content = content,
        date = datetime.now(),
        user = User.query.filter_by(username=session['username']).first()
    )
    db.session.add(question)
    db.session.commit()
    return question

def delete_question(title=None, question=None):
    if not question:
        question = Question.query.filter_by(title=title).first()

    comments = question.comments
    for comment in comments:
        delete_comment(id=comment.id)
    db.session.delete(question)
    db.session.commit()

def get_question(title=None, id=None):
    if title:
        return Question.query.filter_by(title=title).first()
    else:
        return Question.query.filter_by(id=id).first()
    
def update_question(question : Question, title : str, content : str):
    question.content = content
    question.title = title
    db.session.commit()

def add_comment(content : str, question : Question):
    comment = Comment(
        content=content,
        date = datetime.now(),
        user = User.query.filter_by(username=session['username']).first(),
        question = question
    )
    db.session.add(comment)
    db.session.commit()
    return comment

def get_comment(id: int):
    return Comment.query.filter_by(id=id)

def delete_comment(id : int):
    db.session.delete(Comment.query.filter_by(id=id).first())
    db.session.commit()

def update_comment(comment : Comment, content : str):
    comment.content = content
    db.session.commit()