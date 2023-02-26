from flask import Flask, redirect, render_template, request, session, url_for

from . import question
from app.model import Question, Comment
from app.model_manage import add_question, get_question

@question.route('/')
def index():
    questions = Question.query.all()
    return render_template('questions.html', questions=questions)


@question.route('/<page_id>')
def page(page_id):
    return render_template('question_page.html', question=get_question(id=page_id))

@question.route('/add_question', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        if get_question(title=request.form['title']):
            return render_template('add_question.html', error='This question already exist')
        add_question(title=request.form['title'], content=request.form['description'])
        return redirect(url_for('question.index'))
    else:
        return render_template('add_question.html')