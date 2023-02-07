from flask import Flask
from flask import request
from flask import render_template

forum = Flask(__name__)


@forum.route("/")
def index():
    return render_template("index.html")



@forum.route("/login", methods=['POST','GET'])
def login():
    return render_template("login.html")





