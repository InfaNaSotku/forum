from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    questions = db.relationship('Question', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    comments = db.relationship('Comment', backref='question', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    