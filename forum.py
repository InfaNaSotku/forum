from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect, url_for
from flask_sqlalchemy import SQLAlchemy

forum = Flask(__name__)
db = SQLAlchemy()
forum.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///forum.db"
db.init_app(forum)
forum.secret_key = "SecretKey"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
with forum.app_context():
    db.create_all()

def add_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None:
        user = User(
            username=username,
            password=password,
        )
        db.session.add(user)
        db.session.commit()
    return user


@forum.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('index.html', username='guest')

@forum.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = add_user(request.form['username'], request.form['password'])
        if not user is None and not user.password == request.form['password']:
            return render_template('login.html', error='error')
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    elif request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('index'))
        else:
            return render_template('login.html')

@forum.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
    return redirect(url_for('index'))

