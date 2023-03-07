from flask import Flask, redirect, render_template, request, session, url_for

from . import question
from app.model import Question, Comment
from app.model_manage import add_question, get_question, update_question
from app.model_manage import add_comment, delete_comment as del_comment


@question.route('/')
def index():
    questions = Question.query.all()
    return render_template('questions.html', questions=questions)


@question.route('/<page_id>', methods=['GET', 'POST'])
def page(page_id):
    if request.method == 'POST':
        if request.form['submit'] == 'Add comment':
            add_comment(content=request.form['content'], question=get_question(id=page_id))
    question = get_question(id=page_id)
    if not 'username' in session:
        return render_template('question_page.html', question=question) 
    if session['username'] == question.user.username:
        return render_template('question_page.html', question=question, question_edit=True, current_username=session['username'])
    return render_template('question_page.html', question=question, current_username=session['username'])
    

@question.route('/<page_id>/<comment_id>')    
def delete_comment(page_id, comment_id):
    del_comment(id=comment_id)
    return redirect(url_for('question.page', page_id=page_id))


@question.route('/add_question', methods=['GET', 'POST'])
def add():
    if not 'username' in session:
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        if get_question(title=request.form['title']):
            return render_template('edit_question.html', error='This question already exist')
        add_question(title=request.form['title'], content=request.form['description'])
        return redirect(url_for('question.index'))
    else:
        return render_template('edit_question.html')
    
@question.route('/edit_question/<page_id>', methods=['GET', 'POST'])
def edit(page_id):
    if request.method == 'POST':
        question = get_question(title=request.form['title'])
        if question:
            if question.id != page_id:
                return render_template('edit_question.html', error='This question already exist')
        question = get_question(id=page_id)
        update_question(question=question, title=request.form['title'],\
                         content=request.form['content'])
        return redirect(url_for('question.page'), page_id=page_id)
    else:
        return render_template('edit_question.html')
    