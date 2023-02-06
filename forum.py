from flask import Flask



forum = Flask(__name__)


@forum.route("/")
def hello():
    return "<p>Hi!</p>"
