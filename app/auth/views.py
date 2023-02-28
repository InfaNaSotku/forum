from flask import Flask, redirect, render_template, request, session, url_for
from app import bcrypt

from . import auth
from app.model import User
from app.model_manage import add_user, get_user, delete_user

@auth.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = get_user(username=request.form['username'])
        if not user:
            return render_template('login.html', error='User doesn\'t exist')
        if not bcrypt.check_password_hash(user.password, request.form['password']):
            return render_template('login.html', error='Incorrect password')
        session['username'] = request.form['username']
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('main.index'))
        else:
            return render_template('login.html')

@auth.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        if not request.form['password'] == request.form['confirm password']:
            return render_template('register.html', error='Password doesn\'t match')
        if get_user(username=request.form['username']):
            return render_template('register.html', error='User already exist')
        add_user(username=request.form['username'],\
                  password=bcrypt.generate_password_hash(request.form['password']))
        session['username'] = request.form['username']
        return redirect(url_for('main.index'))
    elif request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('main.index'))
        else:
            return render_template('register.html')

@auth.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
    return redirect(url_for('main.index'))

@auth.route('/delete')
def delete():
    if 'username' in session:
        delete_user(username=session['username'])
        session.clear()
    return redirect(url_for('main.index'))