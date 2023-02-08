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

@forum.route("/")
def index():
    return render_template("index.html", username=session['username'])



@forum.route("/login", methods=['POST','GET'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    elif request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('index'))
        else:
            return render_template("login.html")

 




