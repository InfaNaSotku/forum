from flask import Flask, redirect, render_template, request, session, url_for
from app.model_manage import add_user
from . import auth

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = add_user(request.form['username'], request.form['password'])
        if not user is None and not user.password == request.form['password']:
            return render_template('login.html', error='error')
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html')

@auth.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
    return redirect(url_for('main.index'))