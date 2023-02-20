from flask import Flask, redirect, render_template, request, session

from . import main

@main.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return render_template('index.html', username='guest')